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
    def getInfo(name=name,bid=bid):
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
print(f"The winner of the action is {highest_name} with a bid of ${highest_bid}!!!")
