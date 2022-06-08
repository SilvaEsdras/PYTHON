

import sqlite3

conn = sqlite3.connect('clientes2.db')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER, cpf VARCHAR(11) NOT NULL, email TEXT NOT NULL, fone VARCHAR(11) NOT NULL, cidade TEXT, uf VARCHAR(2) NOT NULL, criado_em DATE NOT NULL)")

#print('Tabela criada com sucesso')

cursor.execute ("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em) VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11987654321', 'Sao Paulo', 'SP', '2014-06-08')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Bruna', 21, '22222222222', 'bruna@email.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2014-06-09')")

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)VALUES ('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08')")

conn.commit()

print('Dados inseridos com sucesso.')
#desconectando
conn.close()

