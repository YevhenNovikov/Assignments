from collections import Counter

def compute_difference(first: list, second: list) -> tuple:
    first_counter = Counter(first)
    second_counter = Counter(second)
    
    first_diff = list((first_counter - second_counter).elements())
    second_diff = list((second_counter - first_counter).elements())
    
    return (first_diff, second_diff)

def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])

test_compute_difference()

result = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
print("first-second:", result[0])
print("second-first:", result[1])



def sum_of_two(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]


user_input = input("Enter nums (n,m,...): ")
nums_input = [int(num) for num in user_input.split(',')]
target_input = int(input("Enter target: "))
result = sum_of_two(nums_input, target_input)
print(result)



def unique_elements(arr: list) -> list:
    unique_list = []
    for n in arr:
        if arr.count(n) == 1:
            unique_list.append(n)
    return unique_list

def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


user_input = input("Enter nums (n,m,...): ")
input_list = [int(n) for n in user_input.split(', ')]

result = unique_elements(input_list)
print(result)

test_unique_elements()



def odd_elements(arr: list) -> list:
    odd_elements_list = []
    for num in arr:
        if arr.count(num) % 2 != 0:
            if num not in odd_elements_list:
                odd_elements_list.append(num)
    return odd_elements_list

def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result2 == [1, 3, 4, 6]

user_input = input("Enter nums (n,m,...): ")
input_list = [int(n) for n in user_input.split(', ')]

result = odd_elements(input_list)
print(result)

test_odd_elements() 



def second_largest_element(arr: list) -> int:
    unique_list = []
    non_unique_list = []
    for n in arr:
        if n not in unique_list and n not in non_unique_list:
            unique_list.append(n)
        elif n in unique_list:
            unique_list.remove(n)
            non_unique_list.append(n)

    if len(unique_list) < 2:
        return None
    max_value = max(arr)
    arr.remove(max_value)
    if arr:
        second_max_value = max(arr)
        return second_max_value
    else:
        return None

def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None


user_input = input("Enter nums (n,m,...): ")
input_list = [int(n) for n in user_input.split(', ')]

result = second_largest_element(input_list)
print(result)

test_second_largest_element()



cities = [
('New York City', 8550405),
('Los Angeles', 3792621),
('Chicago', 2695598),
('Houston', 2100263),
('Philadelphia', 1526006),
('Phoenix', 1445632),
('San Antonio', 1327407),
('San Diego', 1307402),
('Dallas', 1197816),
('San Jose', 945942),
]

def get_population(city):
    return city[1]

sorted_cities = sorted(cities, key=get_population, reverse=True)
print(sorted_cities)

total_population = sum(get_population(city) for city in cities)
average_population = total_population / len(cities)

print("total population:", total_population)
print("average population:", average_population)