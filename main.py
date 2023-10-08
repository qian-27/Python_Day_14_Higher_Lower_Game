from art import logo, vs
from game_data import data
from random import choice

print(logo)
score = 0
game_should_continue = True

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from{account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a" #return True if it is a.
    else:
        return guess == "b"

while game_should_continue:
    # Choose a random account
    account_a = choice(data)
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)
    print(f"Compare A: {format_data(account_a)}. ")
    print(vs)
    print(f"Compare B: {format_data(account_b)}. ")

    # Ask user for a guess.
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.\n")
    else:
        print(f"Sorry, that's wrong! Final score: {score}.\n")
        game_should_continue = False