numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
a = 0
symbols = len(numbers)


for i in numbers:
    if i == None:
        numbers.remove(numbers[a])
        element = sum(numbers)/symbols
        numbers.insert(a,element)
        break
    a += 1


print("Измененный список:", numbers)