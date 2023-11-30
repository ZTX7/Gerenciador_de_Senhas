import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk



# CONEXÃO AO BANCO DE DADOS
import sqlite3

conexao = sqlite3.connect("aplicativo_senha.db")
cursor = conexao.cursor()

# CRIAÇÃO DE UMA TABELA DO BANCO
cursor.execute('''
    CREATE TABLE IF NOT EXISTS login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site_aplicativo TEXT NOT NULL,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    )
''')

# EXECUÇÃO DO COMANDO
conexao.commit()

# FECHAR A CONEXÃO COM O BANCO
conexao.close()

# CRIANDO A JANELA
janela = tk.Tk()
janela.title("Gerenciador de Senhas")
janela.configure(background='#6396c8')
janela.geometry("400x300")
janela.maxsize(width=400, height=300)

frame_janela = tk.Frame(janela, background="#89b9ed")
frame_janela.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)


def abrir_janela2():
    janela2 = tk.Toplevel()
    janela2.geometry("400x300")
    janela2.title('Cadastrar senha')
    janela2.maxsize(width=400, height=300)
    janela2.minsize(width=400, height=300)

    # FUNÇÕES CRUD
    # CREATE / CRIAÇÃO DE DADOS
    def cadastrar_senha():

        try:

            if entrada_site_aplicativo.get() == "":
                resultado.config(text="Por favor, preencha todos os campos.")

            elif entrada_senha.get() == "":
                resultado.config(text="Por favor, preencha todos os campos.")

            elif entrada_senha.get() == "":
                resultado.config(text="Por favor, preencha todos os campos.")

            else:

                conexao = sqlite3.connect("aplicativo_senha.db")
                cursor = conexao.cursor()
                sql_insert = "INSERT INTO login (site_aplicativo, usuario, senha) VALUES (?, ?, ?)"
                sql_parameter = [entrada_site_aplicativo.get(), entrada_usuario.get(), entrada_senha.get()]
                cursor.execute(sql_insert, sql_parameter)
                conexao.commit()
                conexao.close()
                resultado.config(text="Cadastro realizado!")

                entrada_site_aplicativo.delete(0, tk.END)
                entrada_usuario.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)

        except sqlite3.IntegrityError:
                resultado.config(text="Erro ao se comunicar com o banco de dados.")

    # VISUALIZAÇÃO DOS PARÂMETROS
    site_aplicativo = tk.Label(janela2, text='Site/App')
    site_aplicativo.pack(padx=10, pady=5)

    # ENTRADA DE DADOS
    entrada_site_aplicativo = Entry(janela2, width=50)
    entrada_site_aplicativo.pack(padx=10, pady=5)
    entrada_site_aplicativo.delete(0, tk.END)

    # VISUALIZAÇÃO DOS PARÂMETROS
    usuario = tk.Label(janela2, text='Usuário')
    usuario.pack(padx=10, pady=5)

    # ENTRADA DE DADOS
    entrada_usuario = tk.Entry(janela2, width=50)
    entrada_usuario.pack(padx=10, pady=5)

    # VISUALIZAÇÃO DOS PARÂMETROS
    senha = tk.Label(janela2, text='Senha')
    senha.pack(padx=10, pady=5)

    # ENTRADA DE DADOS
    entrada_senha = tk.Entry(janela2, width=50, show="*")
    entrada_senha.pack(padx=10, pady=5)

    # EXECUTAR O BOTAO PARA CADASTRAR
    cadastrar = tk.Button(janela2, text='Cadastrar Senha', width=20, command=cadastrar_senha)
    cadastrar.pack(pady=10)

    # EXIBIR O RESULTADO E ALTERAR O TEXTO DE FORMA DINÂMICA
    resultado = tk.Label(janela2, text="")
    resultado.pack()

    # BOTAO PARA VOLTAR
    voltar = tk.Button(janela2, text="Voltar", width=10, command=janela2.destroy)
    voltar.pack()


def abrir_janela3():
    janela3 = tk.Toplevel()
    janela3.geometry("400x300")
    janela3.title('Verificar senha')
    janela3.maxsize(width=400, height=300)
    janela3.minsize(width=400, height=300)

    #VERIFICA AS CREDENCIAIS E SENHA COM A REFERÊNCIA.
    def verificar_senha():
        try:
            conexao = sqlite3.connect("aplicativo_senha.db")
            cursor = conexao.cursor()
            sql_select = "Select * FROM login WHERE site_aplicativo=? AND usuario=?"
            sql_parameters = [entrada_site_aplicativo.get(), entrada_usuario.get()]
            cursor.execute(sql_select, sql_parameters)
            view_senha = cursor.fetchone()
            conexao.commit()
            conexao.close()

            def verificador():
                if view_senha != "":
                    senha = view_senha[3]
                    resultado.config(text=f"A seguinte senha foi encontrada: '{senha}'")
                else:
                    resultado.config(text=f"Nenhuma senha foi encontrada para\nas credencias informadas")
            if entrada_site_aplicativo.get() == "":
                resultado.config(text=f"Preencha todos os campos.")
            elif entrada_usuario.get() == "":
                resultado.config(text=f"Preencha todos os campos.")
            else:
                return verificador()
        except:
            resultado.config(text=f"Nenhuma senha foi encontrada para\nas credencias informadas")


    # VISUALIZAÇÃO DOS PARÂMETROS
    site_aplicativo = tk.Label(janela3, text='Site/App')
    site_aplicativo.pack(padx=10, pady=5)
    # ENTRADA DE DADOS
    entrada_site_aplicativo = tk.Entry(janela3, width=50)
    entrada_site_aplicativo.pack(padx=10, pady=5)

    # VISUALIZAÇÃO DOS PARÂMETROS
    usuario = tk.Label(janela3, text='Usuário')
    usuario.pack(padx=10, pady=5)
    # ENTRADA DE DADOS
    entrada_usuario = tk.Entry(janela3, width=50)
    entrada_usuario.pack(padx=10, pady=5)

    # EXECUTAR O BOTAO PARA CADASTRAR
    cadastrar = tk.Button(janela3, text='Verificar Senha', width=20, command=verificar_senha)
    cadastrar.place(relx=0.32, rely=0.67)

    # EXIBIR O RESULTADO E ALTERAR O TEXTO DE FORMA DINÂMICA
    resultado = tk.Label(janela3, text="")
    resultado.place(relx=0.25, rely=0.5)

    # BOTAO PARA VOLTAR
    voltar = tk.Button(janela3, text="Voltar", width=10, command=janela3.destroy)
    voltar.place(relx=0.4, rely=0.8)


def abrir_janela4():
    janela4 = tk.Toplevel()
    janela4.geometry("720x480")
    janela4.title("Registros de Login")
    janela4.minsize(width=720, height=480)
    janela4.maxsize(width=720, height=480)

 #RECRIA A TABELA VISUAL DO BANCO DE DADOS NA JANELA 4
    def tabela_senhas():
        conexao = sqlite3.connect("aplicativo_senha.db")
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM login')
        results = cursor.fetchall()
        conexao.close()

        dados = ttk.Treeview(janela4, column=('r_id', 'Site/app', 'Login', 'Senha'), show='headings')
        dados.column("r_id", width=1)
        dados.heading("r_id", text="ID")
        dados.column("Site/app", width=1)
        dados.heading("Site/app", text="Site/App", )
        dados.column("Login", width=1)
        dados.heading("Login", text="Login")
        dados.column("Senha", width=1)
        dados.heading("Senha", text="Senha")
        dados.place(relx=0.05, rely=0.4, relwidth=0.90, relheight=0.45)

        for result in results:
            dados.insert(parent="", index="end", values=(result[0], result[1], result[2], result[3]))

        scroll_table = Scrollbar(janela4, orient="vertical")
        dados.configure(yscroll=scroll_table.set)
        scroll_table.place(relx=0.95, rely=0.4, relwidth=0.04, relheight=0.60)

    #APLICA O CRUDE "DELETE" INFORMANDO O ID.
    def deletar_dados():
        try:
            conexao = sqlite3.connect("aplicativo_senha.db")
            cursor = conexao.cursor()
            cursor.execute(f"DELETE FROM login WHERE id = '{entrada_id.get()}'")
            conexao.commit()
            conexao.close()
            resultado.config(text="Registro deletado! \n Reinicie a janela para atualizar.")

        except sqlite3.IntegrityError:
            resultado.config(text="Verifique se os dados existem, e tente novamente")

        # PROCURA DE PARÂMETROS

    #TEXTO DO CRUDE DELETE.
    deletar = tk.Label(janela4, text="Deletar Login e Senha", font="Arial 12 bold")
    deletar.place(relx=0.105, rely=0.05)

    #TEXTO DO ID.
    select_id = tk.Label(janela4, text="Digite o ID:", font="ArialBold 10")
    select_id.place(relx=0.09, rely=0.18)

    #CAIXA DE ENTRADA DE DADO "ID".
    entrada_id = tk.Entry(janela4, width=20)
    entrada_id.place(relx=0.19, rely=0.18)

    #ACIONA A FUNÇÃO "deletar_dodas()".
    deletar_dados = tk.Button(janela4, text="Deletar", font="ArialBold 11 bold", command=deletar_dados)
    deletar_dados.place(relx=0.18, rely=0.290)

    #EXIBE AS NOTIFICÕES NA TELA.
    resultado = tk.Label(janela4, text="")
    resultado.place(relx=0.05, rely=0.875)

    #ATUALIZA A SENHA NA JANELA4.
    def atualizar_senha():
        try:
            conexao = sqlite3.connect("aplicativo_senha.db")
            cursor = conexao.cursor()
            cursor.execute(f"UPDATE login SET senha='{att_entrada_nova_senha.get()}' WHERE id='{att_entrada_id.get()}'")
            conexao.commit()
            conexao.close()
            resultado.config(text="Senha atualizada!\n Reinicie a janela para atualizar.")

        except:
            resultado.config(text="Verifique se existe dados para o ID informado.")

    txt_atualizar = tk.Label(janela4, text="Atualizar Senha:", font="Arial 12 bold")
    txt_atualizar.place(relx=0.62, rely=0.05)

    info_id = tk.Label(janela4, text="Digite o ID:", font="Arial 10")
    info_id.place(relx=0.53, rely=0.13)
    nova_senha = tk.Label(janela4, text="Digite a nova senha:", font="Arial 10")
    nova_senha.place(relx=0.455, rely=0.22)

    att_entrada_id = tk.Entry(janela4, width=30)
    att_entrada_id.place(relx=0.628, rely=0.135)
    att_entrada_nova_senha = tk.Entry(janela4, width=30)
    att_entrada_nova_senha.place(relx=0.628, rely=0.225)

    resultado = tk.Label(janela4, text="")
    resultado.place(relx=0.05, rely=0.875)

    atualizar = tk.Button(janela4, text="Atualizar", font="ArialBold 11 bold", command=atualizar_senha)
    atualizar.place(relx=0.65, rely=0.290)

    voltar_jan4 = tk.Button(janela4, text="Voltar", font="Arial 11 bold", width=10, command=janela4.destroy)
    voltar_jan4.place(relx=0.45, rely=0.9)

    #CHAMAR TABELA DO BANCO DE DADOS PARA EXIBIÇÃO.
    tabela_senhas()


# TEXTO DE APRESENTAÇÃO E ESCOLHA DA JANELA PRINCIPAL
apresentacao = tk.Label(janela, text='BEM VINDO AO\n- GERENCIADOR DE SENHAS -',
                        foreground="white", background="#6396c8", font="Arial 14 bold")
apresentacao.place(relx=0.0000006, rely=0.05, relwidth=1.009, relheight=0.25)

# CADASTRAR
janela2 = tk.Button(janela, text="Cadastrar Senha", width=20, command=abrir_janela2)
janela2.place(relx=0.32, rely=0.35)

# VERIFICAR
janela3 = tk.Button(janela, text="Verificar Senha", width=20, command=abrir_janela3)
janela3.place(relx=0.32, rely=0.5)

# VISUALIZAR TODAS AS SENHAS
janela4 = tk.Button(janela, text="Visualizar Registros", width=20, command=abrir_janela4)
janela4.place(relx=0.32, rely=0.65)

sair = tk.Button(janela, text="Sair", font="Arial 10", width=9, command=janela.destroy)
sair.place(relx=0.39, rely=0.8)

janela.mainloop()
