from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        ...  # TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)) or not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if (capacity_volume < 0) or (occupied_volume > capacity_volume) or (occupied_volume < 0):
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    bottle = Glass(-200,100)
    cap = Glass(200,-50)

    # TODO попробовать инициализировать не корректные объекты

    print(bottle.capacity_volume)
    print(cap.occupied_volume)