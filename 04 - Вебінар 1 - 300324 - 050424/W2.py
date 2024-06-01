x1 = int(input(""))#x1=0
y1 = int(input(""))#y1=0
x2 = int(input(""))#x2=1
y2 = int(input(""))#y2=3
x3 = int(input(""))#x3=0
y3 = int(input(""))#y3=5
Area = 0.5 * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))#2.5
print(Area)


sentence = input ("") #Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці...
sentence_symbol_space = ""
for symbol in sentence:
    if symbol.isalpha():
        sentence_symbol_space += symbol
    else:
        sentence_symbol_space += " " + symbol + " "
#print(sentence_symbol_space)
words = sentence_symbol_space.split()
#print(words)
num_word = 0
for word in words:
    if word.isalpha():
        num_word += 1
print(num_word)



start_string = input ("") #snake_case_text
end_string = start_string.replace ("_", " ").title().replace (" ", "")#SnakeCaseText
print(end_string)



start_string = input ("") #SnakeCaseText

end_string = "" #snake_case_text

i = 0
while i < len(start_string):
    letter = start_string[i]
    if i != 0:
        if letter.isupper():
            end_string += '_' + letter.lower()
        else:
            end_string += letter
    else:
        end_string += letter.lower()
    i += 1

print(end_string)



s1 = input("")#listen
s2 = input("")#silent

if len(s1) != len(s2):
    print("not anagram")
else:
    i=0
    not_anagram = False
    while i < len(s1):
        if s1[i] not in s2:
            not_anagram = True
        i += 1
    
    i=0
    not_anagram = False
    while i < len(s2):
        if s2[i] not in s1:
            not_anagram = True
        i += 1
    
    if not_anagram is True:
        print("not anagrams")
    else:
        print("anagrams")



s1 = input("")#listen
s2 = input("")#silent

is_anagrams = sorted(s1) == sorted(s2)

if is_anagrams:
    print("anagrams")
else:
    print("not anagrams")



n = int(input('n='))#20
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1