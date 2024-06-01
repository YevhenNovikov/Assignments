print(10 > 5) 
print(42 != "42")
print(3 < 4)

print('"Have a nice day!"')
word = '"Have a nice day!"'
print(word)

numbers = '123456789'
print(numbers[7::-2])

word = input("level")
word == word[::-1]

current_age = input('')
name_var = input('')
birthday_str = 'My name is {} and I am {} years old'
print(birthday_str.format(name_var, current_age))

current_age = input('')
name_var = input('')
birthday_str = 'My name is {name} and I am {age} years old'
print(birthday_str.format(name=name_var, age=current_age))

age_1 = input('')
new_name = input('')
birthday_str = f'My name is {new_name} and I am {age_1} years old'
print(birthday_str)

string_1 = "Animals  "
print(string_1.lower())

string_2 = "  Badger"
print(string_2.capitalize())

string_3 = "   HoneyPot   "
print(string_3.lstrip())

string_3 = "   HoneyPot   "
print(string_3.rstrip())

string_3 = "   HoneyPot   "
print(string_3.strip())

string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
print(string_1.startswith('Be'))
print(string_2.startswith('Be'))
print(string_3.startswith('Be'))
print(string_4.startswith('Be'))

string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
formatted_string_2 = string_2.title()
formatted_string_3 = string_3.capitalize()
formatted_string_4 = string_4.swapcase()
print(formatted_string_2.startswith('Be'))
print(formatted_string_3.startswith('Be'))
print(formatted_string_4.startswith('Be'))

'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
#!enil terces a s tI
"It's a secret line"
a_secret_message = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
print(a_secret_message.replace('X', '').replace('x', '')[::-1])