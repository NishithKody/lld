import uuid
from typing import List
from comment import Comment

class Answer:
    def __init__(self, author, content) -> None:
        self.id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self.comments: List[Comment] = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)