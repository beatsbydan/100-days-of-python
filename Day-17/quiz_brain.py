class QuizBrain:
    def __init__(self, questions):
        self.question_num = 0
        self.score = 0
        self.questions = questions
    
    def still_has_questions(self):
        return self.question_num < len(self.questions)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is: {correct_ans}")
        print(f"Your current score: {self.score}/{self.question_num}")
        print(f"\n")
    
    def next_question(self):
        self.question_num += 1
        choice = input(f"Q.{self.question_num}: {self.questions[self.question_num].text} (True/False)")
        self.check_answer(self, choice, self.questions[self.question_num].answer)