import sqlite3

conexao = sqlite3.connect('banco_de_dados')
cursor = conexao.cursor()

# execução de comandos
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(150), idade INT, curso VARCHAR(150))')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Raphaela", 19, "Eng. de Software")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Victor", 19, "Eng. de Software")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ana", 19, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Duda", 19, "Ciências C.")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Davi", 19, "Sistemas de Informação")')

conexao.commit()  # envio de informações
conexao.close()  # fechamento da conexão com o banco de dados
