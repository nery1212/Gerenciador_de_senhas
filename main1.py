from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerar_senhas():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    senha_letters = [choice(letters) for _ in range(randint(8, 10))]
    senha_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    senha_numeros = [choice(numbers) for _ in range(randint(2, 4))]

    senha_list = senha_letters + senha_symbols + senha_numeros
    shuffle(senha_list)

    senha = "".join(senha_list)
    senha_entry.delete(0, END)
    senha_entry.insert(0, senha)
    pyperclip.copy(senha)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    email = email_entry.get()
    senha = senha_entry.get()
    site = site_entry.get()
    new_data = {
        site:   {
            "email": email,
            "senha": senha,

                    }
    }

    if email == '' or senha == '' or site == '':
        messagebox.showerror("Erro", "Informe os campos")
    else:
        try:
            with open('senhas.json', 'r') as arquivo:
                data = json.load(arquivo)
                data.update(new_data)

        except FileNotFoundError:
            with open('senhas.json', 'w') as arquivo:
                json.dump(new_data, arquivo, indent=4)

        else:
            data.update(new_data)

            with open('senhas.json', 'w') as arquivo:
                json.dump(new_data, arquivo, indent=4)


        finally:
            site_entry.delete(0, END)
            email_entry.delete(0, END)

#-----------------pesquisar senha----------#


def find_password():
    try:
        with open('senhas.json', 'r') as arquivo:
             data = json.load(arquivo)
             site = site_entry.get()
        messagebox.showinfo("Senhas e emails do site", f"Email: {data.get(site)['email']}\n Senha:{data.get(site)['senha']}")

    except FileNotFoundError:
        messagebox.showerror("Erro", "você ainda não colocou senhas de nenhum site. Salve uma senha primeiro")

    except TypeError:
        messagebox.showinfo("Erro",  "Não existe site com esse não salvo")










# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title('Gerenciador de senhas')
logo = PhotoImage(file="logo.png")
janela.config(padx=50, pady=50)
canvas = Canvas(janela, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#labels
label_site = Label(text='site')
label_site.grid(row=1, column=0)

email_label = Label(text='email/username')
email_label.grid(row=2, column=0)

senha_label = Label(text='senha')
senha_label.grid(row=3, column=0)

#entry
site_entry = Entry(width=28)
site_entry.focus()
site_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.insert(0, 'samuel.nery.silva@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)
senha_entry = Entry(width=28)
senha_entry.grid(row=3, column=1)

#botoes

procurar_botao = Button(text='Procurar', command=find_password)
procurar_botao.grid(row=1, column=2)

gerador_senhas_botao = Button(text="gerar senha", command=gerar_senhas)
gerador_senhas_botao.grid(row=3, column=2)

botao_adicionar = Button(text="Adicionar", width=36, command=save)
botao_adicionar.grid(row=4, column=1, columnspan=2)
janela.mainloop()