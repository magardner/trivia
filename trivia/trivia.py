# Quiz game
import sys, getopt, csv
from random import randint

questions = []


def ask(questionslist) -> bool:
    #Picks a random quesiton
    #Returns true if the question was answered correctly
    number_of_questions = len(questions)
    question_number = randint(0, number_of_questions-1)
    answer = input(f'{questions[question_number]["question"]}\n')
    if answer == questions[question_number]["answer"]:
        print(f'Well done, you are correct!\n')
        return True
    elif str(answer).lower() == str(questions[question_number]["answer"]).lower():
        print(f'Well done, you are correct!\n')
        return True
    else:
        print(f'Nope sorry wrong answer.')
        print(f'The correct answer is:\n{str(questions[question_number]["answer"])}')
        return False

def main(argv):
    quizfile = ''
    try:
        opts, args = getopt.getopt(argv,"hq:",["quizfile="])
    except getopt.GetoptError:
        print ('test.py -q <quizfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -q <quizfile>')
            sys.exit()
        elif opt in ("-q", "--quizfile"):
            quizfile = arg
    print(f'Reading questions from {quizfile}')
    #Read the questions into an array containing dictionaries.
    with open(quizfile,"r",encoding="UTF-8") as quiz:
        for row in csv.reader(quiz, dialect=csv.excel,delimiter=',',quotechar='"', lineterminator="\r\n",skipinitialspace=True):
            try:
                #print(f'{row}')
                answer = row.pop()
                question = row.pop()
                questions.append({"question": question,
                                "answer": answer})
            except:
                print(f"Row can't be parsed. Skipping.")
        print(f'Loaded {len(questions)} questions.')
    score = 0

    print(f'Your score is currently {score}')

    question_count = int(input('How many questions do you want to answer?\n'))

    if question_count> 1:
        print(f'Okay, here come your {question_count} questions')
    else:
        print(f'Okay, here is your question.')

    for i in range(int(question_count)):
        if ask(questions):
            score = score +1
        print(f'Score {score}')
        print(f'Next Question.')
    print(f'Your final score is {score}')




if __name__ == "__main__":
    main(sys.argv[1:])