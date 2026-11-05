# Starting file for LAB 6-1
# Include your course number, student first and last name, and date in the comment header
# CS 31, josh lucero, 11-4-26

import statistics 

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 120:
                scores.append(score)
            else:
                print("Test score must be from 0 through 120. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total_scores = 0
    for thisscore in scores:
        total_scores += thisscore
    

    average_score = round(total_scores/len(scores))

    median = statistics.median(scores)

    # format and display the result
    print()
    print("Score total:       ", )
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", )
    print("Lowest Age: ", min(scores))
    print("Highest Age: ", max(scores))
    print("Median Score:      ", median)


def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

