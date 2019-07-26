from question import Question
class Quiz:
    questions = []

    @classmethod
    def loadQuestion(cls):
        with open("question.txt") as f:
            data = f.readlines()
            for line in data:
                q = line.split(",")
                cls.questions.append(Question(*q))

    @classmethod
    def begin_quiz(cls):
        cls.loadQuestion()
        correct = 0
        worng = 0
        total = len(cls.questions)
        print(f"Total no. of Questions: {total}")
        for i,question in enumerate(cls.questions):
            print(f"{i+1}. {question}")
            ch = input("Enter the choice [A,B,C,D] only... :")
            if ch == question.ans.strip():
                correct += 1
            else:
                worng += 1

        cls.show_results(correct,worng)

    @classmethod
    def show_results(cls,correct,worng):
        print("*"*50)
        total = len(cls.questions)
        print(f"Total Questions: {total}")
        print(f"No. of Correct:{correct}")
        print(f"No. of worng:{worng}")
        percentage = ((correct/total)*100)
        print(f"Percentage:{percentage}")
        if percentage >= 60:
            print("Congrats!! You passed the test")
        else:
            print("Better  Luck Next Time")