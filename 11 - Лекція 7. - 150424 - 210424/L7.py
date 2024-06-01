import random

capitals = {
    'Ukraine': 'Kyiv', 
    'France': 'Paris', 
    'Germany': 'Berlin',
    'Italy': 'Rome', 
    'USA': 'Washington', 
    'Canada': 'Ottawa',
    'Switzerland': 'Bern', 
    'Austria': 'Vienna',
    'Belgium': 'Brussels',  
    'Sweden': 'Stockholm',
    'Norway': 'Oslo', 
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki', 
    'Poland': 'Warsaw',
    'Romania': 'Bucharest', 
    'Bulgaria': 'Sofia', 
    'Greece': 'Athens'
}

def play_game():
    score = 0
    lives = 3
    
    while lives > 0:
        keys_in_capitals = capitals.keys()
        list_of_countries = list(keys_in_capitals)
        country = random.choice(list_of_countries)
        capital = capitals[country]
        print(f"Guess the capital of {country}:")
        
        user_input = input().strip().capitalize()
        hint_index = -1
        
        while user_input != capital:
            lives -= 1
            print("Incorrect. You have", lives, "attempts left.")
            hint_index += 1
            hint = capital[:hint_index + 1]
            print("Hint:", hint)
            if lives == 0:
                break
            user_input = input().strip().capitalize()
        
        if lives == 0:
            print("Your life is over. Game over. Your final score:", score)
            break
        
        score += 1
        print("You're right!")
    
    if lives > 0:
        print(f"Thanks for playing! Your final score is: {score}")

play_game()



def majority_element(nums: list) -> int:
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return max(counts, key=counts.get)

def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result2 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result2 == 2

input_string = input()
nums = [int(num) for num in input_string.split(', ')]

result = majority_element(nums)
print(result)

test_majority_element()



def get_subjects_not_passed_by_all_students(student_exams):
    subjects_not_passed = set()
    subject_scores = {}

    for student_exam in student_exams:
        name, score, subject = student_exam
        if subject not in subject_scores:
            subject_scores[subject] = []
        subject_scores[subject].append(score)

    for subject, scores in subject_scores.items():
        if all(score < 60 for score in scores):
            subjects_not_passed.add(subject)

    return subjects_not_passed


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}


    failed_subjects = get_subjects_not_passed_by_all_students(exams)
    print("The subjects that were not passed by all students:", ", ".join(failed_subjects))

test_get_subjects_not_passed_by_all_students()