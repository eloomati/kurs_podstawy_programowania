numbers = [1, 2, 3, 4, 5]
print(numbers)
get_num = numbers.pop() #domyslnie zdejmuj ostatni elmente
print(numbers)
print(get_num)

get_second_element = numbers.pop(1)
print(f"{get_second_element} to drugi element listy")