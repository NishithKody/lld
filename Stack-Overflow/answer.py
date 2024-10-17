import uuid
from typing import List
from comment import Comment
from commentable import Commentable
from datetime import datetime

class Answer(Commentable):
    def __init__(self, author, question, content) -> None:
        self.id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self.question = question
        self.comments: List[Comment] = []
        self.creation_time = datetime.now()
        self.is_accepted = False

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
    
    def get_comment(self):
        return self.comments

    def accept(self):
        if(self.is_accepted):
            return ValueError('answer has been accepted')
        
        self.is_accepted = True
        