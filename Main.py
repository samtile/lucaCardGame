import random
import statistics

gameScores = [0] * 100000
lowestScore = 100
highestScore = 0


def cards(game_number):
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
            10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
    random.shuffle(deck)
    score = 0
    count = 1
    search_card = 1
    note = ""
    for x in deck:
        if count == 52:
            score += x
            gameScores[game_number] = score
            global lowestScore
            if score < lowestScore:
                lowestScore = score
            global highestScore
            if score > highestScore:
                highestScore = score
                print("\nNew high score!")
                print(note)
                print("Last card scored is ", str(x),", FINAL SCORE IS ", str(score), "\n")
        elif x == search_card:
            score += x
            note = note + "Card value " + str(x) + " found at card number " + str(count) + ", Total score is now " + str(score) + "\n"
            if search_card == 13:
                search_card = 1
            else:
                search_card += 1
        count += 1


n = len(gameScores)
for y in range(n):
    cards(y)

print("Total score: ", str(sum(gameScores)))
print("Number of games played: ", str(len(gameScores)))
print("Lowest score: ", str(lowestScore))
print("Highest score: ", str(highestScore))
print("Range: ", str(highestScore - lowestScore))
print("Mean score: ", sum(gameScores) / len(gameScores))
print("Median score: ", statistics.median(gameScores))
print("Mode score: ", statistics.mode(gameScores))
