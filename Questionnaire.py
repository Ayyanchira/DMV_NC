# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:48:49 2018

@author: monic
"""

class Questionnaire:
    def __init__(self, questions, total_marks, marks_scored):
        self.questions = questions
        self.total_marks = total_marks
        self.marks_scored = marks_scored
    
    def display_questions_for_user(self):
        return self.questions
    
    def get_marks_scored(self):
        return self.marks_scored
    
    def get_total_marks(self):
        return self.total_marks
    
    
    
    
    