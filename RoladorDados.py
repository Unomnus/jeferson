import tkinter as tk
from tkinter import messagebox


# Função acionada pelo botão
def mostrar_mensagem():
  messagebox.showinfo("Alô", "Olá! Você criou seu primeiro aplicativo gráfico.")


# Criando a janela principal
janela = tk.Tk()
janela.title("Meu Primeiro App")
janela.geometry("300x150")

# Adicionando um texto (Label)
rotulo = tk.Label(janela, text="Bem-vindo ao Python!", font=("Arial", 12))
rotulo.pack(pady=20)

# Adicionando um botão
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack(pady=10)

# Mantendo a janela aberta
janela.mainloop()