# CSU Book Club reward calculator

books_bought = int(input("\nEnter how many books you purchased this month:\n"))

earned_points = 0

if books_bought == 2:
    earned_points = 5
elif books_bought == 4:
    earned_points = 15
elif books_bought == 6:
    earned_points = 30
elif books_bought >= 8:
    earned_points = 60

print(f"Reward points: {earned_points}")
