import os
from typing import Dict, Any, List
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from data_loader import get_sample_movies, build_movie_graph, format_edge_reasons
from graph_engine import MovieGraph, MovieNode

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Initialize Flask without default static routing to prevent route conflicts
app = Flask(__name__, static_folder=None)
CORS(app)

# Initialize graph once at startup
print("[Graph Engine] Initializing movie dataset and graph relations...")
movies = get_sample_movies()
graph: MovieGraph = build_movie_graph(movies)
print(f"[Graph Engine] Initialized {len(graph)} nodes and relationships successfully.")

@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    file_path = os.path.join(STATIC_DIR, path)
    if os.path.exists(file_path):
        return send_from_directory(STATIC_DIR, path)
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify([node.to_dict() for node in graph.nodes.values()])

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json() or {}
    start_id = data.get("movie_id")
    max_depth = data.get("max_depth", 2)
    genres = data.get("genres", [])

    if not start_id or start_id not in graph.nodes:
        return jsonify({"error": "Invalid or missing start movie ID"}), 400

    results = graph.bfs_recommendations(start_id=start_id, max_depth=max_depth, filter_genres=genres)
    
    formatted_results = []
    for item in results:
        node_dict = item["node"].to_dict()
        node_dict["distance"] = item["distance"]
        node_dict["reasons"] = item["reasons"]
        formatted_results.append(node_dict)

    return jsonify({"target": graph.nodes[start_id].to_dict(), "recommendations": formatted_results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
