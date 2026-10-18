import tkinter as tk
from tkinter import messagebox


# Função acionada pelo botão
def mostrar_mensagem():
  messagebox.showinfo("Alô", "Olá! Você criou seu primeiro aplicativo gráfico.")


# Criando a janela principal
janela = tk.Tk()
janela.title("ROLADOR DADOS")
janela.geometry("800x600")

# Adicionando um texto (Label)
rotulo = tk.Label(janela, text="ROLADOR DE DADOS", font=("Arial", 12))
rotulo.pack(pady=20)

# Adicionando um botão
botao = tk.Button(janela, text="ROLAR", command=mostrar_mensagem)
botao.pack(pady=10)

# Mantendo a janela aberta
janela.mainloop()