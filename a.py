import argparse
import random
import json



class Actor:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def add_scores(self):
        self.scores +=1


with open("questions.json","r") as file:
    data = json.load(file)
    easy_questions = data["easy_questions"]
    medium_questions = data["medium_questions"]
    hard_questions = data["hard_questions"]

    
def choose_the_level():
        print("easy_questions to easy level press 1")
        print("medium_questions for medium level press 2")
        print("hard_questions for hard level press 3")
        the_selected_level=int(input("Please enter your choice"))
        if the_selected_level==1:
            return easy_questions
        elif the_selected_level ==2 :
            return medium_questions
        elif the_selected_level == 3:
            return hard_questions
        else: 
            print("Please enter a number from the options only")
            return choose_the_level()


def questions_for_players(players, questions):
    current_player_index = 0
    while questions:
        current_player = players[current_player_index]
        print(f"\n{current_player.name}, it's your turn!")
        question = random.choice(questions)

        print(question['question'])
        for num, answer in question['answers'].items():
            print(f"{num}. {answer}")

        player_answer_num = input("Your answer: ")
        player_answer = question['answers'].get(player_answer_num)

        if player_answer == question['correct_answer']:
            print("Correct!")
            current_player.add_scores()
        else:
            print("Wrong!")

        questions.remove(question)

        current_player_index = (current_player_index + 1) % len(players)

    print("\nGame over!")
    for player in players:
        print(f"{player.name}: {player.scores} points")




    max_score = max(player.scores for player in players)
    winners = [player.name for player in players if player.scores == max_score]

    if len(winners) > 1:
        print(f"It's a tie between: {', '.join(winners)}")

    else:
        print(f"The winner is {winners[0]}!") 

def get_players():
    players = []
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        players.append(Actor(name, 0))
    return players





players = get_players()

questions = choose_the_level()


questions_for_players(players, questions)
