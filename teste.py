import tkinter as tk
from PIL import Image, ImageTk

# Cores
COR_FUNDO_ESQUERDA = "#808080"
COR_FUNDO_DIREITA = "#D3D3D3"

# Janela principal
janela = tk.Tk()
janela.state("zoomed")
janela.configure(bg="black")

# Frame principal
frame_principal = tk.Frame(janela)
frame_principal.pack(fill="both", expand=True)

# Frame da esquerda (largura fixa)
largura_esquerda = 500
frame_esquerda = tk.Frame(frame_principal, bg=COR_FUNDO_ESQUERDA, width=largura_esquerda)
frame_esquerda.pack(side="left", fill="y")
frame_esquerda.pack_propagate(False)

# Título
titulo = tk.Label(frame_esquerda, text="TÍTULO", font=("Arial", 24, "bold"), bg=COR_FUNDO_ESQUERDA, fg="black")
titulo.pack(pady=(40, 20))

# Botões
for texto in ["BOTÃO 1", "BOTÃO 2", "BOTÃO 3"]:
    botao = tk.Button(frame_esquerda, text=texto, font=("Arial", 14), width=20)
    botao.pack(pady=10)

# Frame da direita (ocupa o restante)
frame_direita = tk.Frame(frame_principal, bg=COR_FUNDO_DIREITA)
frame_direita.pack(side="left", fill="both", expand=True)

# Carregar imagem SEM redimensionar
imagem_original = Image.open("exemplo.png")  # Coloque a imagem na mesma pasta do código
imagem_tk = ImageTk.PhotoImage(imagem_original)

# Exibir imagem do lado direito, colada na direita e centralizada verticalmente
label_imagem = tk.Label(frame_direita, image=imagem_tk, bg=COR_FUNDO_DIREITA)
label_imagem.pack(side="right", anchor="e", pady=20)
label_imagem.image = imagem_tk  # Referência para não ser coletada pelo garbage collector

janela.mainloop()
