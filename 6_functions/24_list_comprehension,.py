#newlist = [expression for item in iterable if condition ==True]

L = [1,2,3,4,10,123,22]
new_list = [num for num in L if num % 3==0]
print(new_list)