import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

#configurando a engine do BD
engine = create_engine ('sqlite:///datadabese.db')

#configurando a sessão no BD
Session = sessionmaker(engine)

#criando a tabela
Base = declarative_base ()

class Usuario (Base):
    __tablename__ = 'usuarios'
    id =Column (Integer,primary_key=True)
    nome = Column (String, nullable=False)
    tipo = Column (String,nullable=False)

def insert_usuario(nome_usuario,tipo_usuario):
    session = Session()
    try:
        if all ([nome_usuario,tipo_usuario]):
            usuario = Usuario(nome = nome_usuario, tipo = tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuario {nome_usuario} criado com sucesso!')
        else:
            print('É obrigatorio preencher o nome e o tipo de usuário!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuario {nome_usuario}: {e}')
    finally:
        session.close()

def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()

        for i in dados:
            print(f'Usuario: {i.nome} - Tipo: {i.tipo}')

    except Exception as e:
        print('Ocorreu algum  erro ao realizar a sua consulta de usuario(os)!')

    finally:
        session.close()


def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()
    try:
        if all([id_usuario,nome_usuario]):
            usuario = session.query (Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print('Nome do Usuario alterado com sucesso!')
        else:
            print('Informe um Id e um novo Nome para o usuário!')
    except Exception as e:
        session.rollback()
        print('Ocorreu algum  erro ao atualizar o(s) usuario(os)!')

    finally:
        session.close()

def delete_usuario (id_usuario):
    session = Session()
    try:
        if id_usuario:
            usuario = session.query (Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuario de Id {id_usuario} deletado com sucesso!')
        else:
            print('Por favor informe o Id que deseja deletar!')
    except Exception as e:
        session.rollback
        print(f'Erro ao tentar deletar o usuario de ID {id_usuario}!')
    finally:
        session.close()

if __name__ == '__main__':
    os.system('cls')
    Base.metadata.create_all(engine)
    #insert_usuario('Gabriela', 'Convidado')
    #select_usuarios('Laura')
    #update_nome_usuario('2', 'Laura')
    delete_usuario(5)
