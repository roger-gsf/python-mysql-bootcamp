# Python and MySQL Connection Bootcamp

#### Programas para a Oficina

# Criação da Tabela  MYSQL

CREATE DATABASE usuarios;

create table usuario(
    id integer primary Key AUTO_INCREMENT,
    name varchar(50) not Null,
    senha varchar(50) not Null, 
    e_mail varchar(50) not Null,
    age int not Null);


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

print ('dataBase')
# Configurações do banco de dados
DATABASE_URL = "mariadb+mariadbconnector://root@localhost/usuarios"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Definição do modelo
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    senha=Column(String(50), nullable=False)
    e_mail=Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)



# Função para inserir um novo usuário
def insert_Usuario(name, senha, e_mail, age):
    new_Usuario = Usuario(name=name,  senha=senha, e_mail=e_mail, age=age)
    session.add(new_Usuario)
    session.commit()
    print(f'Usuário {name} adicionado com sucesso!')


# Função para atualizar um usuário
def update_Usuario(name, new_senha, new_e_mail, new_age):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {name} não encontrado.')


# Função para deletar um usuário
def delete_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {name} deletado com sucesso.')
    else:
        print(f'Usuário {name} não encontrado.')


# Função para listar todos os usuários
def list_Usuarios():
    all_Usuarios = session.query(Usuario).all()
    if all_Usuarios:
        for usuario in all_Usuarios:
            print(f'ID: {usuario.id}, Nome: {usuario.name}, senha: {usuario.senha}, e-mail: {usuario.e_mail}, Idade: {usuario.age} ')
    else:
        print('Nenhum usuário encontrado.')


# Função principal para interagir com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar usuário")
        print("2. Atualizar usuário")
        print("3. Deletar usuário")
        print("4. Listar usuários")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == '1':
            name = input("Nome do usuário: ")
            senha=input('Senha:')
            e_mail=input('E-mail:')
            age = int(input("Idade do usuário: "))
            insert_Usuario(name, senha, e_mail, age )
        elif choice == '2':
            list_Usuarios()
            name = input("Nome do usuário a ser atualizado: ")
            new_senha = input('Senha:')
            new_e_mail = input('E-mail:')
            new_age = int(input("Nova idade: "))
            update_Usuario(name, new_senha, new_e_mail, new_age)
        elif choice == '3':
            list_Usuarios()
            name = input("Nome do usuário a ser deletado: ")
            delete_Usuario(name)
        elif choice == '4':
            list_Usuarios()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
 

    main()
    session.close()
    

### versão atualizada para UPDATE e DELETE por ID


from sqlalchemy import create_engine, Column, Integer, String



from sqlalchemy.orm import sessionmaker,declarative_base

# Configurações do banco de dados
DATABASE_URL ="mysql+mysqlconnector://root:@localhost/usuarios"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


# Definição do modelo
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    senha=Column(String(50), nullable=False)
    e_mail=Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)



# Função para inserir um novo usuário
def insert_Usuario(name, senha, e_mail, age):
    new_Usuario = Usuario(name=name,  senha=senha, e_mail=e_mail, age=age)
    session.add(new_Usuario)
    session.commit()
    print(f'Usuário {name} adicionado com sucesso!')


# Função para atualizar um usuário
def update_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        new_senha = input('Senha:')
        new_e_mail = input('E-mail:')
        new_age = int(input("Nova idade: "))

        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {name} não encontrado.')

def update_Usuario_id(id):
    usuario = session.query(Usuario).filter_by(id=id).first()
    if usuario:
        new_name = input('Nome:')
        new_senha = input('Senha:')
        new_e_mail = input('E-mail:')
        new_age = int(input("Nova idade: "))
        usuario.name = new_name
        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {id}  {new_name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {id}   não encontrado.')




# Função para deletar um usuário
def delete_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {name} deletado com sucesso.')
    else:
        print(f'Usuário {name} não encontrado.')

def delete_Usuario_id(id):
    usuario = session.query(Usuario).filter_by(id=id).first()
    user_name= usuario.name
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {id} {user_name} deletado com sucesso.')
    else:
        print(f'Usuário {id} não encontrado.')

# Função para listar todos os usuários
def list_Usuarios():
    session = Session()
    all_Usuarios = session.query(Usuario).all()
    if all_Usuarios:
        for usuario in all_Usuarios:
            print(f'ID: {usuario.id}, Nome: {usuario.name}, senha: {usuario.senha}, e-mail: {usuario.e_mail}, Idade: {usuario.age} ')
    else:
        print('Nenhum usuário encontrado.')


# Função principal para interagir com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar usuário")
        print("2. Atualizar usuário")
        print("3. Deletar usuário")
        print("4. Listar usuários")
        print("5. Atualizar usuario por ID")
        print("6. Deletar usuário por ID")
        print("7. Sair")

        choice = input("Opção: ")

        if choice == '1':
            name = input("Nome do usuário: ")
            senha=input('Senha:')
            e_mail=input('E-mail:')
            age = int(input("Idade do usuário: "))
            insert_Usuario(name, senha, e_mail, age )
        elif choice == '2':
            list_Usuarios()
            name = input("Nome do usuário a ser atualizado: ")
            update_Usuario(name)
        elif choice == '3':
            list_Usuarios()
            name = input("Nome do usuário a ser deletado: ")
            delete_Usuario(name)
        elif choice == '4':
            list_Usuarios()
            input('[Enter] Continua!')
        elif choice == '5':
            list_Usuarios()
            id= int(input('ID do usuario para atualizar:'))
            update_Usuario_id(id)
        elif choice == '6':
            list_Usuarios()
            id = int(input("ID do usuário a ser deletado: "))
            delete_Usuario_id(id)
        elif choice == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    main()
    session.close()



# PythonProjectOficina2

# criar somente o Banco de Dados - NÃO PRECISA CRIAR A TABELA 

CREATE DATABASE  pet_adoption;


#main.py
import tkinter as tk
from model import create_tables
from view import PetView
from controller import PetController

def main():
    create_tables()  # Cria as tabelas no banco de dados
    root = tk.Tk()
    view = PetView(root)
    controller = PetController(view)
    root.mainloop()

if __name__ == "__main__":
    main()


# model.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqlconnector://root:@localhost/pet_adoption"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    species = Column(String(50), nullable=False)
    adopted = Column(Boolean, default=False)

def create_tables():
    Base.metadata.create_all(engine)


# view.py
import tkinter as tk
from tkinter import messagebox
class PetView:
    def __init__(self, master):
        self.master = master
        master.title("Pet Adoption")

        self.label_name = tk.Label(master, text="Nome:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()

        self.label_age = tk.Label(master, text="Idade:")
        self.label_age.pack()
        self.entry_age = tk.Entry(master)
        self.entry_age.pack()

        self.label_species = tk.Label(master, text="Espécie:")
        self.label_species.pack()
        self.entry_species = tk.Entry(master)
        self.entry_species.pack()

        self.button_add = tk.Button(master, text="Adicionar Pet")
        self.button_add.pack()

        self.button_show = tk.Button(master, text="Mostrar Pets")
        self.button_show.pack()

        self.button_adopt = tk.Button(master, text="Adotar Pet")
        self.button_adopt.pack()

        self.text_area = tk.Text(master)
        self.text_area.pack()

        self.button_limpar = tk.Button(master, text="Limpar")
        self.button_limpar.pack()

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_species.delete(0, tk.END)

    def show_pets(self, pets):
        self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
        for pet in pets:
            self.text_area.insert(tk.END, f"Nome: {pet.name}, Idade: {pet.age}, Espécie: {pet.species}, Adotado: {'Sim' if pet.adopted else 'Não'}\n")
    def limpa_area(self):
        self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def get_selected_pet_name(self):
        try:
            selected_text = self.text_area.selection_get()
            return selected_text.split(",")[0].split(":")[1].strip()  # Extrai o nome do pet
        except tk.TclError:
            return None  # Nenhum texto selecionado


# controller.py
from model import create_tables, Session, Pet


class PetController:
    def __init__(self, view):
        self.view = view
        self.session = Session()
        self.view.button_add.config(command=self.add_pet)
        self.view.button_show.config(command=self.show_pets)
        self.view.button_adopt.config(command=self.adopt_pet)
        self.view.button_limpar.config(command=self.limpa_area)

    def add_pet(self):
        if self.view.entry_name.get() and self.view.entry_age.get() and self.view.entry_species.get():
            try:
                name = self.view.entry_name.get()
                age = int(self.view.entry_age.get())
                species = self.view.entry_species.get()
                print(name, age, species)
                new_pet = Pet(name=name, age=age, species=species)
                self.session.add(new_pet)
                self.session.commit()
                self.view.clear_entries()
            except ValueError:
                self.view.show_error("Por favor, insira uma idade válida!")
        else:
            self.view.show_error("Por favor, preencha todos os campos.")
    def adopt_pet(self):
        selected_pet_name = self.view.get_selected_pet_name()
        if selected_pet_name:
            pet = self.session.query(Pet).filter_by(name=selected_pet_name).first()
            if pet:
                pet.adopted = True  # Atualiza o status para adotado
                self.session.commit()
                self.view.show_pets(self.session.query(Pet).all())  # Atualiza a lista de pets
                self.view.show_error(f"{pet.name} foi adotado com sucesso!")
            else:
                self.view.show_error("Pet não encontrado.")
        else:
            self.view.show_error("Por favor, selecione um pet para adotar.")


    def show_pets(self):
        pets = self.session.query(Pet).all()
        self.view.show_pets(pets)

    def limpa_area(self):
       self.view.limpa_area()



https://drive.google.com/drive/folders/1m6MNPWeiQqHNtJWBAHrZlaSWwfi98o2r?usp=sharing
