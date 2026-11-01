"""
Relationship-Driven Movie Recommendation System - Flask API Server
Exposes graph search and BFS recommendation engine endpoints via HTTP.
"""

import os
from typing import Dict, Any, List
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from data_loader import get_sample_movies, build_movie_graph, format_edge_reasons
from graph_engine import MovieGraph, MovieNode

# Initialize Flask application with static directory
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="/static")
CORS(app)  # Enable Cross-Origin Resource Sharing

# Initialize graph once at startup
print("[Graph Engine] Initializing movie dataset and graph relations...")
_movies = get_sample_movies()
graph: MovieGraph = build_movie_graph(_movies)
print(f"[Graph Engine] Initialized {len(graph)} nodes and relationships successfully.")


@app.route("/", methods=["GET"])
def index():
    """Serves index.html from static directory if present, or API metadata."""
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return send_from_directory(STATIC_DIR, "index.html")
    return jsonify({
        "status": "online",
        "service": "Relationship-Driven Movie Recommendation API",
        "endpoints": {
            "/api/recommend": "GET ?title=<movie_title>&hops=<1-5> - BFS recommendations",
            "/api/search": "GET ?query=<string> - O(1) title lookup & matching",
            "/api/movies": "GET - List all indexed movies",
        },
        "stats": {
            "total_movies": len(graph),
        }
    })


@app.route("/api/recommend", methods=["GET"])
def recommend_movies():
    """
    Executes BFS recommendations from a seed movie title.
    
    Query Params:
        title (str): Required seed movie title (case-insensitive).
        hops (int): Optional exploration depth / levels (default: 2, range: 1..5).
        
    Returns:
        JSON: {
            "target": { ...movie details... },
            "nodes": [ ...movie details with level indicator 0, 1, 2... ],
            "edges": [ ...relational edges with metadata... ]
        }
    """
    title = request.args.get("title", "").strip()
    if not title:
        return jsonify({
            "error": "Missing required query parameter: 'title'",
            "example": "/api/recommend?title=Inception&hops=2"
        }), 400

    hops_raw = request.args.get("hops", "2")
    try:
        hops = int(hops_raw)
        if hops < 1:
            hops = 1
        elif hops > 5:
            hops = 5  # Clamp upper bound for performance safety
    except ValueError:
        return jsonify({"error": f"Invalid 'hops' parameter '{hops_raw}'. Must be an integer."}), 400

    # Retrieve movie node
    target_node = graph.get_movie_by_title(title)
    if target_node is None:
        return jsonify({
            "error": f"Movie '{title}' not found in graph database.",
            "available_titles": [m.title for m in graph.id_hashmap.values()]
        }), 404

    # Run BFS recommendation traversal
    bfs_result = graph.bfs_recommendations(start_title=title, max_depth=hops)
    
    # Format nodes payload with level indicators
    nodes_payload: List[Dict[str, Any]] = []
    for node, level in bfs_result["visited_nodes"]:
        node_dict = node.to_dict()
        node_dict["level"] = level
        nodes_payload.append(node_dict)

    # Format edges payload with relationship reasons and metadata
    edges_payload: List[Dict[str, Any]] = []
    for source_node, target_node_rel, level in bfs_result["edges"]:
        metadata = graph.get_relationship_metadata(source_node, target_node_rel)
        edge_data = {
            "source": source_node.id,
            "target": target_node_rel.id,
            "source_title": source_node.title,
            "target_title": target_node_rel.title,
            "level": level,
            "relationship": format_edge_reasons(metadata),
            "metadata": metadata,
        }
        edges_payload.append(edge_data)

    return jsonify({
        "target": target_node.to_dict(),
        "nodes": nodes_payload,
        "edges": edges_payload,
        "hops": hops,
        "total_nodes": len(nodes_payload),
        "total_edges": len(edges_payload),
    })


@app.route("/api/search", methods=["GET"])
def search_movies():
    """
    Checks if a movie title exists via O(1) title_hashmap and provides matching titles.
    
    Query Params:
        query (str): Movie title or substring search query.
        
    Returns:
        JSON: {
            "query": str,
            "exists": bool,
            "exact_match": Optional[dict],
            "matches": List[dict]
        }
    """
    query = request.args.get("query", "").strip()
    if not query:
        # Return all indexed movies
        all_movies = [node.to_dict() for node in graph.id_hashmap.values()]
        return jsonify({
            "query": "",
            "exists": False,
            "exact_match": None,
            "matches": all_movies,
            "total": len(all_movies)
        })

    # O(1) exact normalized match check
    normalized_query = graph._normalize_title(query)
    exact_match_node = graph.title_hashmap.get(normalized_query)

    # Substring / fuzzy matches across all indexed movies
    matches: List[Dict[str, Any]] = []
    for norm_title, node in graph.title_hashmap.items():
        if normalized_query in norm_title or any(normalized_query in actor.lower() for actor in node.cast):
            matches.append(node.to_dict())

    # Ensure exact match is placed first if present
    if exact_match_node:
        matches = [m for m in matches if m["id"] != exact_match_node.id]
        matches.insert(0, exact_match_node.to_dict())

    return jsonify({
        "query": query,
        "exists": exact_match_node is not None,
        "exact_match": exact_match_node.to_dict() if exact_match_node else None,
        "matches": matches,
        "total_matches": len(matches)
    })


@app.route("/api/movies", methods=["GET"])
def list_movies():
    """Returns list of all indexed movies in the graph."""
    movies_list = [node.to_dict() for node in sorted(graph.id_hashmap.values(), key=lambda m: m.title)]
    return jsonify({
        "movies": movies_list,
        "total": len(movies_list)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Relationship-Driven Movie Recommendation Server on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=False)
