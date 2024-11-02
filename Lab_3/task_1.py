# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def search_function(item_list, find_item):
    for i in item_list:
        if find_item in item_list:
            index_item = item_list.index(find_item)
            return index_item
            break
        else:
            return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = search_function(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
