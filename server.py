import os
from typing import Dict, Any, List
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from data_loader import get_sample_movies, build_movie_graph, format_edge_reasons
from graph_engine import MovieGraph, MovieNode

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder=None)
CORS(app)

print("[Graph Engine] Initializing movie dataset and graph relations...")
movies = get_sample_movies()
graph: MovieGraph = build_movie_graph(movies)
print(f"[Graph Engine] Initialized {len(graph)} nodes and relationships successfully.")

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/assets/<path:filename>", methods=["GET"])
def serve_assets(filename):
    assets_dir = os.path.join(STATIC_DIR, "assets")
    return send_from_directory(assets_dir, filename)

@app.route("/static/<path:filename>", methods=["GET"])
def serve_static(filename):
    file_path = os.path.join(STATIC_DIR, filename)
    if os.path.exists(file_path):
        return send_from_directory(STATIC_DIR, filename)
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify([node.to_dict() for node in graph.nodes.values()])

@app.route("/api/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "GET":
        title = request.args.get("title", "")
        start_node = None
        for node in graph.nodes.values():
            if node.title.lower() == title.lower():
                start_node = node
                break
        if not start_node:
            return jsonify({"error": "Movie title not found"}), 404
        start_id = start_node.id
        max_depth = int(request.args.get("hops", 2))
        genres = []
    else:
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

    return jsonify({
        "target": graph.nodes[start_id].to_dict(),
        "recommendations": formatted_results
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
