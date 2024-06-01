False == (not True)
(True and False) == (True and False)
(not True) and ("A" == "B")


one_grain_g = 0.065
one_grain_t = one_grain_g / 1000
num_cell = 64
total_grains = (2 ** num_cell)-1
total_weight = total_grains * one_grain_t
print("weight of grains on a chessboard: ", total_weight, " t")


positive_number = int(input())
factors = []
for factor in range(1, positive_number + 1):
    if positive_number % factor == 0:
        factors.append(factor)

print(f"If the number is {positive_number}, the factors are: {factors}".replace("[", "").replace("]", ""))


a = input("")
b = input("")
c = input("")
if a == b == c:
    print("An equilateral triangle is a triangle in which all three sides are equal")
elif a == b or a == c or b == c:
    print("A scalene triangle is a triangle that has three unequal sides")
else:
    print("An isosceles triangle is a triangle with (at least) two equal sides")




input_string = input() #aaaabchjjjjjswwwwwwwxyzaaaaaa

max_quantity = 0
max_letter = ""
current_quantity = 0
current_letter = ""

for letter in input_string:
    if letter == current_letter:
        current_quantity += 1
    else:
        if current_quantity > max_quantity:
            max_quantity = current_quantity
            max_letter = current_letter
        current_letter = letter
        current_quantity = 1

if current_quantity > max_quantity:
    max_quantity = current_quantity
    max_letter = current_letter

print(f'Longest consecutive symbol: {max_letter}')



year = int(input("Input a year:"))
month = int(input("Input a month [1-12]:"))
day = int(input("Input a day [1-31]:"))

if month in [1, 3, 5, 7, 8, 10, 12]:
    last_day_of_month = 31
elif month in [4, 6, 9, 11]:
    last_day_of_month = 30
else:
    leap_year = []
    for number in range(-4, 3000, 12):
         leap_year.append(number)
    if (leap_year):
        last_day_of_month = 29
    else:
        last_day_of_month = 28

if day < last_day_of_month:
    next_day = day + 1
    next_month = month
    next_year = year
if day == last_day_of_month:
    next_day = 1
    if month < 12:
        next_month = month + 1
        next_year = year
    if month == 12:
        next_month = 1
        next_year = year + 1

print(f"The next date is [{next_year}-{next_month}-{next_day}]")