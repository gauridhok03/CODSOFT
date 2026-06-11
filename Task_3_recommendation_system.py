# =====================================================
#        MEDIA RECOMMENDATION SYSTEM
#     Movies & Books Recommendation Engine
#     Content-Based Filtering Approach
# =====================================================

movies = {
    "action": [
        ("John Wick", 8.5),
        ("The Dark Knight", 9.0),
        ("Mission Impossible", 8.2),
        ("Mad Max: Fury Road", 8.1),
        ("Gladiator", 8.5),
        ("Top Gun: Maverick", 8.3)
    ],

    "sci-fi": [
        ("Interstellar", 8.9),
        ("Inception", 8.8),
        ("The Matrix", 8.7),
        ("Avatar", 7.9),
        ("The Martian", 8.0),
        ("Dune", 8.2)
    ],

    "comedy": [
        ("3 Idiots", 8.4),
        ("Free Guy", 7.8),
        ("Jumanji", 7.5),
        ("The Hangover", 7.7),
        ("Deadpool", 8.0),
        ("Central Intelligence", 6.9)
    ],

    "romance": [
        ("Titanic", 7.9),
        ("The Notebook", 7.8),
        ("La La Land", 8.0),
        ("Me Before You", 7.4),
        ("A Walk to Remember", 7.3),
        ("The Fault in Our Stars", 7.7)
    ],

    "horror": [
        ("The Conjuring", 7.5),
        ("Insidious", 6.8),
        ("It", 7.3),
        ("Annabelle", 5.9),
        ("The Nun", 5.3),
        ("Smile", 6.5)
    ]
}

books = {
    "fiction": [
        ("The Alchemist", 4.7),
        ("To Kill a Mockingbird", 4.8),
        ("The Great Gatsby", 4.5),
        ("The Kite Runner", 4.8),
        ("The Book Thief", 4.7),
        ("1984", 4.8)
    ],

    "fantasy": [
        ("Harry Potter", 4.9),
        ("The Hobbit", 4.8),
        ("The Lord of the Rings", 4.9),
        ("Percy Jackson", 4.7),
        ("The Chronicles of Narnia", 4.6),
        ("Eragon", 4.5)
    ],

    "self-help": [
        ("Atomic Habits", 4.8),
        ("The Power of Now", 4.6),
        ("Think and Grow Rich", 4.7),
        ("Deep Work", 4.7),
        ("The 7 Habits of Highly Effective People", 4.8),
        ("Ikigai", 4.6)
    ],

    "finance": [
        ("Rich Dad Poor Dad", 4.7),
        ("The Psychology of Money", 4.8),
        ("The Intelligent Investor", 4.7),
        ("Money Master the Game", 4.5),
        ("Think and Grow Rich", 4.7),
        ("Your Money or Your Life", 4.4)
    ],

    "mystery": [
        ("Sherlock Holmes", 4.8),
        ("The Da Vinci Code", 4.6),
        ("Gone Girl", 4.5),
        ("Murder on the Orient Express", 4.7),
        ("The Silent Patient", 4.6),
        ("And Then There Were None", 4.8)
    ]
}


def show_movies():
    print("\nAvailable Movie Genres:")
    for genre in movies:
        print("•", genre.title())

    genre = input("\nEnter movie genre: ").lower()

    if genre in movies:
        print("\n" + "=" * 50)
        print("        MOVIE RECOMMENDATIONS")
        print("=" * 50)

        for i, (movie, rating) in enumerate(movies[genre], start=1):
            print(f"{i}. {movie:<30} ⭐ {rating}/10")

    else:
        print("❌ Genre not found.")


def show_books():
    print("\nAvailable Book Genres:")
    for genre in books:
        print("•", genre.title())

    genre = input("\nEnter book genre: ").lower()

    if genre in books:
        print("\n" + "=" * 50)
        print("         BOOK RECOMMENDATIONS")
        print("=" * 50)

        for i, (book, rating) in enumerate(books[genre], start=1):
            print(f"{i}. {book:<35} ⭐ {rating}/5")

    else:
        print("❌ Genre not found.")


def main():

    print("=" * 55)
    print("        MEDIA RECOMMENDATION SYSTEM")
    print("      Movies & Books Recommendation")
    print("=" * 55)

    name = input("\nEnter your name: ").title()

    while True:

        print("\n" + "=" * 55)
        print(f"Welcome, {name}")
        print("=" * 55)

        print("\n1. Movie Recommendations")
        print("2. Book Recommendations")
        print("3. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            show_movies()

        elif choice == "2":
            show_books()


        elif choice == "3":
            print(f"\nThank you for using the system, {name}!")
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()