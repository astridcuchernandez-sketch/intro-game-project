def get_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return "player1"
    else:
        return "player2"

choices = ["rock", "paper", "scissors"]
p1_score = 0
p2_score = 0

print("=== 2 Player Rock Paper Scissors ===")

while True:
    print(f"\nScore -> Player 1: {p1_score} | Player 2: {p2_score}")
    
    p1 = input("Player 1, enter rock/paper/scissors (or 'quit'): ").lower()
    if p1 == "quit":
        break
    if p1 not in choices:
        print("Invalid choice by Player 1.")
        continue

    print("\n" * 20)  # hides Player 1 choice from Player 2

    p2 = input("Player 2, enter rock/paper/scissors (or 'quit'): ").lower()
    if p2 == "quit":
        break
    if p2 not in choices:
        print("Invalid choice by Player 2.")
        continue

    result = get_winner(p1, p2)

    if result == "tie":
        print("It's a tie!")
    elif result == "player1":
        print("Player 1 wins this round!")
        p1_score += 1
    else:
        print("Player 2 wins this round!")
        p2_score += 1

    print("-" * 40)

print("\nFinal Score:")
print(f"Player 1: {p1_score} | Player 2: {p2_score}")
print("Game over!")