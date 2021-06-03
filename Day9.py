# Day 9 Project: Silent auction

namesAndBids = {}

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\
'''
done = False

while not done:
    print("Welcome to the super secret silent auction program")
    print("Are you ready to bid?!")
    name = input("What is your name?:\t")
    bid = int(input("What is your bid?:\t$"))

    def getInfo(name=name, bid=bid):
        namesAndBids[name] = bid
    getInfo()
    others = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if others == 'no':
        done = True
    else:
        print("\033[H\033[J")
highest_bid = max(namesAndBids.values())
highest_name = max(namesAndBids, key=namesAndBids.get)

print("\033[H\033[J")
print(
    f"The winner of the action is {highest_name} with a bid of ${highest_bid}!!!")


# Day 9.1 Excercise: navigating dictionaries
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectation"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Day 9.2 Excercise: Nesting a dicitionaries in lists. 

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
  travel_log.append({"country": country, "visits": visits, "cities": cities})




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
