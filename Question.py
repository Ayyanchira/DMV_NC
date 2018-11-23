# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:34:09 2018

@author: monic
"""

class Question:
    
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer
        
    def get_question(self):
        return self.question
    
    def get_correct_answer(self):
        return self.correct_answer;
    
    def get_answer_choices(self):
        answer_choices = [];
        answer_choices.append(self.answer1)
        answer_choices.append(self.answer2)
        answer_choices.append(self.answer3)
        answer_choices.append(self.answer4)
        
        return answer_choices;

'''
q = Question("question 1", "a1","a2","a3","a4",4)
print(q.get_answer_choices())
print(q.get_question())
print(q.get_correct_answer())
'''


    
    
    