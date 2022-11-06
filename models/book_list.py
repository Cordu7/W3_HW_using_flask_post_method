from models.book_class import Book
import datetime
book1=Book("Das Doppelte Lottchen", "Erich Kästner", "Fiction", datetime.date(2022, 5, 17))
book2=Book("Where the Wild Things Are", "Maurice Sendak", "Picture Book", datetime.date(2022, 4, 20))
book3= Book("Roll of Thunder, Hear my Cry", "Mildred D. Taylor", "Fiction", datetime.date(2020, 11, 5))
book4= Book("Nimona", "ND Stevenson", "Graphic Novel", datetime.date(2022, 11, 1)) 

book_list= [book1, book2, book3, book4]

def add_new_book(book):
    book_list.append(book)

def delete_book(book_title):
    book_to_delete= None
    for book in book_list:
        if book.title==book_title:
            book_to_delete= book
    book_list.remove(book_to_delete)