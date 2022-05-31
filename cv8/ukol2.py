import random

def get_pc_choice() -> str:
    choose_dict = {
       1: "rock",
       2: "paper",
       3: "scissors",
       4: "lizard",
       5: "spock"
    }
    choice = random.randint(1,5)
    return choose_dict.get(choice)

def who_beats_who(rules : dict, pc : str, player : str) -> tuple:
    if player in rules.get(pc):
        # pc beats player
        return (True, False)
    if pc in rules.get(player):
        # player beats pc
        return (True, True)
    return (False, False)

def main_game():
    pc_score = 0
    player_score = 0

    rules = {
        "rock": ["lizard", "scissors"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

    while(pc_score < 3 and player_score < 3):
        print("\nPossible choices: 'rock','paper','scissors','lizard','spock'")
        print("Enter your choice: ")
        player_choice = input()
        pc_choice = get_pc_choice()

        results = who_beats_who(rules, pc_choice, player_choice)
        if results[0]:
            if results[1]:
                # player won
                print("Player: {0} | PC: {1} | PLAYER WINS".format(player_choice, pc_choice))
                player_score += 1
            else:
                # pc won
                print("Player: {0} | PC: {1} | PC WINS".format(player_choice, pc_choice))
                pc_score += 1
        else:
            print("Player: {0} | PC: {1} | ITS A DRAW".format(player_choice, pc_choice))

        print("\n SCORE |x| Player: {0} | PC: {1}".format(player_score, pc_score))

if __name__ == "__main__":
    main_game()