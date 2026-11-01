from dataclasses import dataclass, field
from typing import Dict, List, Set, Any
from collections import deque
from data_loader import MovieNode

class MovieGraph:
    def __init__(self):
        self.id_hashmap: Dict[str, MovieNode] = {}
        self.title_hashmap: Dict[str, str] = {}
        self.adj_list: Dict[str, Dict[str, List[str]]] = {}

    @property
    def nodes(self) -> Dict[str, MovieNode]:
        return self.id_hashmap

    def __len__(self):
        return len(self.id_hashmap)

    def add_movie(self, movie: MovieNode):
        self.id_hashmap[movie.id] = movie
        self.title_hashmap[movie.title.lower()] = movie.id
        if movie.id not in self.adj_list:
            self.adj_list[movie.id] = {}

        for other_id, other_movie in self.id_hashmap.items():
            if other_id == movie.id:
                continue

            reasons = []
            if movie.director and movie.director == other_movie.director:
                reasons.append(f"Same director ({movie.director})")

            shared_cast = set(movie.cast).intersection(set(other_movie.cast))
            if shared_cast:
                reasons.append(f"Shared cast ({', '.join(shared_cast)})")

            shared_genres = set(movie.genres).intersection(set(other_movie.genres))
            if shared_genres:
                reasons.append(f"Shared genres ({', '.join(shared_genres)})")

            if reasons:
                self.adj_list[movie.id][other_id] = reasons
                if other_id not in self.adj_list:
                    self.adj_list[other_id] = {}
                self.adj_list[other_id][movie.id] = reasons

    def bfs_recommendations(self, start_id: str, max_depth: int = 2, filter_genres: List[str] = None) -> List[Dict[str, Any]]:
        if start_id not in self.id_hashmap:
            return []

        visited = {start_id}
        queue = deque([(start_id, 0, [])])
        recommendations = []

        filter_set = set(filter_genres) if filter_genres else None

        while queue:
            curr_id, depth, path_reasons = queue.popleft()

            if depth > 0:
                curr_node = self.id_hashmap[curr_id]
                if not filter_set or set(curr_node.genres).intersection(filter_set):
                    recommendations.append({
                        "node": curr_node,
                        "distance": depth,
                        "reasons": path_reasons
                    })

            if depth >= max_depth:
                continue

            for neighbor_id, reasons in self.adj_list.get(curr_id, {}).items():
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    queue.append((neighbor_id, depth + 1, reasons))

        return recommendations
