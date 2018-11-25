import json
import Questionnaire
import spl
from art import *

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


    print("#####################################################################################################################################################################")
    welcomeMessage = text2art("             Welcome   to   NC  DMV  Test")
    print(welcomeMessage)
    print("#####################################################################################################################################################################")
    difficulty = input("\n\nInput the Difficulty level you want:\n 1: Easy \n 2: Moderate \n 3: Difficult\n\n")
    
    #print("Generating question set for your test...")
    # call sakshis function by passing parameter difficulty and 15 if required
    splInstance = spl.dataCollection('Spl_1.xlsx')
    #debug
    # print(splInstance.book)
    questions = splInstance.getQuestions(int(difficulty))
  #debug
    #print(questions)
    questionnaire = Questionnaire.Questionnaire(questions,0,0)
    questionnaire.maxScore = 15
    questionnaire.currentScore = 0
    retryAttempt = 0

    print(
        "\nYour Question set is ready.\nINFORMATION: There will be 15 questions asked. Each question will have 4 option to choose from out of which one will be the correct one.")
    print("After each question, press desired option number and press enter to proceed.\n")

    # TODO if difficulty = 1
    if int(difficulty) == 1:
        print("For difficulty level easy, you get an extra chance to if your first answer is wrong.\n\n")

    input("Press enter to begin the test\n")
    print(text2art("Score : 0/15"))
    print("#####################################################################################################################################################################")
    for (index, question) in enumerate(questions):
        # Reset retry attempt

        if int(difficulty) == 1:
            retryAttempt = 1
        # Ask the question
        print("Question ",index + 1)
        print(question["Question"])
        print("\n Options Are:")
        print("[1] : ", question["option1"])
        print("[2] : ", question["option2"])
        print("[3] : ", question["option3"])
        print("[4] : ", question["option4"])

        # Take input from user
        selectedAnswer = input("Type the option number and press enter: \n")
        # Check if its correct
        if int(selectedAnswer) == int(question["correctAnswer"]):
            print(text2art("Great!"))
            # If correct, add 1 to the score
            questionnaire.currentScore += 1

        else:
            print(text2art("Oops! Thats wrong!"))
            
            if retryAttempt > 0:
                while retryAttempt > 0:
                    selectedAnswer = input(text2art("Try another option..."))
                    if int(selectedAnswer) == int(question["correctAnswer"]):
                        print(text2art("Awesome! You Got It!"))
                        # If correct, add 1 to the score
                        questionnaire.currentScore += 1
                    else:
                        print(text2art("Never mind."))
                    retryAttempt -= 1
        scoreMessage = ("Score : {} / 15".format(questionnaire.currentScore))
        print(text2art(scoreMessage))
        print("#####################################################################################################################################################################")
    if questionnaire.currentScore > 10:
        congratulationsMessage = text2art("Congratulations! You Passed !!!")
        print(congratulationsMessage)
    else:
        failureMessage = text2art("You failed!")
        print(failureMessage)
