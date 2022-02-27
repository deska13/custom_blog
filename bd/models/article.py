from bd.models.comment import Comment


class Article:
    def __init__(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.comments = []
        self.author = author


    def get_title(self):
        return self.title


    def get_content(self):
        return self.content


    def get_comments(self):
        return self.comments


    def add_comment(self, content):
        self.comments.append(Comment(content))


    def get_id(self):
        return self.id


    def get_author(self):
        return self.author
