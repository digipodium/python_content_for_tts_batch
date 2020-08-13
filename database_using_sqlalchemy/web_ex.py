from sqlalchemy.orm import sessionmaker
from orm_file import Book
from sqlalchemy import create_engine

import streamlit as st

# connect to database
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

choice = st.sidebar.selectbox("select option",['Add book','View books'])

if choice == 'Add book':
    st.header("Add book details")
    title = st.text_input('enter book title',)
    author = st.text_input('enter author name')
    year = st.number_input('year of publishing',min_value=1800,max_value=2020,value=2000)
    price = st.number_input('book price',min_value=0.0,max_value=999999.0, step=.5)
    submit = st.button("save details")
    if submit and title and author:
        obj = Book(title=title, author=author, price=price, year = year)
        sess.add(obj)
        sess.commit()
        st.success("book data added")
    else:
        st.warning("please fill valid details")
elif choice =='View books':
    st.header("Displaying all books")
    results = sess.query(Book).all()
    for book in results:
        st.subheader(book.title)
        st.text(book.author)
        st.text(book.year)
        st.empty()

