class Library:
    books_name = []
    books_index = []

    def store(self, name, index) -> None:
        self.name = name
        self.index = index

    def keeper(self):
        if self.name not in self.books_name and self.index not in self.books_index:
            self.books_name.append(self.name)
            self.books_index.append(self.index)
        else:
            print('Sorry The name of the book is taken or Serial of the book is taken.')
    def search(self, name):
        try:
            self.serial = self.books_name.index(name)
            print(
                f"The index of the book {self.name} is {self.books_index[self.serial]}"
            )
        except ValueError:
            print("Book not Found")


books = Library()
while True:
    name = str(input("Book name: "))
    if name == "Stop":
        print(f"Number of books stored is {len(books.books_name)}")
        break
    elif name == "Search":
        books.search(str(input("Book name for search: ")))
    else:
        index = int(input("Serial Number: "))
        books.store(name, index)
        books.keeper()
