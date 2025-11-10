# python
import customtkinter as ctk
from PIL import Image, ImageTk

def mostrar_splash():
    ctk.set_appearance_mode("dark")
    splash = ctk.CTk()
    splash.title("PiTU - Inicializando...")
    largura_janela, altura_janela = 600, 400
    splash.geometry(f"{largura_janela}x{altura_janela}")
    splash.overrideredirect(True)

    # Centraliza a janela
    largura_tela = splash.winfo_screenwidth()
    altura_tela = splash.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    splash.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Carrega imagem splashscreen.png com fallback
    try:
        img = Image.open("splashscreen.png")
        img = img.resize((largura_janela, altura_janela), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label_img = ctk.CTkLabel(splash, image=img_tk, text="")
        label_img.image = img_tk  # mantém referência
        label_img.pack(fill="both", expand=True)
    except FileNotFoundError:
        label_img = ctk.CTkLabel(splash, text="PiTU", font=("Arial", 32))
        label_img.pack(expand=True)

    # Animação usando after (executando na thread principal)
    def fade_in(i=0):
        splash.attributes("-alpha", i / 100)
        if i < 100:
            splash.after(50, fade_in, i + 5)
        else:
            splash.after(2000, lambda: fade_out(100))

    def fade_out(i=100):
        splash.attributes("-alpha", i / 100)
        if i > 0:
            splash.after(50, fade_out, i - 5)
        else:
            splash.destroy()

    # Inicia com transparência 0 e start fade-in
    splash.attributes("-alpha", 0.0)
    fade_in()
    splash.mainloop()

    # Após o splash ser destruído (mainloop retornou), abre a janela principal
    abrir_pitu()

def abrir_pitu():
    janela = ctk.CTk()
    janela.title("PiTU - Programa Principal")
    janela.geometry("1000x700")

    label = ctk.CTkLabel(janela, text="Bem-vindo ao PiTU!", font=("Arial", 28))
    label.pack(pady=20)

    botao = ctk.CTkButton(janela, text="Abrir Calculador de Diretórios")
    botao.pack(pady=10)

    janela.mainloop()

# Inicia com Splash
mostrar_splash()
