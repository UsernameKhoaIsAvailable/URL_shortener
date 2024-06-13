from flaskr.app import db


class Link(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    alias = db.Column(db.String(255), unique=True, nullable=False)
    url = db.Column(db.String(255))
    password = db.Column(db.String(255))
    click_times = db.Column(db.Integer)
    is_phishing = db.Column(db.Boolean)
    user_id = db.Column(db.ForeignKey('user.id'))
    user = db.relationship('User',
                           back_populates='links')

    def __init__(self, id, alias, url, user_id):
        self.id = id
        self.alias = alias
        self.url = url
        self.user_id = user_id
        self.click_times = 0
        self.is_phishing = False


class User(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_administrator = db.Column(db.Boolean)
    is_blocked = db.Column(db.Boolean)
    token = db.Column(db.String(255))
    is_verified = db.Column(db.Boolean)
    links = db.relationship("Link", back_populates="user", cascade='all, delete-orphan')

    def __init__(self, id, username, email, password, token):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.token = token
        self.is_administrator = False
        self.is_blocked = False
        self.is_verified = False

    def ___json__(self):
        return {
            'id': self.id
        }
