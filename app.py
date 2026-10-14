from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)


# Modelo User
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"User<Name: {self.name}, Email: {self.email}>"


def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada correctamente.")
        
def insert_users():
    with app.app_context():
        user1 = User(name="Alan Brito", email="alan@gmail.com")
        user2 = User(name="Elsa Flores", email="elsa@gmail.com")
        user3 = User(name="Zacarias Conde", email="Zacarias@gmail.com")
        
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        
        db.session.commit()
        print("Usuario insertados Correctamente..")
        
        
        


if __name__ == '__main__':
    init_db()
    insert_users()

