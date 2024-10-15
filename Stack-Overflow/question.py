import uuid
from comment import Comment
from answer import Answer
from tag import Tag
from typing import List

class Question:
    def __init__(self, content, title, author, tag_names) -> None:
        self.id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self.title = title
        self.comments: List[Comment] = []
        self.answers: List[Answer] = []
        self.tags = []
        for name in tag_names:
            self.tags.append(Tag(name))

    
    def add_comment(self, comment:Comment):
        self.comments.append(comment)
    
    def add_answer(self, answer:Answer):
        self.answers.append(answer)
    
    def get_comment(self):
        return self.comments
    
    def get_answer(self):
        return self.answers
