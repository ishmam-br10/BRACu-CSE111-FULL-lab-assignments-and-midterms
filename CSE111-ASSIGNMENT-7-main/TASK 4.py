#TASK 4
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+        "Price: "+str(self.__price)
#write your code here
class Book(Product):
    def __init__(self, id, name, price, isbn, publisher):
        super().__init__(id, name, price)
        self.isbn = isbn
        self.publisher = publisher

    def printDetail(self):
        return f"{super().get_id_title_price()} ISBN: {self.isbn} Publisher: {self.publisher}"

class CD(Product):
    def __init__(self, id, name, price, band, duration, genre):
        super().__init__(id, name, price)
        self.band = band
        self.duration =duration
        self.genre = genre
    def printDetail(self):
        return f"{super().get_id_title_price()} Band: {self.band} Duration: {self.duration} Genre: {self.duration}"
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())
