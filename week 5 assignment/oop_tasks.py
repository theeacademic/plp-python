from abc import ABC, abstractmethod


class Device:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self._powered_on = False

    def power_on(self):
        self._powered_on = True

    def power_off(self):
        self._powered_on = False

    def is_on(self):
        return self._powered_on

    def device_info(self):
        return f"{self.brand} {self.model} with {self.storage_gb}GB"


class Smartphone(Device):
    def __init__(self, brand, model, storage_gb, camera_mp):
        super().__init__(brand, model, storage_gb)
        self.camera_mp = camera_mp

    def take_photo(self):
        if not self.is_on():
            return "Cannot take photo. Device is off."
        return f"Photo taken with {self.camera_mp}MP camera."


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"


class Mover(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Mover):
    def move(self):
        return "Driving"


class Plane(Mover):
    def move(self):
        return "Flying"


class Boat(Mover):
    def move(self):
        return "Sailing"


def demo():
    phone = Smartphone("Acme", "X1", 128, 48)
    phone.power_on()
    book = Book("Python 101", "Ada Lovelace", 300)

    movers = [Car(), Plane(), Boat()]

    print(phone.device_info())
    print(phone.take_photo())
    print(book.description())
    for mover in movers:
        print(mover.move())


if __name__ == "__main__":
    demo()


