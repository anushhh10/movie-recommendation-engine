"""
Relationship-Driven Movie Recommendation System - Scaled Data Loader
Features a curated corpus of 70+ interconnected blockbuster and auteur films
spanning Action, Sci-Fi, Crime, Drama, Thriller, Comedy, Adventure, Romance,
Fantasy, Horror, Mystery, and Animation.
"""

from typing import List, Dict, Any
from graph_engine import MovieNode, MovieGraph


def get_sample_movies() -> List[MovieNode]:
    """
    Returns a robust dataset of 70+ interconnected popular movies.
    Dense interconnections across directors and ensemble casts ensure BFS
    returns rich 15-30+ recommendation trees.
    """
    movie_records = [
        # --- Christopher Nolan Universe ---
        {
            "id": "m1",
            "title": "Inception",
            "year": 2010,
            "director": "Christopher Nolan",
            "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy", "Cillian Murphy", "Michael Caine"],
            "genres": ["Action", "Sci-Fi", "Adventure"],
        },
        {
            "id": "m2",
            "title": "The Dark Knight",
            "year": 2008,
            "director": "Christopher Nolan",
            "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine", "Cillian Murphy", "Gary Oldman", "Morgan Freeman"],
            "genres": ["Action", "Crime", "Drama"],
        },
        {
            "id": "m3",
            "title": "Interstellar",
            "year": 2014,
            "director": "Christopher Nolan",
            "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine", "Matt Damon", "Timothée Chalamet"],
            "genres": ["Sci-Fi", "Adventure", "Drama"],
        },
        {
            "id": "m4",
            "title": "The Prestige",
            "year": 2006,
            "director": "Christopher Nolan",
            "cast": ["Christian Bale", "Hugh Jackman", "Scarlett Johansson", "Michael Caine", "David Bowie"],
            "genres": ["Drama", "Mystery", "Sci-Fi"],
        },
        {
            "id": "m5",
            "title": "Oppenheimer",
            "year": 2023,
            "director": "Christopher Nolan",
            "cast": ["Cillian Murphy", "Emily Blunt", "Matt Damon", "Robert Downey Jr.", "Florence Pugh", "Gary Oldman"],
            "genres": ["Biography", "Drama", "History"],
        },
        {
            "id": "m6",
            "title": "Dunkirk",
            "year": 2017,
            "director": "Christopher Nolan",
            "cast": ["Fionn Whitehead", "Tom Glynn-Carney", "Jack Lowden", "Harry Styles", "Cillian Murphy", "Tom Hardy", "Kenneth Branagh"],
            "genres": ["Action", "Drama", "History"],
        },
        {
            "id": "m7",
            "title": "Batman Begins",
            "year": 2005,
            "director": "Christopher Nolan",
            "cast": ["Christian Bale", "Michael Caine", "Liam Neeson", "Katie Holmes", "Gary Oldman", "Cillian Murphy", "Morgan Freeman"],
            "genres": ["Action", "Crime", "Drama"],
        },
        {
            "id": "m8",
            "title": "Tenet",
            "year": 2020,
            "director": "Christopher Nolan",
            "cast": ["John David Washington", "Robert Pattinson", "Elizabeth Debicki", "Kenneth Branagh", "Michael Caine"],
            "genres": ["Action", "Sci-Fi", "Thriller"],
        },
        {
            "id": "m9",
            "title": "Memento",
            "year": 2000,
            "director": "Christopher Nolan",
            "cast": ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"],
            "genres": ["Mystery", "Thriller"],
        },

        # --- Martin Scorsese & Leonardo DiCaprio Universe ---
        {
            "id": "m10",
            "title": "Shutter Island",
            "year": 2010,
            "director": "Martin Scorsese",
            "cast": ["Leonardo DiCaprio", "Mark Ruffalo", "Ben Kingsley", "Michelle Williams", "Max von Sydow"],
            "genres": ["Mystery", "Thriller", "Horror"],
        },
        {
            "id": "m11",
            "title": "The Departed",
            "year": 2006,
            "director": "Martin Scorsese",
            "cast": ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson", "Mark Wahlberg", "Martin Sheen", "Vera Farmiga"],
            "genres": ["Crime", "Drama", "Thriller"],
        },
        {
            "id": "m12",
            "title": "The Wolf of Wall Street",
            "year": 2013,
            "director": "Martin Scorsese",
            "cast": ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie", "Matthew McConaughey", "Kyle Chandler"],
            "genres": ["Biography", "Comedy", "Crime"],
        },
        {
            "id": "m13",
            "title": "Goodfellas",
            "year": 1990,
            "director": "Martin Scorsese",
            "cast": ["Robert De Niro", "Ray Liotta", "Joe Pesci", "Lorraine Bracco", "Samuel L. Jackson"],
            "genres": ["Biography", "Crime", "Drama"],
        },
        {
            "id": "m14",
            "title": "Casino",
            "year": 1995,
            "director": "Martin Scorsese",
            "cast": ["Robert De Niro", "Sharon Stone", "Joe Pesci", "James Woods"],
            "genres": ["Crime", "Drama"],
        },
        {
            "id": "m15",
            "title": "Taxi Driver",
            "year": 1976,
            "director": "Martin Scorsese",
            "cast": ["Robert De Niro", "Jodie Foster", "Cybill Shepherd", "Harvey Keitel"],
            "genres": ["Crime", "Drama"],
        },
        {
            "id": "m16",
            "title": "The Irishman",
            "year": 2019,
            "director": "Martin Scorsese",
            "cast": ["Robert De Niro", "Al Pacino", "Joe Pesci", "Harvey Keitel", "Anna Paquin"],
            "genres": ["Biography", "Crime", "Drama"],
        },
        {
            "id": "m17",
            "title": "Killers of the Flower Moon",
            "year": 2023,
            "director": "Martin Scorsese",
            "cast": ["Leonardo DiCaprio", "Robert De Niro", "Lily Gladstone", "Jesse Plemons", "Brendan Fraser"],
            "genres": ["Crime", "Drama", "History"],
        },
        {
            "id": "m18",
            "title": "Catch Me If You Can",
            "year": 2002,
            "director": "Steven Spielberg",
            "cast": ["Leonardo DiCaprio", "Tom Hanks", "Christopher Walken", "Martin Sheen", "Amy Adams"],
            "genres": ["Biography", "Crime", "Drama"],
        },
        {
            "id": "m19",
            "title": "The Revenant",
            "year": 2015,
            "director": "Alejandro G. Iñárritu",
            "cast": ["Leonardo DiCaprio", "Tom Hardy", "Domhnall Gleeson", "Will Poulter"],
            "genres": ["Action", "Adventure", "Drama"],
        },
        {
            "id": "m20",
            "title": "Titanic",
            "year": 1997,
            "director": "James Cameron",
            "cast": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates", "Bill Paxton"],
            "genres": ["Drama", "Romance"],
        },

        # --- Quentin Tarantino Universe ---
        {
            "id": "m21",
            "title": "Django Unchained",
            "year": 2012,
            "director": "Quentin Tarantino",
            "cast": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio", "Kerry Washington", "Samuel L. Jackson"],
            "genres": ["Drama", "Western", "Action"],
        },
        {
            "id": "m22",
            "title": "Once Upon a Time in Hollywood",
            "year": 2019,
            "director": "Quentin Tarantino",
            "cast": ["Leonardo DiCaprio", "Brad Pitt", "Margot Robbie", "Emile Hirsch", "Al Pacino"],
            "genres": ["Comedy", "Drama"],
        },
        {
            "id": "m23",
            "title": "Pulp Fiction",
            "year": 1994,
            "director": "Quentin Tarantino",
            "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis", "Harvey Keitel", "Christopher Walken"],
            "genres": ["Crime", "Drama"],
        },
        {
            "id": "m24",
            "title": "Inglourious Basterds",
            "year": 2009,
            "director": "Quentin Tarantino",
            "cast": ["Brad Pitt", "Christoph Waltz", "Michael Fassbender", "Eli Roth", "Diane Kruger"],
            "genres": ["Adventure", "Drama", "War"],
        },
        {
            "id": "m25",
            "title": "Kill Bill: Vol. 1",
            "year": 2003,
            "director": "Quentin Tarantino",
            "cast": ["Uma Thurman", "Lucy Liu", "Vivica A. Fox", "Daryl Hannah", "David Carradine"],
            "genres": ["Action", "Crime", "Thriller"],
        },

        # --- David Fincher Universe ---
        {
            "id": "m26",
            "title": "Fight Club",
            "year": 1999,
            "director": "David Fincher",
            "cast": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter", "Meat Loaf", "Jared Leto"],
            "genres": ["Drama", "Thriller"],
        },
        {
            "id": "m27",
            "title": "Se7en",
            "year": 1995,
            "director": "David Fincher",
            "cast": ["Brad Pitt", "Morgan Freeman", "Gwyneth Paltrow", "Kevin Spacey"],
            "genres": ["Crime", "Drama", "Mystery"],
        },
        {
            "id": "m28",
            "title": "Zodiac",
            "year": 2007,
            "director": "David Fincher",
            "cast": ["Jake Gyllenhaal", "Mark Ruffalo", "Robert Downey Jr.", "Anthony Edwards", "Brian Cox"],
            "genres": ["Crime", "Drama", "Mystery"],
        },
        {
            "id": "m29",
            "title": "The Social Network",
            "year": 2010,
            "director": "David Fincher",
            "cast": ["Jesse Eisenberg", "Andrew Garfield", "Justin Timberlake", "Armie Hammer", "Rooney Mara"],
            "genres": ["Biography", "Drama"],
        },
        {
            "id": "m30",
            "title": "Gone Girl",
            "year": 2014,
            "director": "David Fincher",
            "cast": ["Ben Affleck", "Rosamund Pike", "Neil Patrick Harris", "Tyler Perry"],
            "genres": ["Drama", "Mystery", "Thriller"],
        },

        # --- Denis Villeneuve Sci-Fi & Drama Universe ---
        {
            "id": "m31",
            "title": "Dune",
            "year": 2021,
            "director": "Denis Villeneuve",
            "cast": ["Timothée Chalamet", "Rebecca Ferguson", "Oscar Isaac", "Josh Brolin", "Zendaya", "Jason Momoa", "Javier Bardem"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m32",
            "title": "Blade Runner 2049",
            "year": 2017,
            "director": "Denis Villeneuve",
            "cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas", "Sylvia Hoeks", "Robin Wright", "Dave Bautista"],
            "genres": ["Action", "Drama", "Sci-Fi"],
        },
        {
            "id": "m33",
            "title": "Arrival",
            "year": 2016,
            "director": "Denis Villeneuve",
            "cast": ["Amy Adams", "Jeremy Renner", "Forest Whitaker", "Michael Stuhlbarg"],
            "genres": ["Drama", "Mystery", "Sci-Fi"],
        },
        {
            "id": "m34",
            "title": "Sicario",
            "year": 2015,
            "director": "Denis Villeneuve",
            "cast": ["Emily Blunt", "Benicio Del Toro", "Josh Brolin", "Victor Garber", "Jon Bernthal"],
            "genres": ["Action", "Crime", "Drama"],
        },
        {
            "id": "m35",
            "title": "Prisoners",
            "year": 2013,
            "director": "Denis Villeneuve",
            "cast": ["Hugh Jackman", "Jake Gyllenhaal", "Viola Davis", "Maria Bello", "Terrence Howard", "Paul Dano"],
            "genres": ["Crime", "Drama", "Mystery"],
        },

        # --- Steven Spielberg Classics ---
        {
            "id": "m36",
            "title": "Saving Private Ryan",
            "year": 1998,
            "director": "Steven Spielberg",
            "cast": ["Tom Hanks", "Matt Damon", "Tom Sizemore", "Edward Burns", "Vin Diesel", "Barry Pepper"],
            "genres": ["Drama", "War", "Action"],
        },
        {
            "id": "m37",
            "title": "Jurassic Park",
            "year": 1993,
            "director": "Steven Spielberg",
            "cast": ["Sam Neill", "Laura Dern", "Jeff Goldblum", "Richard Attenborough", "Samuel L. Jackson"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m38",
            "title": "Raiders of the Lost Ark",
            "year": 1981,
            "director": "Steven Spielberg",
            "cast": ["Harrison Ford", "Karen Allen", "Paul Freeman", "John Rhys-Davies"],
            "genres": ["Action", "Adventure"],
        },
        {
            "id": "m39",
            "title": "Schindler's List",
            "year": 1993,
            "director": "Steven Spielberg",
            "cast": ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes", "Caroline Goodall"],
            "genres": ["Biography", "Drama", "History"],
        },

        # --- Marvel Cinematic Universe & Ensembles ---
        {
            "id": "m40",
            "title": "Iron Man",
            "year": 2008,
            "director": "Jon Favreau",
            "cast": ["Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard", "Jeff Bridges", "Samuel L. Jackson"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m41",
            "title": "The Avengers",
            "year": 2012,
            "director": "Joss Whedon",
            "cast": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth", "Scarlett Johansson", "Jeremy Renner", "Samuel L. Jackson"],
            "genres": ["Action", "Sci-Fi", "Adventure"],
        },
        {
            "id": "m42",
            "title": "Avengers: Infinity War",
            "year": 2018,
            "director": "Anthony Russo, Joe Russo",
            "cast": ["Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo", "Chris Evans", "Scarlett Johansson", "Benedict Cumberbatch", "Josh Brolin", "Tom Holland"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m43",
            "title": "Avengers: Endgame",
            "year": 2019,
            "director": "Anthony Russo, Joe Russo",
            "cast": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth", "Scarlett Johansson", "Jeremy Renner", "Paul Rudd", "Brie Larson"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m44",
            "title": "Guardians of the Galaxy",
            "year": 2014,
            "director": "James Gunn",
            "cast": ["Chris Pratt", "Zoe Saldana", "Dave Bautista", "Vin Diesel", "Bradley Cooper", "Benicio Del Toro"],
            "genres": ["Action", "Adventure", "Comedy"],
        },

        # --- Modern Blockbusters & Prestige Hits ---
        {
            "id": "m45",
            "title": "Ford v Ferrari",
            "year": 2019,
            "director": "James Mangold",
            "cast": ["Christian Bale", "Matt Damon", "Jon Bernthal", "Caitriona Balfe", "Josh Lucas"],
            "genres": ["Action", "Biography", "Drama"],
        },
        {
            "id": "m46",
            "title": "Logan",
            "year": 2017,
            "director": "James Mangold",
            "cast": ["Hugh Jackman", "Patrick Stewart", "Dafne Keen", "Boyd Holbrook", "Stephen Merchant"],
            "genres": ["Action", "Drama", "Sci-Fi"],
        },
        {
            "id": "m47",
            "title": "The Martian",
            "year": 2015,
            "director": "Ridley Scott",
            "cast": ["Matt Damon", "Jessica Chastain", "Kristen Wiig", "Jeff Daniels", "Michael Peña", "Chiwetel Ejiofor"],
            "genres": ["Adventure", "Drama", "Sci-Fi"],
        },
        {
            "id": "m48",
            "title": "Gladiator",
            "year": 2000,
            "director": "Ridley Scott",
            "cast": ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen", "Oliver Reed", "Richard Harris"],
            "genres": ["Action", "Adventure", "Drama"],
        },
        {
            "id": "m49",
            "title": "Alien",
            "year": 1979,
            "director": "Ridley Scott",
            "cast": ["Sigourney Weaver", "Tom Skerritt", "John Hurt", "Veronica Cartwright", "Ian Holm"],
            "genres": ["Horror", "Sci-Fi"],
        },
        {
            "id": "m50",
            "title": "Avatar",
            "year": 2009,
            "director": "James Cameron",
            "cast": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver", "Stephen Lang", "Michelle Rodriguez"],
            "genres": ["Action", "Adventure", "Fantasy"],
        },
        {
            "id": "m51",
            "title": "The Matrix",
            "year": 1999,
            "director": "Lana Wachowski, Lilly Wachowski",
            "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving", "Joe Pantoliano"],
            "genres": ["Action", "Sci-Fi"],
        },
        {
            "id": "m52",
            "title": "John Wick",
            "year": 2014,
            "director": "Chad Stahelski",
            "cast": ["Keanu Reeves", "Michael Nyqvist", "Alfie Allen", "Willem Dafoe", "Ian McShane"],
            "genres": ["Action", "Crime", "Thriller"],
        },
        {
            "id": "m53",
            "title": "Mad Max: Fury Road",
            "year": 2015,
            "director": "George Miller",
            "cast": ["Tom Hardy", "Charlize Theron", "Nicholas Hoult", "Hugh Keays-Byrne"],
            "genres": ["Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m54",
            "title": "Barbie",
            "year": 2023,
            "director": "Greta Gerwig",
            "cast": ["Margot Robbie", "Ryan Gosling", "America Ferrera", "Kate McKinnon", "Will Ferrell", "Simu Liu"],
            "genres": ["Adventure", "Comedy", "Fantasy"],
        },
        {
            "id": "m55",
            "title": "Little Women",
            "year": 2019,
            "director": "Greta Gerwig",
            "cast": ["Saoirse Ronan", "Emma Watson", "Florence Pugh", "Eliza Scanlen", "Laura Dern", "Timothée Chalamet", "Meryl Streep"],
            "genres": ["Drama", "Romance"],
        },
        {
            "id": "m56",
            "title": "La La Land",
            "year": 2016,
            "director": "Damien Chazelle",
            "cast": ["Ryan Gosling", "Emma Stone", "John Legend", "Rosemarie DeWitt", "J.K. Simmons"],
            "genres": ["Comedy", "Drama", "Music", "Romance"],
        },
        {
            "id": "m57",
            "title": "Whiplash",
            "year": 2014,
            "director": "Damien Chazelle",
            "cast": ["Miles Teller", "J.K. Simmons", "Paul Reiser", "Melissa Benoist"],
            "genres": ["Drama", "Music"],
        },
        {
            "id": "m58",
            "title": "Her",
            "year": 2013,
            "director": "Spike Jonze",
            "cast": ["Joaquin Phoenix", "Scarlett Johansson", "Amy Adams", "Rooney Mara", "Chris Pratt"],
            "genres": ["Drama", "Romance", "Sci-Fi"],
        },
        {
            "id": "m59",
            "title": "Marriage Story",
            "year": 2019,
            "director": "Noah Baumbach",
            "cast": ["Scarlett Johansson", "Adam Driver", "Laura Dern", "Alan Alda", "Ray Liotta"],
            "genres": ["Comedy", "Drama", "Romance"],
        },
        {
            "id": "m60",
            "title": "The Shawshank Redemption",
            "year": 1994,
            "director": "Frank Darabont",
            "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler", "Clancy Brown"],
            "genres": ["Drama"],
        },
        {
            "id": "m61",
            "title": "The Godfather",
            "year": 1972,
            "director": "Francis Ford Coppola",
            "cast": ["Marlon Brando", "Al Pacino", "James Caan", "Robert Duvall", "Diane Keaton"],
            "genres": ["Crime", "Drama"],
        },
        {
            "id": "m62",
            "title": "Spotlight",
            "year": 2015,
            "director": "Tom McCarthy",
            "cast": ["Mark Ruffalo", "Michael Keaton", "Rachel McAdams", "Liev Schreiber", "John Slattery", "Stanley Tucci"],
            "genres": ["Biography", "Crime", "Drama"],
        },
        {
            "id": "m63",
            "title": "Knives Out",
            "year": 2019,
            "director": "Rian Johnson",
            "cast": ["Daniel Craig", "Chris Evans", "Ana de Armas", "Jamie Lee Curtis", "Michael Shannon", "Don Johnson", "Christopher Plummer"],
            "genres": ["Comedy", "Crime", "Drama", "Mystery"],
        },
        {
            "id": "m64",
            "title": "The Grand Budapest Hotel",
            "year": 2014,
            "director": "Wes Anderson",
            "cast": ["Ralph Fiennes", "F. Murray Abraham", "Mathieu Amalric", "Adrien Brody", "Willem Dafoe", "Jeff Goldblum", "Harvey Keitel", "Edward Norton", "Saoirse Ronan"],
            "genres": ["Adventure", "Comedy", "Crime"],
        },
        {
            "id": "m65",
            "title": "Get Out",
            "year": 2017,
            "director": "Jordan Peele",
            "cast": ["Daniel Kaluuya", "Allison Williams", "Bradley Whitford", "Catherine Keener", "Caleb Landry Jones", "Lakeith Stanfield"],
            "genres": ["Horror", "Mystery", "Thriller"],
        },
        {
            "id": "m66",
            "title": "A Quiet Place",
            "year": 2018,
            "director": "John Krasinski",
            "cast": ["Emily Blunt", "John Krasinski", "Millicent Simmonds", "Noah Jupe"],
            "genres": ["Drama", "Horror", "Sci-Fi"],
        },
        {
            "id": "m67",
            "title": "Parasite",
            "year": 2019,
            "director": "Bong Joon-ho",
            "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong", "Choi Woo-shik", "Park So-dam"],
            "genres": ["Drama", "Thriller"],
        },
        {
            "id": "m68",
            "title": "Spider-Man: Into the Spider-Verse",
            "year": 2018,
            "director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
            "cast": ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld", "Mahershala Ali", "Brian Tyree Henry", "Lily Tomlin", "Nicolas Cage", "Liev Schreiber"],
            "genres": ["Animation", "Action", "Adventure", "Sci-Fi"],
        },
        {
            "id": "m69",
            "title": "The Lord of the Rings: The Fellowship of the Ring",
            "year": 2001,
            "director": "Peter Jackson",
            "cast": ["Elijah Wood", "Ian McKellen", "Viggo Mortensen", "Orlando Bloom", "Sean Astin", "Cate Blanchett", "Hugo Weaving", "Christopher Lee"],
            "genres": ["Action", "Adventure", "Drama", "Fantasy"],
        },
        {
            "id": "m70",
            "title": "Forrest Gump",
            "year": 1994,
            "director": "Robert Zemeckis",
            "cast": ["Tom Hanks", "Robin Wright", "Gary Sinise", "Mykelti Williamson", "Sally Field"],
            "genres": ["Drama", "Romance"],
        },
    ]

    return [MovieNode(**data) for data in movie_records]


def build_movie_graph(movies: List[MovieNode]) -> MovieGraph:
    """
    Initializes a MovieGraph, inserts movie nodes, and automatically synthesizes
    undirected edges between movies sharing a director or cast members.
    """
    graph = MovieGraph()

    # Step 1: Add all movie nodes into O(1) hash structures
    for movie in movies:
        graph.add_movie(movie)

    # Step 2: Automatically infer relationships pairwise
    n = len(movies)
    for i in range(n):
        for j in range(i + 1, n):
            m1 = movies[i]
            m2 = movies[j]

            # Directorial connection
            shared_director = (m1.director == m2.director)
            
            # Cast connection (intersection of cast lists)
            shared_cast = sorted(list(set(m1.cast) & set(m2.cast)))

            if shared_director or shared_cast:
                metadata: Dict[str, Any] = {
                    "shared_director": m1.director if shared_director else None,
                    "shared_cast": shared_cast,
                }
                graph.add_relationship(m1, m2, metadata=metadata)

    return graph


def format_edge_reasons(metadata: Dict[str, Any]) -> str:
    """Helper to format relationship metadata into human-readable strings."""
    reasons = []
    if metadata.get("shared_director"):
        reasons.append(f"Director: {metadata['shared_director']}")
    if metadata.get("shared_cast"):
        cast_str = ", ".join(metadata["shared_cast"])
        reasons.append(f"Cast: [{cast_str}]")
    return " | ".join(reasons) if reasons else "Connected"


def display_bfs_recommendations(
    graph: MovieGraph,
    start_title: str = "Inception",
    max_depth: int = 2,
) -> None:
    """
    Executes BFS recommendation traversal and pretty-prints the structured results.
    """
    print("=" * 76)
    print(" GOOGLE ANTIGRAVITY - GRAPH ENGINE RECOMMENDATION SYSTEM ")
    print("=" * 76)
    print(f"Graph Statistics: {len(graph.id_hashmap)} Movies (Vertices), "
          f"{sum(len(m.neighbors) for m in graph.id_hashmap.values()) // 2} Undirected Edges")
    print("-" * 76)

    # Run BFS
    result = graph.bfs_recommendations(start_title, max_depth=max_depth)
    target_node = result["target_node"]
    visited_by_level = result["visited_by_level"]
    edges = result["edges"]

    print(f"\n[TARGET SEED MOVIE] (Level 0)")
    print(f"  Title:     {target_node.title} ({target_node.year})")
    print(f"  ID:        {target_node.id}")
    print(f"  Director:  {target_node.director}")
    print(f"  Cast:      {', '.join(target_node.cast)}")
    print(f"  Genres:    {', '.join(target_node.genres)}")
    print(f"  Degree:    {len(target_node.neighbors)} direct connections\n")

    # Display Recommendations by Level
    for level in range(1, max_depth + 1):
        nodes_at_level = visited_by_level.get(level, [])
        level_label = (
            "Direct Recommendations (1st-Degree)"
            if level == 1
            else f"Extended Recommendations ({level}nd-Degree)"
        )
        print("-" * 76)
        print(f"[LEVEL {level}] {level_label} -> Count: {len(nodes_at_level)}")
        print("-" * 76)

        if not nodes_at_level:
            print("  (No movies found at this depth level)")
            continue

        for idx, movie in enumerate(nodes_at_level, start=1):
            print(f"  {idx}. {movie.title} ({movie.year}) [{movie.id}]")
            print(f"     Director: {movie.director} | Genres: {', '.join(movie.genres)}")
            
            # Find and display connecting edge reasons
            connecting_edges = [
                (u, v) for (u, v, d) in edges if d == level and (v == movie or u == movie)
            ]
            for u, v in connecting_edges:
                via_node = u if v == movie else v
                meta = graph.get_relationship_metadata(via_node, movie)
                reasons = format_edge_reasons(meta)
                print(f"     <- Connected via '{via_node.title}': {reasons}")
            print()

    # Traversed BFS Edges Summary
    print("=" * 76)
    print(f"TOTAL EXPLORATION NODES: {len(result['visited_nodes'])} | EDGES: {len(edges)}")
    print("=" * 76)


if __name__ == "__main__":
    sample_movies = get_sample_movies()
    movie_graph = build_movie_graph(sample_movies)

    # Test BFS from Inception
    display_bfs_recommendations(movie_graph, start_title="Inception", max_depth=2)
