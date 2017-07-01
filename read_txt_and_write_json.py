import json

def get_cook_book():
	cook_book = {}
	with open ('recipe.txt', 'r') as f:
		for line in f:
			dish = line.lower().strip()
			ing_list = []
			cook = []
			for s in range (int(f.readline().strip())):
				e = f.readline().strip().split(' | ')
				ing_list = list(map(str.strip, e))
				elements = {}
				elements['ingridient_name'] = ing_list[0]
				elements['quantity'] = int(ing_list[1])
				elements['measure'] = ing_list[2]
				cook.append (elements)
			cook_book[dish] = cook
			f.readline()
	return cook_book


def cook_book_to_json(): # создание recipe_j.json с записью в него словаря из get_cook_book()
	with open('recipe_j.json', 'w', encoding='utf-8') as f:
		f.write(json.dumps(get_cook_book(), ensure_ascii=False))

get_cook_book()
cook_book_to_json()
