from PyQt5 import uic, QtWidgets
import psycopg2

con = psycopg2.connect(host='localhost', database='Produtos',
                       user='postgres', password='kk93909979')

Cursor = con.cursor()

def logar():
    user = login.lnUser.text()
    senha = login.lnSenha.text()

    print(user)
    print(senha)

    if user == 'adminDogcenter' and senha == 'caogato':
        formulario.show()
        login.close()
    else:
        login.label_4.setText('Login ou Senha invalidos')

def sair():
    login.close()

def funcao_principal():
    codigo = formulario.lineEdit.text()
    descricao = formulario.lineEdit_2.text()
    preco = formulario.lineEdit_3.text()

    categoria = 'Sem categoria definida'

    if formulario.radioButton.isChecked():
        print('Categoria Alimentos foi selecionada')
        categoria = 'Alimentos'

    elif formulario.radioButton_2.isChecked():
        print('Categoria Medicamentos foi selecionada')
        categoria = 'Medicamentos'
    
    elif formulario.radioButton_3.isChecked():
        print('Categoria Acessorios foi selecionada')
        categoria = 'Acessorios'

    else:
        print('Nem uma categoria foi selecionada.')
        

    print('Codigo: ', codigo)
    print('Descricao: ', descricao)  
    print('Preco: ', preco)
    print('Categoria:', categoria)

    
    Cursor.execute(
        "INSERT INTO Produtos (Codigo, Descricao, Preco, Categoria) VALUES (%s,%s,%s,%s)", (int(codigo),str(descricao),float(preco),str(categoria))
    )

    con.commit()
    

    formulario.lineEdit.setText('')
    formulario.lineEdit_2.setText('')
    formulario.lineEdit_3.setText('')

def chama_segunda_tela():
    segunda_tela.show()

    cursor = con.cursor()
    comando = "SELECT * FROM Produtos"
    cursor.execute(comando)
    dados_lidos = cursor.fetchall()
    print(len(dados_lidos))

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
formulario = uic.loadUi('tela_cadastro.ui')
segunda_tela = uic.loadUi('listar_dados.ui')
login = uic.loadUi('Tela_inicial.ui')
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
login.btnLogin.clicked.connect(logar)
login.btnSair.clicked.connect(sair)
login.lnSenha.setEchoMode(QtWidgets.QLineEdit.Password)

login.show()
app.exec()
