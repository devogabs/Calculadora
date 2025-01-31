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

# Definindo funções

def calcular():
    try:
        resultado = eval(visor.get()) # Avalia o que está no visor.
        visor.delete(0, tk.END)
        visor.insert(0, resultado) # Se der certo, imprime o resultado
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Algo deu errado :(") # Minha versão do "Syntax Error"

def limpar_visor():
    visor.delete(0, tk.END) # Literalmente limpa o visor

def atualizar_visores(texto):
    current = visor.get()
    visor.delete(0, tk.END)  # Limpar o visor
    visor.insert(0, current + texto) # Atualiza o visor com a nova entrada na frente do q já tava lá antes
# Criando a janela principal

screen = tk.Tk()
screen.title("Calculadora")

# Criando o Visor da Calculadora
visor = tk.Entry(screen, width=16, font=("Verdana", 24), bd=10, relief="sunken", justify="right")
visor.grid(row=0, column=0, columnspan=4)

# Botões principais
botões = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Fazendo com que apertar os botões realmente faça algo
for (texto, linha, coluna) in botões:
    if texto == "=":
        b = tk.Button(screen, text=texto, width=10, height=3, font=("Arial", 18), command=calcular)
    elif texto == "C":
        b = tk.Button(screen, text=texto, width=10, height=3, font=("Arial", 18), command=limpar_visor)
    else:
        b = tk.Button(screen, text=texto, width=10, height=3, font=("Arial", 18), command=lambda t=texto: atualizar_visores(t))
    b.grid(row=linha, column=coluna)

# Mantendo a janela aberta
screen.mainloop()