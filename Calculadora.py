import tkinter as tk

'''
Componentes principais do Tkinter:
Tk(): Cria a janela principal da interface.

Exemplo: janela = tk.Tk()
Label(): Exibe um texto ou imagem na janela.

Exemplo: label = tk.Label(janela, text="Olá!")
Button(): Cria um botão que pode acionar uma função quando clicado.

Exemplo: botao = tk.Button(janela, text="Clique", command=minha_funcao)
Entry(): Cria uma caixa de entrada onde o usuário pode digitar texto.

Exemplo: entrada = tk.Entry(janela)
Text(): Cria uma área de texto multilinha.

Exemplo: caixa_texto = tk.Text(janela)
Frame(): Cria uma "caixa" para organizar outros widgets.

Exemplo: frame = tk.Frame(janela)
pack(): Um método de layout simples que coloca os widgets de forma empilhada na janela.

Exemplo: label.pack()
grid(): Coloca os widgets em uma estrutura de grade (linha e coluna).

Exemplo: label.grid(row=0, column=0)
place(): Permite posicionar widgets em coordenadas específicas na janela.

Exemplo: label.place(x=50, y=100)
mainloop(): Mantém a interface aberta e interativa.

Exemplo: janela.mainloop()
================================================================================================
Estrutura básica com Tkinter:

# Definindo uma função
def funcao():
    print("Hello World!")

# Criando a Janela principal (o "main menu")
janela = tk.Tk()

# Título da Janela
janela.title("Título")

# Criando um widget Label (texto)
label = tk.Label(janela, text="Pressione o botão")
label.pack()  # Colocando o Label na janela

# Criando um widget Button (botão)
botao = tk.Button(janela, text="Clique aqui", command=saudacao)
botao.pack()  # Colocando o botão na janela

# Mantendo a janela aberta
janela.mainloop()

'''

# Bom, vamos começar então:

def soma(): # Definindo a primeira função (de muitas):
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"Resultado: {resultado}")

# Criando a janela principal

screen = tk.Tk()
screen.title("Calculadora")

# Criando os elementos que vão aparecer na tela (eu acho)
entrada1 = tk.Entry(screen)
entrada2 = tk.Entry(screen)
botao_adicao = tk.Button(screen, text= "+", command= soma)
label_resultado = tk.Label(screen, text= "Resultado: ")

# Organizando os widgets com grid
entrada1.grid(row=0, column=0)
entrada2.grid(row=0, column=1)
botao_adicao.grid(row=1, column=0, columnspan=2)
label_resultado.grid(row=2, column=0, columnspan=2)

# Mantendo a janela aberta
screen.mainloop()