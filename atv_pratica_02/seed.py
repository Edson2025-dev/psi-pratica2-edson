from models import Autor, Livro


def popular_banco(session):
    # TODO: crie pelo menos 3 autores e 6 livros.

    autor1=Autor(nome='Clarice Lispector',pais='Brasil')
    autor2=Autor(nome='Machado de Assis',pais='Brasil')
    autor3=Autor(nome='Conceição Evaristo',pais='Brasil')

    livro1=Livro(titulo='A Hora da Estrela ',ano=1977,autor=autor1)
    livro2=Livro(titulo='Perto do Coração Selvagem.',ano=1977,autor=autor1)
    livro3=Livro(titulo='Memórias Póstumas de Brás Cubas',ano=1881,autor=autor2)
    livro4=Livro(titulo='Dom Casmurro',ano=1899,autor=autor2)
    livro5=Livro(titulo='Olhos D Água',ano=2014,autor=autor3)
    livro6=Livro(titulo='Ponciá Vicêncio .',ano=1977,autor=autor3)

       

    # TODO: relacione os livros aos autores.
    # TODO: use session.add ou session.add_all e session.commit.
    session.add_all([
        autor1,autor2,autor3,livro1,livro2,livro3,livro4,livro5,livro6
    ])

    session.commit()
