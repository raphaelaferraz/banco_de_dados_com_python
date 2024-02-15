import sqlite3

conexao = sqlite3.connect('banco_de_dados')
cursor = conexao.cursor()

# execução de comandos
# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(150), idade INT, curso VARCHAR(150))')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Raphaela", 19, "Eng. de Software")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Victor", 19, "Eng. de Software")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ana", 19, "Ciência da Computação")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Duda", 19, "Ciências C.")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Davi", 19, "Sistemas de Informação")')

# Visualizar todos os alunos
dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

# Visualizar aluno com mais de 20 anos
dados2 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for aluno in dados2:
#   print(aluno)

# Visualizar alunos em ordem alfabética
dados3 = cursor.execute(
    'SELECT * FROM alunos WHERE curso == "Eng. de Software" ORDER BY nome')
# for aluno in dados3:
#   print(aluno)

# Contagem de alunos na tabela
dados4 = cursor.execute('SELECT COUNT(*) FROM alunos')
# for dado in dados4:
#   print(dado)

# Atualização de idade de um dos alunos da tabela
# cursor.execute('UPDATE alunos SET idade = 20 WHERE nome="Victor"')

# Remoção do aluno por id
# cursor.execute('DELETE FROM alunos WHERE id = 5')

# Adição de nova coluna
# cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(150), idade INT, saldo FLOAT)')

# Inserção de dados na coluna
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Ana Silva", 35, 1500.00)');
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Bruno Martins", 28, 950.00)');
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Carlos Eduardo", 42, 2000.00)');
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Daniela Rocha", 30, 3000.00)');

# Nome e a idade dos clientes com idade superior a 30 anos
dados5 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
# for dado in dados5:
#   print(dado)

# Saldo médio dos clientes
dados6 = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
for dado in dados6:
   print(dado)

conexao.commit()  # envio de informações
conexao.close()  # fechamento da conexão com o banco de dados
