import random

print("""
    Snake, Water and Gun game
    choose any one from (snake, water & gun)
    Total round : 7
""")

_choice = ["snake", "water", "gun"]
_user_winner = [
    [0, 1], [1, 2], [2, 0]
]
_user_loss = [
    [0, 2], [1, 0], [2, 1]
]
_draw = [
    [0, 0], [1, 1], [2, 2]
]
user_won_round = 0
NeoMind_won_round = 0    #NeoMind is AI

user_name = input("Enter the user's first name : ")
for i in range(1, 8):
    user_choice = input("Enter your choice : ")
    user_choice = user_choice.lower()
    try:
        user_idx = _choice.index(user_choice)
    except (ValueError, NameError) as e:
        print(e)
        continue

    NeoMind_idx = random.randint(0, 2)
    NeoMind_choice = _choice[NeoMind_idx]
    user_ai_list = [user_idx, NeoMind_idx]

    print(f"""
        {user_name} choice : {user_choice}
        AI choice : {NeoMind_choice}
    """)

    for win in _user_winner:
        if win == user_ai_list:
            print(f"{user_name} Won the round & NeoMind Lose.\n{user_choice} beats the {NeoMind_choice}")
            user_won_round += 1
            break

    for lose in _user_loss:
        if lose == user_ai_list:
            print(f"NeoMind Won the round & {user_name} Lose.\n{NeoMind_choice} beats the {user_choice}")
            NeoMind_won_round += 1
            break

    for draw in _draw:
        if draw == user_ai_list:
            print(f"Game Draw")
            break

if user_won_round > NeoMind_won_round:
    print(f"""
        Winner of the Match : {user_name}
        Loser of the Match : NeoMind
""")
elif NeoMind_won_round > user_won_round:
    print(f"""
        The winner of the Match : NeoMind
        Loser of the Match : {user_name}
""")
elif NeoMind_won_round == user_won_round:
    print("Match Draw!")
