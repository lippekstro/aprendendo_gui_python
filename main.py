import tkinter as tk

# cria janela
window = tk.Tk()
# definindo o tamanho
window.geometry("1000x600")
# mudando o titulo
window.title("Meu teste de GUI com Tkinter")

# criando um frame para organizar e agrupar itens
# borda largura 4 e com um efeito 3D
frame_inicio = tk.Frame(bd=4, relief=tk.RIDGE)

# criando um texto (formatando)
# o master indica a qual frame o item pertence
lbl = tk.Label(
    master=frame_inicio,
    text='HELLO, WORLD',
    foreground='white',
    background='black'
)
# inserindo o texto na janela
# configurando para preencher todo o eixo x e uma margem no eixo Y somente embaixo
lbl.pack(
    fill=tk.X,
    pady=(0,20)
)

def clicar():
    # Esta função será chamada quando o botão for clicado
    # Deve vir antes da criacao do botao
    # ela mostra no console
    print("Botão clicado!")
    # mas tambem cria um label pra inserir na janela
    lbl_click = tk.Label(
        master=frame_inicio,
        text="Botao clicado"
    )
    lbl_click.pack()

# criando um botao
btn = tk.Button(
    master=frame_inicio,
    text="Clique",
    command=clicar
)
# inserindo
btn.pack()

frame_inicio.pack(
    fill=tk.X,
    padx=20,
    pady=20
)


# criando um frame, uma estrutura para agrupar itens na janela
# borda largura 2 e do tipo solida
frame_calculadora = tk.Frame(bd=2, relief=tk.GROOVE)

# criando um label para a entrada de um numero
# o master indica que ele pertence ao frame
lbl_num1 = tk.Label(
    master=frame_calculadora,
    text="Numero 1"
)
# criando o input da entrada
entrada_num1 = tk.Entry(
    master=frame_calculadora
)
# inserindo
lbl_num1.pack()
# inserindo mas colocando margens em x e y
entrada_num1.pack(padx=10, pady=10)

# criando um label para a entrada de outro numero
lbl_num2 = tk.Label(
    master=frame_calculadora,
    text="Numero 2"
)
# criando o input da entrada
entrada_num2 = tk.Entry(
    master=frame_calculadora
)
# inserindo
lbl_num2.pack()
# inserindo mas colocando margens em x e y
entrada_num2.pack(padx=10, pady=10)

# criando a funcao de soma com tratamento de erros
def soma():
    try:
        # captura os valores nos inputs
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        # realiza a soma
        resultado = num1+num2
        # altera o valor do label com o resultado
        lbl_resultado.config(text=f"Resultado: {resultado}")
    except:
        lbl_resultado.config(
            text="Erro: Insira numeros validos",
            background="red",
            foreground="white"
        )

# criando o botao que chama a funcao soma
btn_soma = tk.Button(
    master=frame_calculadora,
    text="Somar",
    command=soma
)

# criando o label que vai exibir resultados e erros
lbl_resultado = tk.Label(
    master=frame_calculadora
)

# inserindo
btn_soma.pack()
lbl_resultado.pack(pady=10)

# inserindo o frame ocupando o eixo X, porem com 20 de margens
frame_calculadora.pack(
    fill=tk.X,
    padx=20,
    pady=20
)


# mantem a janela aberta
window.mainloop()

