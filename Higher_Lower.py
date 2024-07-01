from art import logo
from art import vs
from game_data import data
import random


def celebrity():
        data_length = len(data)
        celeb1 = data[random.randint(0, data_length - 1)]
        celeb2= data[random.randint(0, data_length - 1)]
        while celeb1 == celeb2:
            celeb2 = data[random.randint(0, data_length - 1)]
        return celeb1,celeb2



def start(celeb1,celeb2,):
    print(logo)
    print("Compare A:" ,celeb1['name'], "a" ,celeb1['description'], "from" ,celeb1['country'])
    print(vs)
    print("Compare B:" ,celeb2['name'], "a" ,celeb2['description'], "from" ,celeb2['country'])
    answer= input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer 




def compare(celeb1,celeb2):
    if celeb1["follower_count"] > celeb2["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    return winner



def the_final(answer,winner,total): 
    if answer == winner:
        total +=1
        print("You're Right! Current Score:", total)
    else:
        print("Sorry, that's wrong. Final score:", total)
    return total
    

total=0
while True:
    celeb1, celeb2 = celebrity()
    answer = start(celeb1, celeb2)
    winner = compare(celeb1, celeb2)
    total = the_final(answer,winner,total)

    


    continue_game = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if continue_game != 'yes':
        break









