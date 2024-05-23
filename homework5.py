immutable_var = int(input( )), int(input()), int(input()), int(input())
print(immutable_var)
#immutable_var [0] = 90
#print(immutable_var)
#Кортеж нельзя изменить, потому что кортеж не поддерживает обращение по элементам.
mustable_list = ([52, 31], 1337)
print(mustable_list)
mustable_list[0][0] = 213
print(mustable_list)