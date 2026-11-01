"""
Relationship-Driven Movie Recommendation System - Graph Engine
Foundational graph data structures and BFS exploration algorithms.
"""

from collections import deque
from typing import Dict, List, Optional, Set, Tuple, Union, Any


class MovieNode:
    """
    Represents a movie entity vertex in the recommendation graph.
    
    Attributes:
        id: Unique identifier for the movie (e.g., 'm1', 'tt1375666').
        title: Title of the movie.
        year: Release year.
        director: Director's name.
        cast: List of primary actors/actresses.
        genres: List of genres.
        neighbors: Set of adjacent MovieNode instances in the undirected graph.
    """

    def __init__(
        self,
        id: str,
        title: str,
        year: int,
        director: str,
        cast: List[str],
        genres: List[str],
    ) -> None:
        self.id: str = str(id)
        self.title: str = title
        self.year: int = int(year)
        self.director: str = director
        self.cast: List[str] = list(cast)
        self.genres: List[str] = list(genres)
        self.neighbors: Set["MovieNode"] = set()

    def add_neighbor(self, neighbor: "MovieNode") -> None:
        """Adds an adjacent MovieNode to the neighbors set."""
        if neighbor is not self:
            self.neighbors.add(neighbor)

    def __hash__(self) -> int:
        """Hash by unique identifier for set and dictionary hashing."""
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        """Equality based on unique identifier."""
        if isinstance(other, MovieNode):
            return self.id == other.id
        return False

    def __repr__(self) -> str:
        return f"MovieNode(id={self.id!r}, title={self.title!r}, year={self.year})"

    def to_dict(self) -> Dict[str, Any]:
        """Serializes basic node attributes to dictionary format."""
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "cast": self.cast,
            "genres": self.genres,
            "neighbor_count": len(self.neighbors),
        }


class MovieGraph:
    """
    Undirected graph representing movie nodes and relational edges.
    
    Provides O(1) hash map lookups for node retrieval by ID or normalized title,
    as well as level-based BFS recommendation traversals.
    """

    def __init__(self) -> None:
        # O(1) HashMap: Normalized Title -> MovieNode
        self.title_hashmap: Dict[str, MovieNode] = {}
        # O(1) HashMap: ID -> MovieNode
        self.id_hashmap: Dict[str, MovieNode] = {}
        # Stores edge attributes / connection reasons: (id_a, id_b) -> metadata dict
        self._edge_metadata: Dict[Tuple[str, str], Dict[str, Any]] = {}

    @staticmethod
    def _normalize_title(title: str) -> str:
        """Normalizes movie titles for case-insensitive and trimmed O(1) lookups."""
        return title.strip().lower()

    def add_movie(self, movie: MovieNode) -> None:
        """
        Adds a MovieNode to the graph index structures.
        
        Complexity: O(1) average time.
        """
        if not isinstance(movie, MovieNode):
            raise TypeError("Movie must be an instance of MovieNode")

        self.id_hashmap[movie.id] = movie
        normalized_title = self._normalize_title(movie.title)
        self.title_hashmap[normalized_title] = movie

    def get_movie_by_id(self, movie_id: str) -> Optional[MovieNode]:
        """O(1) lookup by movie ID."""
        return self.id_hashmap.get(str(movie_id))

    def get_movie_by_title(self, title: str) -> Optional[MovieNode]:
        """O(1) lookup by movie title (case-insensitive)."""
        return self.title_hashmap.get(self._normalize_title(title))

    def add_relationship(
        self,
        movie_a: Union[MovieNode, str],
        movie_b: Union[MovieNode, str],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Creates an undirected edge between two movie nodes.
        
        Args:
            movie_a: MovieNode instance, ID, or title.
            movie_b: MovieNode instance, ID, or title.
            metadata: Optional dictionary describing edge relationships (e.g. shared cast/director).
        """
        node_a = self._resolve_node(movie_a)
        node_b = self._resolve_node(movie_b)

        if node_a is None:
            raise KeyError(f"Movie '{movie_a}' not found in graph.")
        if node_b is None:
            raise KeyError(f"Movie '{movie_b}' not found in graph.")
        if node_a == node_b:
            return  # Avoid self-loops

        # Undirected edge: mutual neighbor addition
        node_a.add_neighbor(node_b)
        node_b.add_neighbor(node_a)

        # Store symmetrical edge metadata
        if metadata:
            edge_key_1 = (node_a.id, node_b.id)
            edge_key_2 = (node_b.id, node_a.id)
            self._edge_metadata[edge_key_1] = metadata
            self._edge_metadata[edge_key_2] = metadata

    def get_relationship_metadata(
        self,
        movie_a: Union[MovieNode, str],
        movie_b: Union[MovieNode, str],
    ) -> Dict[str, Any]:
        """Retrieves stored metadata between two connected nodes."""
        node_a = self._resolve_node(movie_a)
        node_b = self._resolve_node(movie_b)
        if node_a and node_b:
            return self._edge_metadata.get((node_a.id, node_b.id), {})
        return {}

    def _resolve_node(self, movie_ref: Union[MovieNode, str]) -> Optional[MovieNode]:
        """Resolves a MovieNode reference from instance, ID, or title."""
        if isinstance(movie_ref, MovieNode):
            return movie_ref
        if isinstance(movie_ref, str):
            # Try ID first, then normalized title
            return self.get_movie_by_id(movie_ref) or self.get_movie_by_title(movie_ref)
        return None

    def bfs_recommendations(
        self,
        start_title: str,
        max_depth: int = 2,
    ) -> Dict[str, Any]:
        """
        Performs Breadth-First Search (BFS) recommendation traversal using a FIFO queue.
        
        Traverses relationships up to `max_depth` (e.g., Level 1: direct connections,
        Level 2: 2nd-degree extended connections).
        
        Args:
            start_title: Title of the seed movie to explore from.
            max_depth: Maximum exploration depth/level (default 2).
            
        Returns:
            Dictionary containing:
                - target_node: Seed MovieNode.
                - visited_nodes: List of tuples (MovieNode, level) in discovery order.
                - edges: List of tuples (from_node, to_node, level) traversed.
                - visited_by_level: Dict mapping level -> list of MovieNode instances.
        """
        start_node = self.get_movie_by_title(start_title)
        if start_node is None:
            raise KeyError(f"Seed movie '{start_title}' not found in the graph.")

        # FIFO queue storing (current_node, current_level)
        queue: deque[Tuple[MovieNode, int]] = deque()
        queue.append((start_node, 0))

        # Track visited nodes and their discovery level
        visited_levels: Dict[str, int] = {start_node.id: 0}
        visited_nodes: List[Tuple[MovieNode, int]] = [(start_node, 0)]
        visited_by_level: Dict[int, List[MovieNode]] = {0: [start_node]}
        edges: List[Tuple[MovieNode, MovieNode, int]] = []

        for level in range(1, max_depth + 1):
            visited_by_level[level] = []

        while queue:
            current_node, current_level = queue.popleft()

            # If current node has reached max_depth, do not expand further
            if current_level >= max_depth:
                continue

            next_level = current_level + 1

            # Traverse neighbors
            # Sort neighbors by title for deterministic exploration ordering
            sorted_neighbors = sorted(current_node.neighbors, key=lambda n: n.title)

            for neighbor in sorted_neighbors:
                if neighbor.id not in visited_levels:
                    visited_levels[neighbor.id] = next_level
                    visited_nodes.append((neighbor, next_level))
                    visited_by_level[next_level].append(neighbor)
                    edges.append((current_node, neighbor, next_level))
                    queue.append((neighbor, next_level))
                elif visited_levels[neighbor.id] == next_level:
                    # Edge leading to a node discovered at the same next_level via an alternate path
                    edge_candidate = (current_node, neighbor, next_level)
                    reverse_edge = (neighbor, current_node, next_level)
                    if edge_candidate not in edges and reverse_edge not in edges:
                        edges.append(edge_candidate)

        return {
            "target_node": start_node,
            "visited_nodes": visited_nodes,
            "edges": edges,
            "visited_by_level": visited_by_level,
        }

    def __len__(self) -> int:
        return len(self.id_hashmap)

    def __repr__(self) -> str:
        edge_count = sum(len(node.neighbors) for node in self.id_hashmap.values()) // 2
        return f"MovieGraph(nodes={len(self.id_hashmap)}, edges={edge_count})"
