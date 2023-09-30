from injetor import Injetor
from database import Database


class Functions():
    def __init__(self):
        self.database = Database()

    def get_injetores(self):
        session = self.database.criar_session()

        lista_injetores = session.query(Injetor).all()

        session.close()

        injetores = list()
        for injetor in lista_injetores:
            injetores.append(injetor.codigo)

        return injetores

    def get_injetor(self, event=None):
        if event != None:
            listbox = event.widget
            codigo_injetor = listbox.get(listbox.curselection())
        else: 
            codigo_injetor = event

        session = self.database.criar_session()

        injetor = session.query(Injetor).filter(Injetor.codigo==codigo_injetor)[0]

        session.close()

        return injetor

    def pesquisar_injetor(self, text):
        pesquisa = f'%{text}%'

        session = self.database.criar_session()

        lista_injetores = session.query(Injetor).filter(Injetor.codigo.like(pesquisa)).all()

        session.close()

        return lista_injetores
    
    def selecionar_fabricante(self, fabricante):
        session = self.database.criar_session()

        lista_injetores = session.query(Injetor).filter(Injetor.fabricante==fabricante).all()

        session.close()

        return lista_injetores