"""Given a list of scores from participants in a university sports event, you must find the runner-up's score.
You will receive several scores. Store them in a list and find the score of the participant who finished in second place."""
print("Specify how many numbers you are going to enter, ")

n = int(input())
print("Now enter the numbers with spaces.")
scores = list(map(int, input().split()))

max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

print(f"The second place is {max(scores)}")
