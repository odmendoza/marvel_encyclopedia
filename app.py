from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)
#db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    # pub_date = db.Column(db.DateTime, nullable=False,
    #     default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


teams=db.Table(
    'teams',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
    db.Column('hero_id', db.Integer, db.ForeignKey('hero.id'), primary_key=True)
)


class Hero (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    teams = db.relationship('Team', secondary=teams, lazy='subquery', backref=db.backref('heros', lazy=True))

    def __repr__(self):
        return '<Hero %r>' % self.name


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Hero %r>' % self.name


@app.route('/', methods=['GET'])
def index():
    users = User.query.all()
    danilo = User.query.filter_by(username='Danilo').first()
    print(users)
    print(danilo.username, ' | ', danilo.email)
    return {}


if __name__ == '__main__':
    app.run()
