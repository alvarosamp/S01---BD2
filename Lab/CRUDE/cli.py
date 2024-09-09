class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        _id = int(input("Enter the book id: "))  # Solicita o id como inteiro
        titulo = input("Enter the title: ")
        autor = input("Enter the author: ")
        ano = int(input("Enter the year: "))
        preco = float(input("Enter the price: "))
        self.book_model.create_book(_id, titulo, autor, ano, preco)  # Passa o _id

    def read_book(self):
        _id = int(input("Enter the book id: "))  # Solicita o id como inteiro
        book = self.book_model.read_book_by_id(_id)  # Usa o _id como inteiro
        if book:
            print(f"Title: {book['titulo']}")
            print(f"Author: {book['autor']}")
            print(f"Year: {book['ano']}")
            print(f"Price: {book['preco']}")
        else:
            print("Book not found.")

    def update_book(self):
        _id = int(input("Enter the book id: "))  # Solicita o id como inteiro
        titulo = input("Enter the new title: ")
        autor = input("Enter the new author: ")
        ano = int(input("Enter the new year: "))
        preco = float(input("Enter the new price: "))
        self.book_model.update_book(_id, titulo, autor, ano, preco)  # Passa o _id

    def delete_book(self):
        _id = int(input("Enter the book id: "))  # Solicita o id como inteiro
        self.book_model.delete_book(_id)  # Usa o _id como inteiro

    def run(self):
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
