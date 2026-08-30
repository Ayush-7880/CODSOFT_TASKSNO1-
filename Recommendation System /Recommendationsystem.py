# ============================================================
# CODSOFT AI INTERNSHIP - TASK 4
# MOVIE RECOMMENDATION SYSTEM
# Content-Based Recommendation System
# ============================================================


# Movie dataset
movies = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 8.8
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 8.7
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "language": "English",
        "rating": 9.0
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "language": "English",
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "genre": "Comedy",
        "language": "Hindi",
        "rating": 8.4
    },
    {
        "title": "Dangal",
        "genre": "Drama",
        "language": "Hindi",
        "rating": 8.3
    },
    {
        "title": "Zindagi Na Milegi Dobara",
        "genre": "Drama",
        "language": "Hindi",
        "rating": 8.2
    },
    {
        "title": "Taare Zameen Par",
        "genre": "Drama",
        "language": "Hindi",
        "rating": 8.3
    },
    {
        "title": "The Hangover",
        "genre": "Comedy",
        "language": "English",
        "rating": 7.7
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama",
        "language": "English",
        "rating": 8.8
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 8.7
    },
    {
        "title": "PK",
        "genre": "Comedy",
        "language": "Hindi",
        "rating": 8.1
    },
    {
        "title": "War",
        "genre": "Action",
        "language": "Hindi",
        "rating": 6.5
    },
    {
        "title": "Pathaan",
        "genre": "Action",
        "language": "Hindi",
        "rating": 5.8
    },
    {
        "title": "Drishyam",
        "genre": "Thriller",
        "language": "Hindi",
        "rating": 8.2
    },
    {
        "title": "Shutter Island",
        "genre": "Thriller",
        "language": "English",
        "rating": 8.2
    },
    {
        "title": "Parasite",
        "genre": "Thriller",
        "language": "Korean",
        "rating": 8.5
    },
    {
        "title": "Spider-Man: No Way Home",
        "genre": "Action",
        "language": "English",
        "rating": 8.2
    },
    {
        "title": "The Lion King",
        "genre": "Animation",
        "language": "English",
        "rating": 8.5
    },
    {
        "title": "Coco",
        "genre": "Animation",
        "language": "English",
        "rating": 8.4
    }
]


def show_available_options():
    """Display available genres and languages."""

    genres = sorted(set(movie["genre"] for movie in movies))
    languages = sorted(set(movie["language"] for movie in movies))

    print("\nAvailable Genres:")
    print(", ".join(genres))

    print("\nAvailable Languages:")
    print(", ".join(languages))


def calculate_score(movie, preferred_genre, preferred_language,
                    minimum_rating):
    """
    Calculate recommendation score.

    Higher score means the movie matches the
    user's preferences better.
    """

    score = 0

    # Genre match has highest priority
    if movie["genre"].lower() == preferred_genre.lower():
        score += 50

    # Language match
    if movie["language"].lower() == preferred_language.lower():
        score += 30

    # Rating preference
    if movie["rating"] >= minimum_rating:
        score += 20

    # Add a small rating-based score
    score += movie["rating"]

    return score


def get_recommendations(preferred_genre, preferred_language,
                        minimum_rating, number_of_movies=5):

    recommendations = []

    for movie in movies:

        score = calculate_score(
            movie,
            preferred_genre,
            preferred_language,
            minimum_rating
        )

        # Only recommend movies matching genre
        if movie["genre"].lower() == preferred_genre.lower():

            recommendations.append(
                {
                    "title": movie["title"],
                    "genre": movie["genre"],
                    "language": movie["language"],
                    "rating": movie["rating"],
                    "score": score
                }
            )

    # Sort according to recommendation score
    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations[:number_of_movies]


def display_recommendations(recommendations):

    if not recommendations:
        print("\nNo matching movies found.")
        print("Try another genre.")
        return

    print("\n" + "=" * 65)
    print("              RECOMMENDED MOVIES")
    print("=" * 65)

    for index, movie in enumerate(recommendations, start=1):

        print(f"\n{index}. {movie['title']}")
        print(f"   Genre    : {movie['genre']}")
        print(f"   Language : {movie['language']}")
        print(f"   Rating   : {movie['rating']}/10")


def main():

    print("=" * 65)
    print("             MOVIE RECOMMENDATION SYSTEM")
    print("=" * 65)

    print("\nWelcome to the AI Movie Recommendation System!")

    show_available_options()

    # User preferences
    preferred_genre = input(
        "\nEnter your preferred genre: "
    ).strip()

    preferred_language = input(
        "Enter your preferred language: "
    ).strip()

    while True:
        try:
            minimum_rating = float(
                input("Enter minimum rating (0-10): ")
            )

            if 0 <= minimum_rating <= 10:
                break

            print("Please enter a rating between 0 and 10.")

        except ValueError:
            print("Please enter a valid number.")

    # Generate recommendations
    recommendations = get_recommendations(
        preferred_genre,
        preferred_language,
        minimum_rating
    )

    display_recommendations(recommendations)

    print("\n" + "=" * 65)
    print("Thank you for using the Recommendation System!")
    print("=" * 65)


if __name__ == "__main__":
    main()
