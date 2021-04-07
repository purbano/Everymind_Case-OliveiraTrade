#Importação de bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

# Criação da janela
app = Tk()

# Título da janela
app.title("Oliveira Trade - Login")
app.iconbitmap(default="image/IconeOliveira.ico")

# Dimensionamento da janela
app.geometry("600x380")
app.configure(background="#fff")
app.resizable(width=False, height=False) #fixar o tamanho da janela

#Inserção da imagem na tela
icone = PhotoImage(file="image/OliveiraTradeLogo.png")

# Organização da janela
LeftFrame = Frame(app, width=200, height=380, bg="#fff", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(app, width=400, height=380, bg="#66CDAA", relief="raise")
RightFrame.pack(side=RIGHT)

IconeLabel = Label(LeftFrame, image=icone, bg="#fff")
IconeLabel.place(x=10, y=100)

#Tela de Sign in
UsuarioLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic",13), bg="#66CDAA", fg="#fff")
UsuarioLabel.place(x=40, y=100)

UsuarioDados = ttk.Entry(RightFrame, width=35)
UsuarioDados.place (x=120, y=105)

SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic",13), bg="#66CDAA", fg="#fff")
SenhaLabel.place(x=40, y=140)

SenhaDados = ttk.Entry(RightFrame, width=35, show="•")
SenhaDados.place (x=120, y=145)

#Função login, a qual verifica se os valores entre o banco de dados e o Sign In estão iguais
def Login():
    Usuario = UsuarioDados.get()
    Senha = SenhaDados.get()

    DataBase.cursor.execute("""
    SELECT * FROM Usuario
    WHERE (Usuario = ? AND Senha = ?) 
    """, (Usuario, Senha))
    print("Login Efetuado!")
    verificarLogin = DataBase.cursor.fetchone()
    try:
        if (Usuario in verificarLogin and Senha in verificarLogin):
            messagebox.showinfo(title="Tela de Login", message="Acesso confirmado. Seja bem vindo!")
    except:
        messagebox.showerror(title="Login inválido", message="Acesso negado. Verifique se está cadastrado no sistema!")

#Inserção dos botões
BtnLogin = ttk.Button(RightFrame, text="Login", width=25,command=Login)
BtnLogin.place(x=125, y=210)

#Definindo a função de registro
def Registro():
    #Fazendo com que botões de login saiam da tela
    BtnLogin.place(x=5000)
    BtnRegistro.place(x=5000)
    #Ajuste do campo Usuário e Senha
    UsuarioDados.place(x=120, y=225)
    UsuarioLabel.place(x=30, y=220)
    SenhaDados.place(x=120, y=265)
    SenhaLabel.place(x=30, y=260)

    #Tela de Sign up
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 13), bg="#66CDAA", fg="#fff")
    NomeLabel.place(x=30, y=20)
    NomeDados = ttk.Entry(RightFrame, width=35)
    NomeDados.place (x=120, y=25)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 13), bg="#66CDAA", fg="#fff")
    EmailLabel.place(x=30, y=60)
    EmailDados = ttk.Entry(RightFrame, width=35)
    EmailDados.place (x=120, y=65)

    TelefoneLabel = Label(RightFrame, text="Telefone:", font=("Century Gothic", 13), bg="#66CDAA", fg="#fff")
    TelefoneLabel.place(x=30, y=100)
    TelefoneDados = ttk.Entry(RightFrame, width=35)
    TelefoneDados.place(x=120, y=105)

    DataNascimentoLabel = Label(RightFrame, text="Data de nascimento:", font=("Century Gothic", 13), bg="#66CDAA", fg="#fff")
    DataNascimentoLabel.place(x=30, y=140)
    DataNascimentoDados = ttk.Entry(RightFrame, width=18)
    DataNascimentoDados.place(x=220, y=145)

    CPFLabel = Label(RightFrame, text="CPF:", font=("Century Gothic", 13), bg="#66CDAA", fg="#fff")
    CPFLabel.place(x=30, y=180)
    CPFDados = ttk.Entry(RightFrame, width=35)
    CPFDados.place(x=120, y=185)

    #Inserindo os botões de registro nesta tela Sign Up
    def RegistroBancoDados(): #Registro dos campos ao banco de dados
        Nome = NomeDados.get()
        Email = EmailDados.get()
        Telefone = TelefoneDados.get()
        DataNascimento = DataNascimentoDados.get()
        Cpf = CPFDados.get()
        Usuario = UsuarioDados.get()
        Senha = SenhaDados.get()

        #Avaliação do preenchimento dos dados
        if (Nome=="" and Email=="" and Telefone=="" and DataNascimento=="" and Cpf=="" and Usuario=="" and Senha==""):
            messagebox.showerror(title="Erro de cadastro!", message="Preencha todos os campos!")
        else:
            DataBase.cursor.execute("""
            INSERT INTO Usuario(Nome, Email, Telefone, DataNascimento, Cpf, Usuario, Senha) VALUES(?, ?, ?, ?, ?, ?, ?)    
            """, (Nome, Email, Telefone, DataNascimento, Cpf, Usuario, Senha))
            DataBase.conn.commit()
            messagebox.showinfo(title="Informação de cadastro", message="Cadastro realizado com sucesso!")

    RegistroBtn = ttk.Button(RightFrame, text="Registro", width=25, command=RegistroBancoDados)
    RegistroBtn.place(x=125, y=300)

    #Função para retornar a tela de Sign in
    def VoltarLogin():
        #Remover os campos de cadastro e ajuste dos campos
        NomeLabel.place(x=5000)
        NomeDados.place(x=5000)
        EmailLabel.place(x=5000)
        EmailDados.place(x=5000)
        TelefoneLabel.place(x=5000)
        TelefoneDados.place(x=5000)
        DataNascimentoLabel.place(x=5000)
        DataNascimentoDados.place(x=5000)
        CPFLabel.place(x=5000)
        CPFDados.place(x=5000)
        UsuarioLabel.place(x=40, y=100)
        UsuarioDados.place(x=120, y=105)
        SenhaLabel.place(x=40, y=140)
        SenhaDados.place(x=120, y=145)
        RegistroBtn.place(x=5000)
        BtnVoltar.place(x=5000)

        #Botões de login de volta a tela
        BtnLogin.place(x=125)
        BtnRegistro.place(x=125)

    BtnVoltar = ttk.Button(RightFrame, text="Voltar", width=25, command=VoltarLogin)
    BtnVoltar.place(x=125, y=340)

BtnRegistro = ttk.Button(RightFrame, text="Registro", width=25, command=Registro)
BtnRegistro.place(x=125, y=245)

#Fixação da tela
app.mainloop()
