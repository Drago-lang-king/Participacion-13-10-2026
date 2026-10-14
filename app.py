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

class Product(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f"Product<Name: {self.name}, Price: {self.price}, Stock: {self.stock}"


def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada correctamente.")
        
def insert_product():
    with app.app_context():
        producto1 = Product(name="Naranja", price=35.50, stock=10)
        producto2 = Product(name="Manzana", price=23.85, stock=20)
        producto3 = Product(name="Lima", price=33.40, stock=30)
        
        db.session.add(producto1)
        db.session.add(producto2)
        db.session.add(producto3)
        
        db.session.commit()
        print("Productos creados Corectamente")

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
        
def query_users():
    with app.app_context():
        print("Listado de Usuarios")
        
        users = User.query.all()
        for i in users:
            print(i)
            
        print("\nListado de registors filtrados")
        filtros = User.query.filter(User.id>=2).all()
        for j in filtros:
            print(j)
            
        print("\nObterner un solo registro")
        user = User.query.filter_by(id=1).first()
        if user:
            print(user)
        else:
            print("Usuario no encontrado")
            
def update_user():
    with app.app_context():
        print("\Actualizacion de un registro")
        
        user = User.query.filter_by(id=1).first()
        if user:
            user.name = "Pepe Trueno"
            user.email = "pepe@gmail.com"
            db.session.commit()
            print("Usuario actualizado")
        else:
            print("Usuario no encontrado")

def delete_user():
    with app.app_context():
        print("\Eliminacion de registro")
        user = User.query.filter_by(id=3).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            print("Usuario eliminado satisfactoriamente")
        else:
            print("Usuario no encontrado")

if __name__ == '__main__':
    init_db()
    insert_product()
    #insert_users()
    #delete_user()
    #query_users()
    #update_user()
