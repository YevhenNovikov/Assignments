def get_input():
    while True:
        user_input = input("Enter an integer: ")
        return (user_input)


def convert_to_int():
    while True:
        try:
            input_value = int(get_input())
            print("Integer entered:", input_value)
            return
        except ValueError:
            print("Error! Not an integer. Try again.")

convert_to_int()



def get_input():
    string = input("enter a string: ")
    n = input("enter an integer: ")
    return string, n

def print_character_at_index(str_input, index):
    try:
        index = int(index)
        symbol = str_input[index]
        print("Symbol with index", index, "this is", symbol)
    except IndexError:
        print("Error: Index is out of range. Please enter a valid index.")
        string, n = get_input()
        print_character_at_index(string, n)
    except ValueError:
        print("Error: Please enter an integer.")
        string, n = get_input()
        print_character_at_index(string, n)

string, n = get_input()
print_character_at_index(string, n)



balance = 1000

def transaction(amount, type):
    def deposit(amount):
        global balance
        balance += amount
        print("New balance after deposit:", balance)

    def withdrawal(amount):
        global balance
        balance -= amount
        print("New balance after amount:", balance)

    if type == "deposit":
        deposit(amount)
    elif type == "withdrawal":
        withdrawal(amount)
    else:
        print("Invalid transaction type")

get_amount = float(input("Enter amount: "))
get_type = input("Enter transaction type (deposit or withdrawal): ")
transaction(get_amount, get_type)



import random

def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
print(result)



import random

def dice_roll():
    return random.randint(1, 6)

results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(1000):
    result_roll = dice_roll()
    results[result_roll] += 1

for number, number_of_times in results.items():
    print(f"Number {number} was rolled {number_of_times} times.")





import random

def receive_input():
    num_regions = int(input("Enter the number of regions: "))
    ratings = []
    for region in range(1, num_regions+1):
        rating = int(input(f"Enter a rating for 1st candidate in {region} region: "))
        ratings.append(rating)
    return ratings


def simulate_region_election(rating):
    candidates = [1, 2]
    votes = random.choices(candidates, weights=[rating, 100 - rating], k=10000)
    candidate1_votes = votes.count(1)
    candidate2_votes = votes.count(2)
    return candidate1_votes, candidate2_votes

def simulate_election(ratings):
    results = []
    for reg, rating in enumerate(ratings):
        candidate1_votes, candidate2_votes = simulate_region_election(rating)
        results.append((reg+1, candidate1_votes, candidate2_votes))
    return results

def calculate_result(results):
    total_candidate1_votes = 0
    total_candidate2_votes = 0
    for result in results:
        region, candidate1_votes, candidate2_votes = result
        total_candidate1_votes += candidate1_votes
        total_candidate2_votes += candidate2_votes

    total_votes = total_candidate1_votes + total_candidate2_votes
    winner_procent = max(total_candidate1_votes, total_candidate2_votes) / total_votes * 100
    if total_candidate1_votes > total_candidate2_votes:
        winner = "1st candidate"
    else:
        winner = "2nd candidate"
    return winner, total_candidate1_votes, total_candidate2_votes, winner_procent

def announce_result(result, election_result):
    winner, total_candidate1_votes, total_candidate2_votes, winner_procent = result
    for region, candidate1_votes, candidate2_votes in election_result:
        print(f"Region {region}: {candidate1_votes} votes for 1st candidate, {candidate2_votes} votes for 2nd candidate")
    print(f"Result: {winner} won with {total_candidate2_votes} votes and {winner_procent:.1f}% of all votes")


input_data = receive_input()
election_result = simulate_election(input_data)
result = calculate_result(election_result)
announce_result(result, election_result)