numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None
numbers.extend([1, 2, 3])

strings.extend(['hello', 'world'])

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)