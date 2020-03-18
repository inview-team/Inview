from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ProjectsInfo(db.Model):
    __tablename__ ="projects"

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    info = db.Column('info', db.String)
    image_url = db.Column('image_url', db.String)


    def __init__(self, id,title,info,image_url):
        self.id=id
        self.title=title
        self.info=info
        self.image_url=image_url

    def serialize(self):
        print(self.__dict__)
        return {
            'id': self.id,
            'title': self.title,
            'info': self.info,
            'url': self.image_url
        }

class User(db.Model):
    __tablename__ = "users"
    id=db.Column('id', db.Integer, primary_key=True)
    login=db.Column('login', db.String)
    isAdmin=db.Column('isAdmin', db.Boolean)


    def __init__(self, id, login, isAdmin):
        self.id=id
        self.login=login
        self.isAdmin=isAdmin

    def serialize(self):
        return {
            'id': self.id,
            'login': self.login,
            'isAdmin': self.isAdmin
        }

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
