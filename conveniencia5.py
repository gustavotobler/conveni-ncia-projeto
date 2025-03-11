import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ========== Banco de Usuários (Simples) ========== #
usuarios = {
    'admin': {'senha': 'admin123', 'tipo': 'admin'},
    'user': {'senha': 'user123', 'tipo': 'user'}
}

# ========== Dados dos produtos ========== #
produtos = {
    'Gelo': {'preco': 20.00, 'imagem': 'imagens/gelo.jpg'},
    'Água': {'preco': 4.99, 'imagem': 'imagens/agua.png'},
    'Água com gás': {'preco': 4.99, 'imagem': 'imagens/aguacomgas.png'},
    'toddynho': {'preco': 2.50, 'imagem': 'imagens/tody.png'},
    
    'Fanta 2l': {'preco': 12.00, 'imagem': 'imagens/Fanta.png'},
    'Pepsi 2l': {'preco': 12.00, 'imagem': 'imagens/pepsi.jpg'},
    'Coca cola 2l': {'preco': 12.00, 'imagem': 'imagens/cocacola.png'},
    'Sprite': {'preco': 62.00, 'imagem': 'imagens/sprite.png'},
    'Guaraná': {'preco': 62.00, 'imagem': 'imagens/guarana.png'},
    'Dolly': {'preco': 7.00, 'imagem': 'imagens/dolly.jpg'},
    'Soda': {'preco': 12.00, 'imagem': 'imagens/soda.jpg'},
    'Schweppes': {'preco': 6.00, 'imagem': 'imagens/schweppes.png'},
    
    'Monster': {'preco': 12.00, 'imagem': 'imagens/monster.png'},
    'RedHorse': {'preco': 12.00, 'imagem': 'imagens/redhorse.jpg'},
    'Redbull': {'preco': 10.00, 'imagem': 'imagens/redbull.jpg'},
    'Baly': {'preco': 11.00, 'imagem': 'imagens/baly.jpg'},
     
    'Bacardi': {'preco': 52.00, 'imagem': 'imagens/bacardi.png'},
    'Jagermeister': {'preco': 49.00, 'imagem': 'imagens/jagermeister.png'},
    'Malibu': {'preco': 62.00, 'imagem': 'imagens/malibu.png'},
    'Martini': {'preco': 62.00, 'imagem': 'imagens/martini.png'},
    'Tequila': {'preco': 62.00, 'imagem': 'imagens/tequila.png'},
    'licor': {'preco': 62.00, 'imagem': 'imagens/licor.jpg'},
    'Vodka': {'preco': 62.00, 'imagem': 'imagens/vodka.png'},
    'Vinho': {'preco': 82.99, 'imagem': 'imagens/vinho.png'},
    'Ice': {'preco': 6.00, 'imagem': 'imagens/ice.png'},
    'Jack Daniels': {'preco': 69.99, 'imagem': 'imagens/jackdaniels.png'},
    'Red Label': {'preco': 69.90, 'imagem': 'imagens/redlabel.png'},
    'Garrafa 51': {'preco': 59.99, 'imagem': 'imagens/garrafa51.png' },
    'Velho barreiro': {'preco': 59.00, 'imagem': 'imagens/velho_barreiro.png'},
    
    'Heineken': {'preco': 10.00, 'imagem': 'imagens/heineken.png'},
    'Skol': {'preco': 4.00, 'imagem': 'imagens/skol.png'},
    'Brahma': {'preco': 4.50, 'imagem': 'imagens/brahma.png'},
    'corote': {'preco': 10.00, 'imagem': 'imagens/corote.png'},
    'Corona': {'preco': 7.00, 'imagem': 'imagens/corona.png'},
}

carrinho = {}
usuario_atual = None  # Variável para armazenar o usuário logado

# ========== Tela de Cadastro ========== #
def abrir_tela_cadastro():
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("300x250")

    tk.Label(cadastro_window, text="Usuário:").pack(pady=5)
    entry_novo_usuario = tk.Entry(cadastro_window)
    entry_novo_usuario.pack(pady=5)

    tk.Label(cadastro_window, text="Senha:").pack(pady=5)
    entry_nova_senha = tk.Entry(cadastro_window, show="*")
    entry_nova_senha.pack(pady=5)

    def cadastrar():
        novo_usuario = entry_novo_usuario.get()
        nova_senha = entry_nova_senha.get()

        if novo_usuario in usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
        elif novo_usuario and nova_senha:
            usuarios[novo_usuario] = {'senha': nova_senha, 'tipo': 'user'}
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            cadastro_window.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

# ========== Tela de Login ========== #
def verificar_login():
    global usuario_atual

    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        usuario_atual = usuarios[usuario]['tipo']
        login_window.destroy()
        abrir_loja()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")

tk.Label(login_window, text="Usuário:").pack(pady=5)
entry_usuario = tk.Entry(login_window)
entry_usuario.pack(pady=5)

tk.Label(login_window, text="Senha:").pack(pady=5)
entry_senha = tk.Entry(login_window, show="*")
entry_senha.pack(pady=5)

tk.Button(login_window, text="Login", command=verificar_login).pack(pady=10)
tk.Button(login_window, text="Cadastrar", command=abrir_tela_cadastro).pack(pady=5)

login_window.mainloop()

# ========== Criar Loja Após Login ========== #
def abrir_loja():
    root = tk.Tk()
    root.title("Conveniência Online")
    root.geometry("1024x600")
    root.configure(bg="#FFFFFF")

    # Barra superior
    top_frame = tk.Frame(root, bg="#FFD700", height=50)
    top_frame.pack(fill="x")

    titulo = tk.Label(top_frame, text="🍺 Conveniência Online", fg="black", bg="#FFD700", font=("Arial", 16, "bold"))
    titulo.pack(side="left", padx=20, pady=5)

    # Área de produtos
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
            img = Image.open(dados['imagem']).resize((200, 200))
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

    global carrinho_label
    carrinho_label = tk.Label(carrinho_frame, text="Total: R$ 0.00", bg="#FFD700", font=("Arial", 12, "bold"))
    carrinho_label.pack(side="left", padx=20)

    btn_finalizar = tk.Button(carrinho_frame, text="Finalizar Compra", font=("Arial", 12), command=finalizar_compra)
    btn_finalizar.pack(side="right", padx=20)

    # Se for admin, adiciona botão de gerenciar produtos
    if usuario_atual == 'admin':
        btn_admin = tk.Button(top_frame, text="Gerenciar Produtos", font=("Arial", 10), command=gerenciar_produtos)
        btn_admin.pack(side="right", padx=20)

    root.mainloop()

# ========== Funções do Carrinho ========== #
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

# ========== Executar Loja Após Login ========== #
if usuario_atual:
    abrir_loja()