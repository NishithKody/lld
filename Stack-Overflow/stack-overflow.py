from user import User
from answer import Answer
from question import Question
from typing import List,Dict

class StackOverflow:
    _instance = None
    def __init__(self) -> None:
        if(StackOverflow._instance is not None):
            raise Exception("The instance is already present")
        else:
            StackOverflow._instance = self
            self.users: Dict[str, User ] = {}
            self.questions : Dict[str, Question] = {}
            self.answers: Dict[str, Answer] = {}
            
    @staticmethod
    def get_instance():
        if(StackOverflow._instance is None):
            StackOverflow()
        return StackOverflow._instance
    
    def add_user(self, email, name):
        user_id = len(self.users)+1
        user = User(user_id, email, name)
        self.users[user_id] = user
        return user

    def ask_question(self,user: User,title,content,tags):
        question = user.ask_question(title,content,tags)
        self.questions[question.id] = question
        return question

    def answer_question(self, user: User, question, content):
        ans = user.answer_question(question, content)
        self.questions[ans.id] = ans
        return ans

    def add_comment(self, commentable, user:User, content):
        user.comment_on(commentable, content)

