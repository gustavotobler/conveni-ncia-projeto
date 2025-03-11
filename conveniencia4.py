import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Dados dos produtos com imagens originais
produtos = {
    'Vodka': {'preco': 62.00, 'imagem': 'imagens/vodka.png'},
    'Schweppes': {'preco': 6.00, 'imagem': 'imagens/schweppes.png'},
    'Heineken': {'preco': 10.00, 'imagem': 'imagens/heineken.png'},
    'Brahma': {'preco': 4.50, 'imagem': 'imagens/brahma.png'},
    'corote': {'preco': 10.00, 'imagem': 'imagens/corote.png'},
    'Ice': {'preco': 35.00, 'imagem': 'imagens/ice.png'},
    'Jack Daniels': {'preco': 69.99, 'imagem': 'imagens/jackdaniels.png'},
    'Água': {'preco': 4.99, 'imagem': 'imagens/agua.png'},
    'Red Label': {'preco': 69.90, 'imagem': 'imagens/redlabel.png'},
    'Coca cola 2l': {'preco': 12.00, 'imagem': 'imagens/cocacola.png'},
    'Fanta 2l': {'preco': 12.00, 'imagem': 'imagens/Fanta.png'},
    'Pepsi 2l': {'preco': 12.00, 'imagem': 'imagens/pepsi.jpg'},
    'Vinho': {'preco': 82.99, 'imagem': 'imagens/vinho.png'},
    'Monster': {'preco': 12.00, 'imagem': 'imagens/monster.png'},
    'Garrafa 51': {'preco': 59.99, 'imagem': 'imagens/garrafa51.png' },
    'skol': {'preco': 4.00, 'imagem': 'imagens/skol.png'}
}

# Configurações globais
carrinho = {}

def adicionar_ao_carrinho(produto):
    if produto in carrinho:
        carrinho[produto]['quantidade'] += 1
    else:
        carrinho[produto] = {'preco': produtos[produto]['preco'], 'quantidade': 1}
    atualizar_carrinho()

def atualizar_carrinho():
    total = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    carrinho_label.config(text=f"Total: R$ {total:.2f}")

def finalizar_compra():
    if not carrinho:
        messagebox.showwarning("Carrinho vazio", "Adicione itens ao carrinho antes de finalizar a compra.")
        return
    detalhes = "\n".join([f"{produto}: {dados['quantidade']}x - R$ {dados['preco'] * dados['quantidade']:.2f}" for produto, dados in carrinho.items()])
    messagebox.showinfo("Compra Finalizada", f"Itens comprados:\n{detalhes}\n\nTotal: R$ {sum(item['preco'] * item['quantidade'] for item in carrinho.values()):.2f}")
    carrinho.clear()
    atualizar_carrinho()

# Criando a janela principal
root = tk.Tk()
root.title("Conveniência Online")
root.geometry("1024x600")
root.configure(bg="#FFFFFF")

# Barra superior
top_frame = tk.Frame(root, bg="#FFD700", height=50)
top_frame.pack(fill="x")

titulo = tk.Label(top_frame, text="🍺 Conveniência Online", fg="black", bg="#FFD700", font=("Arial", 16, "bold"))
titulo.pack(side="left", padx=20, pady=5)

# Área de produtos com rolagem
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame)
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Exibir produtos dinamicamente
colunas = 5
for index, (nome, dados) in enumerate(produtos.items()):
    try:
        img = Image.open(dados['imagem']).resize((180, 200))
        img_tk = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem {dados['imagem']}: {e}")
        continue

    frame_produto = tk.Frame(scrollable_frame, bg="white", bd=2, relief="solid", width=300, height=200)
    frame_produto.grid(row=index // colunas, column=index % colunas, padx=30, pady=40)

    label_img = tk.Label(frame_produto, image=img_tk, bg="white")
    label_img.image = img_tk
    label_img.pack()

    label_nome = tk.Label(frame_produto, text=nome, bg="white", font=("Arial", 10, "bold"))
    label_nome.pack()

    label_preco = tk.Label(frame_produto, text=f"R$ {dados['preco']:.2f}", bg="white", fg="green", font=("Arial", 10))
    label_preco.pack()

    btn_adicionar = tk.Button(frame_produto, text="Adicionar", bg="yellow", command=lambda p=nome: adicionar_ao_carrinho(p))
    btn_adicionar.pack(pady=5)

# Carrinho de compras
carrinho_frame = tk.Frame(root, bg="#FFD700", height=50)
carrinho_frame.pack(fill="x", side="bottom")

carrinho_label = tk.Label(carrinho_frame, text="Total: R$ 0.00", bg="#FFD700", font=("Arial", 12, "bold"))
carrinho_label.pack(side="left", padx=20)

btn_finalizar = tk.Button(carrinho_frame, text="Finalizar Compra", font=("Arial", 12), command=finalizar_compra)
btn_finalizar.pack(side="right", padx=20)

# Rodar o app
root.mainloop()
