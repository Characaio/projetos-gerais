import sqlite3 as sql3

conn = sql3.connect('dados.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS employees (
                   id INT AUTO_INCREMENT  PRIMARY KEY,
                   first_name VARCHAR(100) NOT NULL,
                   last_name VARCHAR(100) NOT NULL,
                   age INT
               )
               '''
                
            )
run = True
while run:
    first_name = str(input('Qual seu primeiro nome?'))
    last_name = str(input('Qual é seu ultimo nome?'))
    while True:
        try:
            age = int(input('qual é sua idade?'))
            break
        except:
            print("coloca um NUMERo")
    dados = (first_name, last_name, age)
    cursor.execute('''INSERT INTO employees (first_name,last_name,age)
                VALUES (?,?,?)''',dados)


    cursor.execute(''' SELECT * FROM employees''')

    ans = cursor.fetchall()

    for i in ans:
        print(i)
        
    conn.commit()
    escolha = str(input('você quer colocar mais dados nessa tabela? Y/N'))
    if escolha.upper() == 'Y':
        pass
    else:
        run = False



conn.close()