import uuid
from comment import Comment
from answer import Answer
from tag import Tag
from typing import List
from commentable import Commentable
from voteable import Voteable
from datetime import datetime
from vote import Vote

class Question(Commentable, Voteable):
    def __init__(self, content, title, author, tag_names) -> None:
        self.id = str(uuid.uuid4())
        self.creation_time = datetime.now()
        self.author = author
        self.content = content
        self.title = title
        self.comments: List[Comment] = []
        self.answers: List[Answer] = []
        self.tags: List[Tag] = []
        for name in tag_names:
            self.tags.append(Tag(name))
        self.votes: List[Vote] = []
        
    def add_comment(self, comment:Comment):
        self.comments.append(comment)
    
    def add_answer(self, answer:Answer):
        self.answers.append(answer)
    
    def get_comment(self):
        return self.comments
    
    def get_answer(self) -> List[Answer]:
        return self.answers
    
    def vote(self, user, value) -> None:
        self.votes.append(Vote(user,value))

    def get_vote_count(self) -> int:
        res = 0
        for vote in self.votes:
            res = res + vote.value
        return res

