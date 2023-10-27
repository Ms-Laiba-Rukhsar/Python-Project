from prettytable import PrettyTable
import datetime

def main_table(main_list):
    my_table = PrettyTable()
    my_table.field_names = ["id_of_book", "name_of_author", "title_of_book", "price_of_book",
                            "available_status_of_book"]
    for x in main_list:
        to_make_row = [x["id_of_book"], x["name_of_author"], x["title_of_book"],
                       x["price_of_book"], x["available_status_of_book"]]
        my_table.add_row(to_make_row)
    print(my_table)


def add():
    book_id = 1
    author = input('entre authors name:')
    title = input('entre title of book:')
    price = int(input('entre price of book:'))
    available_status = 'yes'
    book_to_add = {'id_of_book': book_id, 'name_of_author': author, 'title_of_book': title, 'price_of_book': price,
                   'available_status_of_book': available_status}
    return book_to_add


def delete(deleting):
    if len(deleting) == 0:
        print('library is empty')
    else:
        main_table(deleting)
        book_to_delete_id = int(input('entre id of book you wanna delete: '))
        for x in range(len(deleting)):
            if deleting[x]['id_of_book'] == book_to_delete_id:
                deleting.pop(x)
                print(f"book having id {book_to_delete_id} has been deleted from library")
                break
        else:
            print('here is no book with this id in our library')


def update(updating):
    if len(updating) == 0:
        print('library is empty')
    else:
        main_table(updating)
        book_to_update = int(input('entre id of book which do you wanna update'))
        for y in updating:
            if y["id_of_book"] == book_to_update:
                print('1:title_of_book')
                print('2:price_of_book')
                feature_to_change = int(input('entre number corresponding to feature do you wanna change:'))
                if feature_to_change == 1:
                    new_title = input('entre new title of book')
                    print(f"title of book having id [{book_to_update}] has been changed from [{y['title_of_book']}],")
                    y["title_of_book"] = new_title
                    my_table = PrettyTable()
                    my_table.field_names = ["id_of_book", "name_of_author", "title_of_book", "price_of_book"
                                            ,"available_status_of_book"]
                    to_make_row = y["id_of_book"], y["name_of_author"],y["title_of_book"], y["price_of_book"], \
                                  y["available_status_of_book"]
                    my_table.add_row(to_make_row)
                    print(f" to [{new_title}]")
                    print(my_table)
                elif feature_to_change == 2:
                    new_price = int(input('entre your new price'))
                    print(f"price  of book having id [{book_to_update}] has been changed from [{y['price_of_book']}")
                    y["price_of_book"] = new_price
                    my_table = PrettyTable()
                    my_table.field_names = ["id_of_book", "name_of_author", "title_of_book", "price_of_book","available_status_of_book"]
                    to_make_row = y["id_of_book"], y["name_of_author"],y["title_of_book"], y["price_of_book"],y["available_status_of_book"]
                    my_table.add_row(to_make_row)
                    print(f"to [{new_price}]")
                    print(my_table)
                    break
                else:
                    print('entre valid number')
                break
        else:
            print('this book does not exist in our library')


def search(searching):
    if len(searching) == 0:
        print('library is empty')
    else:
        main_table(searching)
        print('1:title_of_book')
        print('2:author_of_book')
        criteria=int(input('select criteria of searching by entring number corresponding to that criteria'))
        if criteria == 1:
            books=[]
            book_to_search_title=input('entre title of book do you wanna search')
            for x in range(len(searching)):
                books.append(searching[x]['title_of_book'])
            if book_to_search_title in books:
                book=0
                my_table=PrettyTable()
                for x in searching:
                    if x['title_of_book'] == book_to_search_title:
                        my_table.field_names = ["id_of_book", "name_of_author", "title_of_book", "price_of_book",
                                                "available_status_of_book"]
                        to_make_row = [x["id_of_book"], x["name_of_author"],
                                       x["title_of_book"],x["price_of_book"],
                                       x["available_status_of_book"]]
                        my_table.add_row(to_make_row)
                        book+=1
                print(f" {book} book/books in library having title ''{book_to_search_title}''")
                print(my_table)
            else:
                print(f"here is no book in library having title ''{book_to_search_title}''")
        elif criteria == 2:
            books=[]
            book_to_search_author = (input('entre author name whose book do you wanna search'))
            for x in range(len(searching)):
                books.append(searching[x]['name_of_author'])
            if book_to_search_author in books:
                book=0
                my_table=PrettyTable()
                for x in searching:
                    if x['name_of_author'] == book_to_search_author:
                        my_table.field_names = ["id_of_book", "name_of_author", "title_of_book", "price_of_book",
                                                "available_status_of_book"]
                        to_make_row = [x["id_of_book"], x["name_of_author"],
                                       x["title_of_book"], x["price_of_book"],
                                       x["available_status_of_book"]]
                        my_table.add_row(to_make_row)
                        book+=1
                print(f"{book} book/books in library of author ''{book_to_search_author}''")
                print(my_table)
            else:
                print(f"here is no book in library written by ''{book_to_search_author}''")


def display_all(displaying):
    if len(displaying) == 0:
        print('library is empty')
    else:
        main_table(displaying)


def borrow(borrowing, borrowing_history):
    if len(borrowing)==0:
        print('library is empty')
    else:
        main_table(borrowing)
        book_to_borrow = int(input('entre id of book that you wanna borrow'))
        today_s_date=datetime.datetime.now()
        year=today_s_date.year
        for x in borrowing:
            if x['id_of_book'] == book_to_borrow:
                month = int(input('entre month of borrowing book'))
                days = int(input('entre date of borrowing book'))
                date_of_issuing = datetime.date(year, month, days)
                if x['available_status_of_book'] == 'NO':
                    print(f"available status of book having id {x['id_of_book']}="
                        f"{x['available_status_of_book']}")
                    print('your demanded book is not available')
                else:
                    name_of_student=input('entre your name')
                    borrowing_history_dict={"id_of_book":book_to_borrow,"name_of_student":name_of_student,"date_of_issuing":date_of_issuing}
                    borrowing_history.append(borrowing_history_dict)
                    x['available_status_of_book'] = 'NO'
                    print(f"book having id {x['id_of_book']} has been issued to you on "
                          f"{date_of_issuing}")
                break
        else:
            print('demanded id is not enrolled in our library')


def return_book(returning,borrow_history):
    if len(returning) == 0:
        print('library is empty')
    else:
        if len(borrow_history)==0:
            print('no book has been borrowed yet')
        else:
            book_to_return = int(input('entre id of book you are returning'))
            date_to_return_1 = datetime.datetime.now()
            a=date_to_return_1.year
            b=date_to_return_1.month
            c=date_to_return_1.day
            date_to_return=datetime.date(a,b,c)
            for y in borrow_history:
                if y['id_of_book'] == book_to_return:
                    name_of_student = input('entre your name')
                    if y['name_of_student'] == name_of_student:
                        owing_book_days = date_to_return-y['date_of_issuing']
                        just_days = owing_book_days.days
                        borrow_history.remove(y)
                        if just_days <= 15:
                            for x in returning:
                                if x['id_of_book'] == book_to_return:
                                    x['available_status_of_book'] = 'yes'
                            print(f"you own book for {just_days} days and has been returned without any fine")
                        else:
                            fine=(just_days-15)*10
                            print(f"you have to pay fine of {fine} "
                                  f"RS because you own this book for "
                                  f"{just_days}days")
                            user_give_amount=int(input('amount you are giving'))
                            if user_give_amount>fine:
                                to_return=user_give_amount-fine
                                print(f"return_amount={to_return} RS and book has been returned")
                            else:
                                print('book has been returned')
                            for x in returning:
                                if x['id_of_book'] == book_to_return:
                                    x['available_status_of_book']='yes'
                    else:
                        print(f"this book was not given to you but to "f"{y['name_of_student']}")
                    break
            else:
                print('this book was not borrowed by our library')


def display_borrowed(displaying_borrowing):
    lst_0=[]
    if len(displaying_borrowing) == 0:
        print('library is empty')
    else:
        my_table = PrettyTable()
        my_table.field_names = ["books_borrowed_id_s","name_of_author","title_of_book","price_of_book","available_status_of_book"]
        for x in displaying_borrowing:
            if x['available_status_of_book'] == 'NO':
                lst_0.append(x['available_status_of_book'])
                my_table.add_row([x["id_of_book"],x["name_of_author"],x["title_of_book"],
                                 x["price_of_book"],x["available_status_of_book"]])
        if len(lst_0)==0:
            print('no book has borrowed yet')
        else:
            print(my_table)


def main_menu():
    books_of_library = []
    borrow_history = []
    while True:
        print('1:add a book in a library')
        print('2:delete a book in a library')
        print('3:update information of book like title or price')
        print('4:search a book by author nam or title')
        print('5:borrow a book from library')
        print('6: return a book to library')
        print('7:display all books')
        print('8:display books borrowed by students')
        print('9:Exit')
        operation = int(input('select operation do you wanna perform by entering number corresponding to that '
                              'operation: '))
        if operation == 1:
            books_of_library.append(add())
            if len(books_of_library) > 1:
                books_of_library[-1]["id_of_book"] = (books_of_library[-2]["id_of_book"]) + 1
        elif operation == 2:
            delete(books_of_library)
        elif operation == 3:
            update(books_of_library)
        elif operation == 4:
            search(books_of_library)
        elif operation == 5:
            borrow(books_of_library, borrow_history)
        elif operation == 6:
            return_book(books_of_library,borrow_history)
        elif operation == 7:
            display_all(books_of_library)
        elif operation == 8:
            display_borrowed(books_of_library)
        elif operation == 9:
            exit()
        else:
            print('select valid operation')

main_menu()