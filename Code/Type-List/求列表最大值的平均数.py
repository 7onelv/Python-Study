list_1 = eval(input())
list_max = [max(i) for i in list_1]
print(f'{ sum(list_max) / len(list_max) :.2f}')
