import os #импортируем библиотеку

path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path, encoding ='utf-8') as cook_file: # открываем файл и добавляем кодировку для чтения
    cookbook = {} # создаем пустой словарь поваренной книги
    for line in cook_file:
        dish = line.strip() # выбираем из словаря названия блюд
        ingredients_count = int(cook_file.readline().strip()) # выбираем ингредиенты и количество их для блюда
        dish_dict = [] # создаем пустой список для словарей с блюдами
        for i in range(ingredients_count):
            # выбираем из файла ингредиенты по разделению "|"
            ingredients_name, quantity, measure = cook_file.readline().strip().split('|')
            # добавляем в список словари с ингредиентами
            dish_dict.append({'ingredients_name':ingredients_name, 'quantity':quantity, 'measure':measure})
        cookbook[dish] = dish_dict # добавляем в поваренную книгу ингредиенты
        cook_file.readline() # пропускаем пустую строку
print('Задача №1: Получили словарь\n================================')
print(cookbook)

# Создаем функцию для получения списка покупок исходя из заказанных блюд и количества персон
def get_shop_list_by_dishes(dishes, person_count):
    purchases_dict = {} # создаем пустой словарь для списка покупок
    for dish in dishes:
        for ingredient in cookbook[dish]: # выбираем ингредиенты из поваренной книги для блюд
            # Добавляем ингредиенты увеличивая их на количество персон
            ingredient_list = dict([(ingredient['ingredients_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure':ingredient['measure']})])
            # Проверяем заказанное блюдо на повтор, если блюдо уже есть то увеличиваем количество ингредиентов
            # Иначе добавляем ингредиенты в список покупок
            if purchases_dict.get(ingredient['ingredients_name']) == 'None':
                _merger = (int(purchases_dict[ingredient['ingredients_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                purchases_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                purchases_dict.update(ingredient_list)
    return purchases_dict

print('\nЗадача №2: Получить словарь с названием ингредиентов и его количества для блюда.\n================================')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



# Получаем список файлов их путь 'sorted'
folder_path = 'sorted'
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Создаем словарь для хранения данных
file_contents = {}


# читаем содержимое файлов и считаем количество строк
for file_name in file_names:
    with open(os.path.join(folder_path, file_name), 'r', encoding ='utf-8') as f:
        lines = f.readlines()
        file_contents[file_name] = {
            'num_lines': len(lines),
            'content': lines
        }

# сортируем словарь по количеству строк в файле
sorted_contents = sorted(file_contents.items(), key=lambda x: x[1]['num_lines'])

# Записываем отсортированное в файл
with open(os.path.join(folder_path,'result.txt'), 'w', encoding ='utf-8') as result_file:
    for file_name, content in sorted_contents:
        result_file.write(f'{file_name}\n{content["num_lines"]}\n')
        result_file.writelines(content['content'])

print('\nЗадача №3: Необходимо объединить их в один по следующим правилам \n1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них. \n2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем. \n================================')
print('Готово! Результат записан в файл result.txt в папке sorted')


