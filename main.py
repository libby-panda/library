books_db = [
    {
        "name": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": "1997",
        "genre": "Fantasy"
    },
    {
        "name": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": "2008",
        "genre": "Dystopia"
    },
    {
        "name": "Divergent",
        "author": "Veronica Roth",
        "year": "2012",
        "genre": "Dystopia"
    },
    {
        "name": "The Hobbit, or There and Back Again",
        "author": "J.R.R. Tolkien",
        "year": "2002",
        "genre": "Fantasy"
    },
    {
        "name": "Hoot",
        "author": "Carl Hiaasen",
        "year": "2006",
        "genre": "Fiction"
    },
    {
        "name": "Restart",
        "author": "Gordon Korman",
        "year": "2017",
        "genre": "Realistic Fiction"
    },
    {
        "name": "The Miscalculations of Lightning Girl",
        "author": "Stacy McAnulty",
        "year": "2018",
        "genre": "Realistic Fiction"
    },
    {
        "name": "Insignificant Events in the Life of a Cactus",
        "author": "Dusti Bowling",
        "year": "2017",
        "genre": "Realistic Fiction"
    },
    {
        "name": "The Remarkable Journey of Coyote Sunrise",
        "author": "Dan Gemeinhart",
        "year": "2019",
        "genre": "Realistic Fiction"
    },
    {
        "name": "Alone",
        "author": "Megan E. Freeman",
        "year": "2021",
        "genre": "Poetry"
    },
    {
        "name": "The Canyon's Edge",
        "author": "Dusti Bowling",
        "year": "2020",
        "genre": "Poetry"
    },
    {
        "name": "Something Like Home",
        "author": "Andrea Beatriz Arango",
        "year": "2023",
        "genre": "Realistic Fiction"
    },
    {
        "name": "Out of My Mind",
        "author": "Sharon M. Draper",
        "year": "2010",
        "genre": "Realistic Fiction"
    },
    {
        "name": "Wonder",
        "author": "R.J. Palacio",
        "year": "2012",
        "genre": "Fiction"
    },
    {
        "name": "Holes",
        "author": "Louis Sachar",
        "year": "1998",
        "genre": "Fiction"
    },
    {
        "name": "Charlotte’s Web",
        "author": "E.B. White",
        "year": "1952",
        "genre": "Fiction"
    },
    {
        "name": "Matilda",
        "author": "Roald Dahl",
        "year": "1988",
        "genre": "Fiction"
    },
    {
        "name": "The Lion, the Witch and the Wardrobe",
        "author": "C.S. Lewis",
        "year": "1950",
        "genre": "Fantasy"
    },
    {
        "name": "The Lightning Thief",
        "author": "Rick Riordan",
        "year": "2005",
        "genre": "Fantasy"
    },
    {
        "name": "The Maze Runner",
        "author": "James Dashner",
        "year": "2009",
        "genre": "Dystopia"
    },
    {
        "name": "City of Bones",
        "author": "Cassandra Clare",
        "year": "2007",
        "genre": "Fantasy"
    },
    {
        "name": "Red Queen",
        "author": "Victoria Aveyard",
        "year": "2015",
        "genre": "Fantasy"
    },
]


def show_menu():
    print("""
               
               
               Library
    1. Show all books
    2. Show books by category
    3. Search books
    999. Exit""")
    user_choice = input("Please choose from these options:")
    return user_choice


def show_all_books(books):

    for book in books:
        print(book)
    print(f"""
    Total:
    {len(books)} books""")


def show_books_by_category(books):
    categories = []
    i = 0
    for book in books:
        genre = book["genre"]
        if genre not in categories:
            i += 1
            categories.append(genre)
            print(f"{i}. {genre}")
    genre_chosen_id = input("Choose a genre.")
    genre_chosen = categories[int(genre_chosen_id) - 1]
    for book in books:
        if book["genre"] == genre_chosen:
            print(book)


def search_books():
    searched_book = input(print("Search books here: "))
    if searched_book != books_db:
        print("Try again.")


def start_library(books):
    while True:
        user_choice = show_menu()
        if user_choice == "1":
            show_all_books(books)
        elif user_choice == "2":
            show_books_by_category(books)
        elif user_choice == "3":
            search_books
        elif user_choice == "999":
            print("It was nice knowing you. Bye!")
            return
        else:
            print("Please try again; that was not a valid choice.")


start_library(books_db)
