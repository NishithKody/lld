from question import Question
from comment import Comment
from answer import Answer

class User:
    def __init__(self, id:str, email:str, name:str) -> None:
        self.id = id
        self.email = email
        self.name = name
        self.rep = 0
        self.questions = []
        self.answers = []
        self.comments = []

    def ask_question(self, title, content, tags):
        qu = Question(content, title, self, tags)
        self.questions.append(qu)
        self.rep += 5
    
    def answer_question(self,question, content):
        ans = Answer(self, question, content)
        self.answers.append(ans)
    
    def  comment_on(self, commentable, content):
        comment = Comment(self, content)
        self.comments.append(comment)
        commentable.add_comment(comment)
    
