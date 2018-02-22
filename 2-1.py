with open('Cook_book.txt', encoding='utf-8') as f:
    cook_book = dict()
    for line in f:
        dish = line.strip().lower()
        cook_book[dish] = list()
        ingridients_number = f.readline()
        for ing in range(int(ingridients_number)):
            ingridient_list = f.readline().strip().split(' | ')
            ingridient_name = ingridient_list[0].lower()
            quantity = int(ingridient_list[1])
            measure = ingridient_list[2]
            ingridient_list = {'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure}
            cook_book[dish].append(ingridient_list)
        f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
