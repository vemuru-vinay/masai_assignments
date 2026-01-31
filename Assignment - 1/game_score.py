player = input("Enter a player name : ")
games_played = int(input("Enter the number of games played : "))
total_score = int(input("Enter the total score achieved by player : "))

avg = total_score // games_played

print(f"Player : {player}")
print(f"Games Played : {games_played}")
print(f"Total Score : {total_score}")
print(f"Average Score : {avg}")