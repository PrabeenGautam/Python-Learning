# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# #TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# for key in student_scores:
#   score = student_scores[key]
#   if score >= 91 and score <= 100:
#     student_grades[key] = 'OutStanding'
#   elif score >= 81 and score <= 90:
#     student_grades[key] = 'Exceeds Expectations'
#   elif score >= 71 and score <= 80:
#     student_grades[key] = 'Acceptable'
#   else:
#     student_grades[key] = 'Fail'

# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country, visits, cities):
#   travel_log.append({"country": country, "visits": visits, "cities": cities})

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel)

from art import logo
print(logo)
bid = {}
bool = 'true'

while bool == 'true':
  name = input('\nWhat is your name?: ')
  bid_input = int(input('What is your bid?: '))

  bid[name] = bid_input
  bid_bool = input('\nIs there any bid left?: ').lower()
  if bid_bool == 'yes':
    bool = 'true'
  else:
    bool = 'false'

max_bid = max(bid)
print('\n')
print(f'{max_bid} has higher bid with bid value {bid[max_bid]}')