# ==============================================================================
# Task 4: Cricket Team Score Evaluation
# File: session-4/task4_cricket_score.py
# Purpose: Evaluate cricket score using if, elif, else:
#          >= 200: 'High Score!'
#          150 - 199: 'Good Score'
#          100 - 149: 'Average'
#          else: 'Needs Improvement'
# ==============================================================================

# 1. Ask user for their favorite cricket team's score
score = int(input("Enter your favorite cricket team's score: "))

# 2. Check score category
if score >= 200:
    print("High Score!")
elif score >= 150:
    print("Good Score")
elif score >= 100:
    print("Average")
else:
    print("Needs Improvement")

