import random

SCORE = 0

# List of questions and answers
quiz = list()

# Read the quiz from input.txt file 
it = 0 # The number of line
fp = open("input.txt")

while True:
    # Create the subdict name
    subdict_name = "q" + str(it+1)
    subdict_name = dict()
    
    # Read the question line
    line_q = fp.readline()

    # Exit while loop if no line is detected
    if not line_q:
        break

    subdict_name['q'] = line_q

    line_a = fp.readline()

    # Read the answer line
    if not line_a:
        break

    subdict_name['a'] = line_a
    it = it + 1

    # Add the dict with question and answer to the list of question and answers
    quiz.append(subdict_name)

fp.close()

# Mix the question-answers from the list 
random.shuffle(quiz)

for d in quiz:
    print(d['q'])
    answer = input("Enter your answer: ")
    answer = answer.lower()

    if answer == d['a'].lower().rstrip('\n'):
        print("Correct")
        SCORE +=10
    else:
        print("Wrong")
        print("The answer is ", d['a'])

print("Your final score is ", SCORE)