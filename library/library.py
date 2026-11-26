class book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.is_borrowed=False
  
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed= True
            print(self.title,"by", self.author,"has been borrowed")
        else:
             print(self.title,"by", self.author,"has already been borrowed")
 
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(self.title,"by", self.author,"has been returned")
        else:
             print(self.title,"by", self.author,"was not borrowed")

book1=book("count of monte cristo","alexander dumas")
book2=book("the picture of dorian gray","oscar wilde")
book3=book("no longer human","ozamu dazai")

book1.borrow()
book1.return_book()
book2.borrow()
book2.return_book()
book3.borrow()
book3.return_book()