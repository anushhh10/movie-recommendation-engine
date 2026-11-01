from dataclasses import dataclass, field
from typing import List, Dict, Set, Any

@dataclass(eq=False)
class MovieNode:
    id: str
    title: str
    year: int
    director: str
    cast: List[str]
    genres: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "cast": self.cast,
            "genres": self.genres
        }

def get_sample_movies() -> List[MovieNode]:
    movie_records = [
        {
            "id": "m1",
            "title": "Inception",
            "year": 2010,
            "director": "Christopher Nolan",
            "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy"],
            "genres": ["Action", "Sci-Fi", "Adventure"]
        },
        {
            "id": "m2",
            "title": "Interstellar",
            "year": 2014,
            "director": "Christopher Nolan",
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine"],
            "genres": ["Sci-Fi", "Drama", "Adventure"]
        },
        {
            "id": "m3",
            "title": "The Dark Knight",
            "year": 2008,
            "director": "Christopher Nolan",
            "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
            "genres": ["Action", "Crime", "Drama"]
        },
        {
            "id": "m4",
            "title": "Oppenheimer",
            "year": 2023,
            "director": "Christopher Nolan",
            "cast": ["Cillian Murphy", "Emily Blunt", "Matt Damon", "Robert Downey Jr."],
            "genres": ["Biography", "Drama", "History"]
        },
        {
            "id": "m71",
            "title": "Salaar: Part 1 – Ceasefire",
            "year": 2023,
            "director": "Prashanth Neel",
            "cast": ["Prabhas", "Prithviraj Sukumaran", "Shruti Haasan"],
            "genres": ["Action", "Drama", "Thriller"]
        },
        {
            "id": "m72",
            "title": "RRR",
            "year": 2022,
            "director": "S.S. Rajamouli",
            "cast": ["N.T. Rama Rao Jr.", "Ram Charan", "Alia Bhatt"],
            "genres": ["Action", "Drama", "History"]
        },
        {
            "id": "m73",
            "title": "Baahubali: The Beginning",
            "year": 2015,
            "director": "S.S. Rajamouli",
            "cast": ["Prabhas", "Rana Daggubati", "Anushka Shetty"],
            "genres": ["Action", "Fantasy", "Drama"]
        },
        {
            "id": "m74",
            "title": "Pushpa: The Rise",
            "year": 2021,
            "director": "Sukumar",
            "cast": ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"],
            "genres": ["Action", "Crime", "Drama"]
        },
        {
            "id": "m75",
            "title": "Kalki 2898 AD",
            "year": 2024,
            "director": "Nag Ashwin",
            "cast": ["Prabhas", "Amitabh Bachchan", "Kamal Haasan", "Deepika Padukone"],
            "genres": ["Sci-Fi", "Action"]
        },
        {
            "id": "m76",
            "title": "K.G.F: Chapter 1",
            "year": 2018,
            "director": "Prashanth Neel",
            "cast": ["Yash", "Srinidhi Shetty", "Sanjay Dutt"],
            "genres": ["Action", "Crime", "Drama"]
        },
        {
            "id": "m77",
            "title": "Fauzi",
            "year": 2026,
            "director": "Hanu Raghavapudi",
            "cast": ["Prabhas", "Imanvi Esmail", "Anupam Kher"],
            "genres": ["Action", "Drama", "History"]
        },
        {
            "id": "m78",
            "title": "Devara: Part 1",
            "year": 2024,
            "director": "Koratala Siva",
            "cast": ["N.T. Rama Rao Jr.", "Janhvi Kapoor", "Saif Ali Khan"],
            "genres": ["Action", "Drama"]
        }
    ]

    return [MovieNode(**data) for data in movie_records]

def build_movie_graph(movies: List[MovieNode]):
    from graph_engine import MovieGraph
    graph = MovieGraph()
    for m in movies:
        graph.add_movie(m)
    return graph

def format_edge_reasons(reasons: List[str]) -> str:
    return ", ".join(reasons)
