# ordered, changable
my_list = ['code', 'eat', 'sleep']
# my_list[2] = 'no sleep'
# print(my_list)

# my_list.insert(2, 'girl')
# print(my_list)

# fav_list = ['a', 'b', 'c']
# my_list.extend(fav_list)
# print(my_list)

[print(x) for x in my_list]

num_list = [1, 2, 3, 4]
square_list = [a*a for a in num_list]
print(square_list)
print([b for b in square_list if b % 2 == 0])
