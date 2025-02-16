if __name__ == "__main__":
    class Car:
        """
        Базовый класс для представления автомобилей.

        Атрибуты:
            _model (str): Модель автомобиля.
            _engine_power (float): Мощность двигателя (в лошадиных силах).
            _price (int): Стоимость автомобиля (в USD).
            _weight (float): Вес автомобиля (в килограммах).
        """

        def __init__(self):
            """Инициализирует атрибуты автомобиля."""
            self._model = None
            self._engine_power = None
            self._price = None
            self._weight = None

        @property
        def engine_power(self) -> float:
            """
            Возвращает мощность двигателя автомобиля.

            :return: Мощность двигателя (в лошадиных силах).
            """
            return self._engine_power

        @engine_power.setter
        def engine_power(self, value: float):
            """
            Устанавливает мощность двигателя автомобиля.

            :param value: Мощность двигателя (в лошадиных силах).
            :raises ValueError: Если мощность отрицательная или не является типом float.
            """
            if not isinstance(value, float):
                print('Мощность двигателя должна быть типа float')
            if value < 0:
                print('Мощность двигателя должна быть положительным числом')
            self._engine_power = value

        @property
        def price(self) -> int:
            """
            Возвращает стоимость автомобиля.

            :return: Стоимость автомобиля (в USD).
            """
            return self._price

        @price.setter
        def price(self, value: int):
            """
            Устанавливает стоимость автомобиля.

            :param value: Стоимость автомобиля (в USD).
            :raises ValueError: Если стоимость отрицательная или не является типом int.
            """
            if not isinstance(value, int):
                print('Стоимость должна быть типа int')
            if value < 0:
                print('Стоимость должна быть положительным числом')
            self._price = value

        @property
        def model(self) -> str:
            """
            Возвращает модель автомобиля.

            :return: Модель автомобиля.
            """
            return self._model

        @model.setter
        def model(self, simbols: str):
            """
            Устанавливает модель автомобиля.

            :param simbols: Модель автомобиля.
            :raises ValueError: Если модель не является типом str.
            """
            if not isinstance(simbols, str):
                print('Модель должна быть типа str')
            self._model = simbols

        @property
        def weight(self) -> float:
            """
            Возвращает вес автомобиля.

            :return: Вес автомобиля (в килограммах).
            """
            return self._weight

        @weight.setter
        def weight(self, value: float):
            """
            Устанавливает вес автомобиля.

            :param value: Вес автомобиля (в килограммах).
            :raises ValueError: Если вес отрицательный или не является типом float.
            """
            if not isinstance(value, float):
                print('Вес должен быть типа float')
            if value < 0:
                print('Вес должен быть положительным числом')
            self._weight = value

        def calculate_power_to_weight_ratio(self) -> float:
            """
            Рассчитывает удельную мощность (отношение мощности двигателя к весу).

            :return: Удельная мощность (л.с./кг).
            :raises ValueError: Если вес автомобиля не задан или равен нулю.
            """
            if self._weight is None or self._weight == 0:
                raise ValueError("Вес автомобиля не задан или равен нулю.")
            return self._engine_power / self._weight

        def calculate_fuel_consumption(self, distance: float) -> float:
            """
            Рассчитывает расход топлива на заданное расстояние.


        :param distance: Расстояние (в километрах).
        :return: Расход топлива (в литрах).
        :raises ValueError: Если расстояние отрицательное.
        """

            if distance < 0:
                raise ValueError("Расстояние должно быть положительным числом.")
        # Упрощенная формула: расход = (мощность / коэффициент) * (расстояние / 100)
        # Для легковых автомобилей коэффициент = 20
            return (self._engine_power / 20) * (distance / 100)


    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчика.

        :return: Строка, содержащая информацию об автомобиле.
        """
        return f'{self.__class__.__name__}(model={self._model!r}, engine_power={self._engine_power!r}, ' \
               f'price={self._price!r}, weight={self._weight!r})'


    def __str__(self):
        """
        Возвращает строковое представление объекта для пользователя.

        :return: Строка, содержащая модель и цену автомобиля.
        """
        return f"Автомобиль: '{self._model}', Цена: '{self._price}', Вес: '{self._weight}'"


class PassengerCar(Car):
    """
    Дочерний класс для представления легковых автомобилей.

    Атрибуты:
        _passenger_capacity (int): Вместимость пассажиров.
    """

    def __init__(self):
        """Инициализирует атрибуты легкового автомобиля."""
        super().__init__()
        self._passenger_capacity = None

    @property
    def passenger_capacity(self) -> int:
        """
        Возвращает вместимость пассажиров.

        :return: Вместимость пассажиров.
        """
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value: int):
        """
        Устанавливает вместимость пассажиров.

        :param value: Вместимость пассажиров.
        :raises ValueError: Если вместимость отрицательная или не является типом int.
        """
        if not isinstance(value, int):
            print('Вместимость пассажиров должна быть типа int')
        if value < 0:
            print('Вместимость пассажиров должна быть положительным числом')
        self._passenger_capacity = value

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчика.

        :return: Строка, содержащая информацию о легковом автомобиле.
        """
        return f'{self.__class__.__name__}(model={self._model!r}, engine_power={self._engine_power!r}, ' \
               f'price={self._price!r}, weight={self._weight!r}, ' \
               f'passenger_capacity={self._passenger_capacity!r})'

    def __str__(self):
        """
        Возвращает строковое представление объекта для пользователя.

        :return: Строка, содержащая модель, вместимость и цену легкового автомобиля.
        """
        return f"Легковой автомобиль: '{self._model}', Вместимость: '{self._passenger_capacity}', Цена: '{self._price}'"


class Truck(Car):
    """
    Дочерний класс для представления грузовых автомобилей.

    Атрибуты:
        _cargo_capacity (float): Грузоподъемность (в тоннах).
    """

    def __init__(self):
        """Инициализирует атрибуты грузового автомобиля."""
        super().__init__()
        self._cargo_capacity = None

    @property
    def cargo_capacity(self) -> float:
        """
        Возвращает грузоподъемность автомобиля.

        :return: Грузоподъемность (в тоннах).
        """
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, value: float):
        """
        Устанавливает грузоподъемность автомобиля.


        :param value: Грузоподъемность (в тоннах).
        :raises ValueError: Если грузоподъемность отрицательная или не является типом float.
        """
        if not isinstance(value, float):
            print('Грузоподъемность должна быть типа float')
        if value < 0:
            print('Грузоподъемность должна быть положительным числом')
        self._cargo_capacity = value

    def calculate_fuel_consumption(self, distance: float) -> float:
        """
        Перегруженный метод для расчета расхода топлива с учетом груза.
        У грузовых автомобилей расход топлива выше из-за груза.

        :param distance: Расстояние (в километрах).
        :return: Расход топлива (в литрах).
        :raises ValueError: Если расстояние отрицательное.
        """
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом.")
        # Упрощенная формула: расход = (мощность / коэффициент) * (расстояние / 100) * (1 + грузоподъемность / 10)
        # Для грузовых автомобилей коэффициент = 10
        return (self._engine_power / 10) * (distance / 100) * (1 + self._cargo_capacity / 10)

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчика.

        :return: Строка, содержащая информацию о грузовом автомобиле.
        """
        return f'{self.__class__.__name__}(model={self._model!r}, engine_power={self._engine_power!r}, ' \
               f'price={self._price!r}, weight={self._weight!r}, ' \
               f'cargo_capacity={self._cargo_capacity!r})'

    def __str__(self):
        """
        Возвращает строковое представление объекта для пользователя.

        :return: Строка, содержащая модель, грузоподъемность и цену грузового автомобиля.
        """
        return f"Грузовой автомобиль: '{self._model}', Грузоподъемность: '{self._cargo_capacity}', Цена: '{self._price}'"


# Пример использования
passenger_car = PassengerCar()
passenger_car.model = "Toyota Camry"
passenger_car.engine_power = 203.0
passenger_car.price = 30000
passenger_car.weight = 1500.0
passenger_car.passenger_capacity = 5

print(passenger_car)
print(repr(passenger_car))
print("Удельная мощность:", passenger_car.calculate_power_to_weight_ratio())
print("Расход топлива на 100 км:", passenger_car.calculate_fuel_consumption(100))

truck = Truck()
truck.model = "Volvo FH16"
truck.engine_power = 750.0
truck.price = 150000
truck.weight = 8000.0
truck.cargo_capacity = 20.0

print(truck)
print(repr(truck))
print("Удельная мощность:", truck.calculate_power_to_weight_ratio())
print("Расход топлива на 100 км (с учетом груза):", truck.calculate_fuel_consumption(100))
