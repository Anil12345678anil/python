my_dict = {'key1': 'value1', 'key2': 'value2'}

# Using square brackets
value1 = my_dict['key1']

# Using get() method
value2 = my_dict.get('key2')
#----------------------------------------------------------------
print(value1, value2)  # Output: value1 value2
my_dict = {'key1': 'value1', 'key2': 'value2'}

for key in my_dict:
    print(key)  # Output: key1 key2
#----------------------------------------------------------------


my_dict = {'key1': 'value1', 'key2': 'value2'}

for value in my_dict.values():
    print(value)  # Output: value1 value2

#----------------------------------------------------------------

my_dict = {'key1': 'value1', 'key2': 'value2'}

for key, value in my_dict.items():
    print(key, value)  # Output: key1 value1, key2 value2

#----------------------------------------------------------------

my_dict = {'key1': 'value1', 'key2': 'value2'}

if 'key1' in my_dict:
    print("Key 'key1' exists")  #my_dict = {'key1': 'value1', 'key2': 'value2'}

print(len(my_dict))  # Output: 2
my_dict = {'a': 1, 'b': 2, 'c': 3}
#----------------------------------------------------------------

# Using get() to retrieve values
value_a = my_dict.get('a')
value_d = my_dict.get('d')  # Key 'd' doesn't exist

print(value_a)  # Output: 1
print(value_d)  # Output: None

# Specifying a default value
value_e = my_dict.get('e', 'Key not found')

print(value_e)  # Output: Key not found
#Output: Key 'key1' exists

#----------------------------------------------------------------

# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Prompting the user to enter a key-value pair
user_key = input("Enter a key: ")
user_value = input("Enter the corresponding value: ")

# Checking if both key and value are present in the dictionary
if user_key in my_dict and str(my_dict[user_key]) == user_value:
    print("Item is in dictionary")
else:
    print("No")

#----------------------------------------------------------------

# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Prompting the user to enter a key-value pair
user_key = input("Enter a key: ")
user_value = input("Enter the corresponding value: ")

# Checking if both key and value are present in the dictionary
if my_dict.get(user_key) == int(user_value):
    print("Item is in dictionary")
else:
    print("No")
#----------------------------------------------------------------



# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Prompting the user to enter a key-value pair
user_key = input("Enter a key: ")
user_value = input("Enter the corresponding value: ")

# Checking if both key and value are present in the dictionary
try:
    if my_dict[user_key] == int(user_value):
        print("Item is in dictionary")
    else:
        print("No")
except KeyError:
    print("No")
