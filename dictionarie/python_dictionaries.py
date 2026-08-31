# # Easy: Create a dictionary named car with keys: "brand", "model", and "year". Assign appropriate values to them and print the "brand" value.

# car = {
#     "brand" : "Toyota",
#     "year"  :  2020,
#     "model" : "Prius",
# }

# print(car["brand"])

# # Medium: Create a dictionary named student_scores with three students and their marks (e.g., {"Rahim": 80, "Karim": 75, "Tanvir": 92}). Write a for loop to print: "[Name] scored [marks] marks." for each student.

# student_scores = {
#     "Rahim": 80, 
#     "Karim": 75, 
#     "Tanvir": 92
# }

# for name, marks in student_scores.items():
#     print (f'{name} scored {marks}')


# # Hard: Write a function named get_highest_scorer(scores_dict) that takes a dictionary of student scores as a parameter. Use a for loop to find and return the name of the student with the highest score.

# # Test it with: scores = {"Alice": 78, "Bob": 95, "Charlie": 88}.

# def get_highest_scorer(scores_dict):

#     highest_score = -1
#     top_student = ""

#     for student, score in scores_dict.items():
#         if score > highest_score:
#             highest_score = score
#             top_student = student
#     return top_student 

# scores = {"Alice": 78, "Bob": 95, "Charlie": 88}
# print(get_highest_scorer(scores))


# Task 1: The Messy Analytics Aggregator
# Scenario: You are processing data from an web form where users accidentally typed numbers as strings, added extra spaces, or left entries blank.
# •	The Challenge: Write a function clean_and_aggregate(data) that takes a dictionary where keys are usernames and values are lists of scores.
# •	Requirements:
# 1.	Clean the data: Convert strings like " 95 " to integers, ignore empty strings "", and skip invalid data types (like nested lists or booleans).
# 2.	Calculate the average score for each user.
# 3.	Return a new dictionary with the user names as keys and their calculated average score (rounded to 1 decimal place) as values.
# •	Sample Input:
# python
# dirty_data = {
#     "Alice": ["85", " 90", ""],
#     "Bob": [72, "not_a_number", "88 "],
#     "Charlie": ["95", True, 100]  # Note: True is technically an int in Python, filter it out!
# }

dirty_data = {
    "Alice": ["85", " 90", ""],
    "Bob": [72, "not_a_number", "88 "],
    "Charlie": ["95", True, 100]  # Note: True is technically an int in Python, filter it out!
}


for name, numbers in dirty_data.items():
    if numbers == str:
        print (int(numbers)) and 
    

def data(datas):
    for name, numbers in datas.items():
        print({name}, {numbers})

print(data(dirty_data))


# Task 2: The E-Commerce Cart Optimizer
# Scenario: You are building a checkout system that needs to calculate totals while managing inventory levels and dynamic discounts.
# •	The Challenge: Write a function calculate_cart(cart, inventory, discounts) that processes a user's shopping cart.
# •	Requirements:
# 1.	Look up the prices from the inventory dictionary. Note that some prices are stored as strings (e.g., "$12.99"), so you must strip the $ and convert them to floats.
# 2.	Apply a percentage discount from the discounts dictionary if a matching coupon code is provided in the cart.
# 3.	If a cart item is missing from the inventory, skip it and add its name to a list of "unavailable_items" inside your final output.
# 4.	Return a dictionary containing the total price (rounded to 2 decimal places) and the list of unavailable items.
# •	Sample Input:
# python
# inventory = {"apple": 1.50, "banana": "0.75", "orange": "$2.00"}
# discounts = {"FRUIT20": 0.20} # 20% off
# user_cart = {"items": {"apple": 3, "mango": 1, "banana": 2}, "coupon": "FRUIT20"}



# Task 3: The Multi-Tier Leaderboard Ranked Sorter
# Scenario: You need to rank players for a competitive game tournament. A simple max() function won't work because ties happen often.
# •	The Challenge: Write a function rank_leaderboard(player_stats) that takes a nested dictionary of player metrics and returns a sorted list of player names.
# •	Requirements:
# 1.	Sort players primarily by their Score (highest to lowest).
# 2.	If their scores are tied, sort them by Games Played (lowest to highest, meaning fewer games to get the same score is better).
# 3.	If they are still tied, sort them alphabetically by their Username.
# 4.	Ensure your code safely handles scores or game counts that are mistakenly passed as strings.
# •	Sample Input:
# python
# tournament_data = {
#     "Player_A": {"score": "1500", "games": 20},
#     "Player_B": {"score": 1500, "games": "15"},
#     "Player_C": {"score": 1200, "games": 10},
#     "Player_D": {"score": 1500, "games": 15}
# }

