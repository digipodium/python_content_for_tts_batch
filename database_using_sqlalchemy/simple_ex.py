from sqlalchemy.orm import sessionmaker
from orm_file import Book
from sqlalchemy import create_engine

# connect to database
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()


print("Welcome to Bookdb")
while True:
    print("***MENU***")
    print("1. View Books")
    print("2. Add Book")
    print('3.exit')
    op = input('select an option : ')

    if op == '1':
        results = sess.query(Book).all()
        for book in results:
            print("ID : ",book.id)
            print("TITLE :",book.title)
            print("AUTHOR :",book.author)
            print()
    elif op == '2':
        print('Add new book info')
        title = input("TITLE ->")
        author = input("AUTHOR ->")
        price = input("PRICE ->")
        yr = input("YEAR ->")

        if title and author and price and yr:
            yr = int(yr)
            price = float(price)

            obj = Book(title=title,author=author,price=price,year=yr)
            sess.add(obj)
            sess.commit()
            print("saved book info")

    elif op == '3': 
        import sys
        sys.exit(0)
    else:
        print("wrong option, select correct options")