class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError ("количество страниц должно быть типа int")
        if pages <=0:
            raise ValueError("количество страниц должно быть больше 0")
        self.__pages = pages

    def __str__(self)-> str:
        return f"Книга {self._name}. Автор {self._author}. Количество страниц{self.__pages}"

    def __repr__(self) -> str:
        return f"PaperBook(name={self._name!r}, author={self._author!r}, pages={self.__pages})"

class AudioBook(Book):
    def __init__(self, name: str , author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, int):
            raise TypeError ("количество страниц должно быть типа float")
        if duration <=0:
            raise ValueError("количество страниц должно быть больше 0")
        self.__duration = duration

    def __str__(self)-> str:
        return f"Книга {self._name}. Автор {self._author}. Количество страниц{self.__duration}"

    def __repr__(self) -> str:
        return f"AudioBook(name={self._name!r}, author={self._author!r}, duration={self.__duration!r})"