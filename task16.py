my_weight = int(input("Введите вес: "))
i = 1

while i <= 15:
    my_weight += 1
    result = my_weight + my_weight * 0.165
    print(f"В {i} году на луне ваш вес будет составлять: {round(result, 2)} ")
    i += 1
