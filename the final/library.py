from asyncio.windows_events import NULL
import AVL_treee as a
import asofin as o
from datetime import date
class Library:
    def __init__(self,name,id_no,book,publisher,book_id,issuedate,BF):
        self.name=name
        self.id_no=id_no
        self.book=book
        self.publisher=publisher
        self.book_id=book_id
        self.issuedate=issuedate
        self.BF=BF
        self.cost=(BF*5)
    def adminclass(self,book,book_id):
        self.book=book
        self.book_id=book_id
    
    def receipt(self):
        print()
        print("----------ISSUE RECEIPT----------")        
        print("Name:          ",self.name)
        print("Id_no:         ",self.id_no)
        print("Book:          ",self.book)
        print("Publisher:     ",self.publisher)
        print("Book ID:       ",self.book_id)
        print("Issued on:     ",self.issuedate)
        print("Borrowed for : ",self.BF)
        print("COST:          ",self.cost)
        print("xxxxxxxxxx-HAPPY READING-xxxxxxxxxx")
        print("----------ISSUE RECEIPT----------")
        print()
def Search(l,b):
    if l in b:
        return 1
    else:
        return 0
def search(l,p,T):
    k=(T.search(root,p))
    if l==1:
        if k is  None:
            return 0
        else:
            return 1
    elif l==4:
        if k is None:
            print("No book found")
        else:
            print("Book found")
    else:
        if k is not None:
            return 0
        else:
            return 1
def hassh(k):
    m=0
    for i in k:
        m+=ord(i)
    return m
D=1
while D>0:
    print("-----LIBRARY MANAGEMENT SYSTEM-----")
    print("1.Administrator")
    print("2.Customer")
    print("3.EXIT")
    V=int(input("Enter the choice: "))
    T=a.AVL_Tree()
    root=None
    book=[]
    bookcode=[]
    admin=[["praveen","johar"],["naveen","thyohar"]]
    if V==1 :
        I=1
        H=0
        while I>0:
            k=input("INPUT ADMIN_ID: ")
            l=(input("ENTER PASSWORD: "))
            p=[k,l]
            if p in admin:
                j=1
                break
            else:
                print("RETRY")
                continue
        while j>0:
            print("-----ADMINISTRATOR-----")
            print("1.New entry")
            print("2.BOOK CODE")
            print("3.BOOK LIST")
            print("4.SEARCH BOOK")
            print("5.EXIT")
            l=int(input("Enter your choice: "))
            print("-----ADMINISTRATOR-----")

            if l==1:
                u=input(("Enter the name of the book: "))
                e=hassh(u)
                p=search(l,e,T)
                if p==0:
                    book.append(u)
                    bookcode.append(e)
                    root=a.treee(T,root,e)
                else:
                    print("Enter a new book")
            elif l==2:
                T.preOrder_B(root)
                print()
            elif l==3:
                for i in book:
                    print(i,end=' ')
                print()
            elif l==4:
                p=input("Enter the name of the book: ")
                L=hassh(p)
                search(l,L,T)
            elif l==5:
                break
        C=bookcode
    elif V==2:
        print(C)

        for i in book:
            print(i,end=' ')
        print()
        B=o.AVLTree()
        root2=None
        p=[]
        while l>0:
            
            print("STUDENT")
            print("1.ISSUE")
            print("2.RETURN BOOK")
            print("3.DUE LIST")
            print("4.EXIT")
            m=int(input("CHOOSE THE OPERATION: "))
            if m==1:
                print("----------ISSUE----------")
                A=input("Enter your name: ")
                c=input("Enter the name of the book: ")
                d=input("Enter the Publisher name: ")
                g=int(input("Days borrowed for : "))
                print("----------ISSUE----------")
                today=date.today()
                w=hassh(c)
                Q=hassh(A)
                I=Search(w,C)
                if I==0:
                    print()
                    print("---------------")
                    print("Book unavailable")
                    print("---------------")
                    print()
                else:
                    root2=o.tree(B,root2,A)
                    N=Library(A,Q,c,d,w,today,g)
                    N.receipt()
            elif m==2:
                print()
                print("-----RETURN-----")
                q=input("Enter the name: ")
                Z=input("Enter the name of the book: ")
                Z=hassh(q)
                B.delete_node(root2,q)
                print()
                print("------RETURN SUCCESFULL-----")
                print()
            elif m==3:
                print("People Yet to Return")
                print()
                B.preOrder(root2)
                print()
                print()
            elif m==4:
                break
    elif V==3:
        break