# TODO решите задачу

import json

def task(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_sum = sum(item["score"] * item["weight"] for item in data)
    return round(total_sum, 3)


# Example usage
file_path = 'C:\\Users\\user\\Desktop\\files\\input.json'
result = task(file_path)
print(task((file_path)))
