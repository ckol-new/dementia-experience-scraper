class Discussion:
    def __init__(self, url, title, content, comments = []):
        self.url = url
        self.title = title
        self.content = content
        self.comments = comments

    def to_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'content': self.content,
            'comments': [comment.to_dict() for comment in self.comments]
        }

    @classmethod
    def from_dict(cls, data):
        url = data['url']
        title = data['title']
        content_dict = data['content']
        content = list(content_dict)
        comments_dict = data['comments']
        comments = list(comments_dict)
        comments = [Comment.from_dict(comment) for comment in comments]
        
        return cls(
            url=url,
            title=title,
            content=content,
            comments=comments
        )

    def __repr__(self): return f'title {self.title!r}, content {self.content!r}'

    def __eq__(self, other):
        if not isinstance(other, Discussion):
            return False
        return (self.url == other.url and self.title == other.title and self.content == other.content)
     
class Comment:
    def __init__(self, content):
        self.content = content

    def to_dict(self):
        return {
            'content': self.content
        }

    @classmethod
    def from_dict(cls, data):
        content_dict = data['content']
        content = list(content)
        return cls(
            content=content
        )
    
    def __eq__(self, other):
        if not isinstance(other, Comment):
            return False
        return (self.content == other.content)

    def __repr__(self): return f'content {self.content!r}'