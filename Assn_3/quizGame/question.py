class Question:

    def __init__(self, ques, op1, op2, op3, op4, ans):
        self.ques = ques
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.ans = ans

    def __str__(self):
        return f"{self.ques}\n1. {self.op1}\n2. {self.op2}\n3. {self.op3}\n4. {self.op4}\n"
        