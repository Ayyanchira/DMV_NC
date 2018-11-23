import json
import Questionnaire

class MainLogic:

    def __init__(self, answerA=None, answerB=None, answerC=None, answerD=None, correctAnswer=None):
        self.question = None
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.correctAnswer = correctAnswer

    def getAnswers(self):
        return self.answerA, self.answerB, self.answerC, self.answerD

    def setAnswers(self, option, answer):
        if option == "1":
            self.answerA = answer

        if option == "2":
            self.answerB = answer

        if option == "3":
            self.answerC = answer

        if option == "4":
            self.answerD = answer


if __name__ == "__main__":
    # data = { }
    # for x in range(1,10):
    #
    #     q1 = Question()
    #     q1.question = input("Enter question number {}".format(x))
    #     q1.answerA = input("Enter option 1")
    #     q1.answerB = input("Enter option 2")
    #     q1.answerC = input("Enter option 3")
    #     q1.answerD = input("Enter option 4")
    #
    #     data["question {}".format(x)] = q1
    #
    # print(data)

    print("Hi! Welcome to North Carolina DMV Test.")
    difficulty = input("Input the Difficulty level you want:\n 1: Easy \n 2: Moderate \n 3: Difficult")
    print("Thank you for the input....")

    print("Generating question set for your test...")
    # call sakshis function by passing parameter difficulty and 15 if required
    questionnaire = Questionnaire
    questionnaire.maxScore = 15
    questionnaire.currentScore = 0
    retryAttempt = 0
    print(
        "Your Question set is ready.\n INFORMATION: There will be 15 questions asked. Each question will have 4 option to choose from out of which one will be the correct one.")
    print("After each question, press desired option number and press enter to proceed.")

    # TODO if difficulty = 1
    print("For difficulty level easy, you get an extra chance to if your first answer is wrong.")

    input("Press enter to begin the test")



    for question in questionnaire:

        # Reset retry attempt
        if difficulty == 1:
            retryAttempt = 1


        # Ask the question
        print(question.question)
        print("Option 1 : ", question.answerA)
        print("Option 2 : ", question.answerA)
        print("Option 3 : ", question.answerA)
        print("Option 4 : ", question.answerA)

        # Take input from user
        selectedAnswer = input("Type the option number and press enter")

        # Check if its correct
        if selectedAnswer == question.correctAnswer:
            print("Correct Answer")
            # If correct, add 1 to the score
            questionnaire.currentScore += 1

        else:
            if retryAttempt > 0:
                while retryAttempt > 0:
                    selectedAnswer = input("Ahh thats wrong... Try another option...")
                    if selectedAnswer == question.correctAnswer:
                        print("There you go!!!")
                        # If correct, add 1 to the score
                        questionnaire.currentScore += 1
                    else:
                        retryAttempt -= 1



    # print("Your question is {}. The answer is {}".format(q1.question, q1.answerA))
