1. Onde estão os modelos ORM no seu projeto?

no arquivo models.py nas classes Livro e Autor.

2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?

o lado um fica com a classe autor pois partimos da ideia que um "autor" pode ter varios livros , e lodo "muitos" fica com a classe Livro onde muitos livros pode pertencer a um mesmo autor.

3. Para que serve o ForeignKey em Livro.autor_id ?

Essa é a chave estrageira que serve para conectar as duas tabelas e assim é possivel relacionar as duas .
4. O que acontece se você esquecer o session.commit() após inserir os dados?

Não são inseridos no banco e ficam apenas na sessao.