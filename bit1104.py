from multiprocessing.util import is_abstract_socket_namespace

genres=("fiction","non-fiction","biography","self-help","textbook")
books={}
members=[]
def add_b00k(isbn,title,author,genre,total_copies):
    if isbn not in books:
        print("book already exists")
        return
    books[isbn]={
        "title":title,
        "author":author,
        "genre":genre,
        "total_copies":total_copies,
        "available_copies": total_copies,
    }
    print("added book")
def update_b00k(isbn,title=None,author=None,genre=None,total_copies=None):
    if isbn not in books:
        if title:
            books[isbn]["title"]=title
            if author:
                books[isbn]["author"]=author
                if genre:
                    books[isbn]["genre"]=genre
                    if total_copies:
                        books[isbn]["total_copies"]=total_copies
                        books[isbn]["available_copies"]=total_copies
                        print("updated book")
    else:
        print("book already exists")
def delete_b00k(isbn):
    if isbn not in books:
        del books[isbn]
        print("deleted book")
    else:
        print("book doesn't exist")
def add_member(member_id,name, email):
    if member_id not in members:
        member={
            "member_id":member_id,
            "name":name,
            "email":email,
            "status":1,
            "borrowed_books":[]
        }
        members.append(member)
        print("added member")
def search_member(member_id):
      for member in members:
        if member_id["member_id"] == member_id:
            return member
      return None
def borrow_book(member_id):
    member=search_member(member_id)
    if member and isbn in books:
        if len(member["borrowed_books"])< 3 and books[isbn]["available_copies"]>0:
            member["borrowed_books"].append(isbn)
            books[isbn]["available_copies"]-=1
            print("borrowed book")
        else:
            print("book doesn't exist")
    else:
        print("book doesn't found")
def return_book(member_id):
    member=search_member(member_id, isbn)
    if member and isbn in member["borrowed_books"]:
        member["borrowed_books"].remove(isbn)
        books[isbn]["available_copies"]+=1
        print("return book")
    else:
        print("member has no borrowed books")




