def custom_append(input_list, value):
    """
    like input_list.append(value), should add the value to the end of the list
    and return nothing
    """
    length = 0
    for item in input_list:
        length += 1

    list_value = [value]
    input_list[length:] = list_value

fruit = ['a','b','c']
value = 'd'
custom_append(fruit,value)
print fruit
