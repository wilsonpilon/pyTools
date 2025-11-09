import customtkinter as ctk
import time
import threading
from PIL import Image, ImageTk

def mostrar_splash():
    splash = ctk.CTk()
    splash.title("PiTU - Inicializando...")
    splash.geometry("600x400")
    splash.overrideredirect(True)  # Remove bordas

    # Centraliza a janela
    largura_tela = splash.winfo_screenwidth()
    altura_tela = splash.winfo_screenheight()
    largura_janela = 600
    altura_janela = 400
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    splash.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Carrega imagem splashscreen.png
    try:
        img = Image.open("splashscreen.png")
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label_img = ctk.CTkLabel(splash, image=img_tk, text="")
        label_img.pack(fill="both", expand=True)
    except FileNotFoundError:
        label_img = ctk.CTkLabel(splash, text="PiTU", font=("Arial", 32))
        label_img.pack(expand=True)

    # Fade-in e Fade-out
    def animacao():
        # Fade-in
        for i in range(0, 101, 5):
            splash.attributes("-alpha", i / 100)
            time.sleep(0.05)

        time.sleep(2)  # Mantém visível

        # Fade-out
        for i in range(100, -1, -5):
            splash.attributes("-alpha", i / 100)
            time.sleep(0.05)

        splash.destroy()
        abrir_pitu()

    threading.Thread(target=animacao, daemon=True).start()
    splash.mainloop()

def abrir_pitu():
    janela = ctk.CTk()
    janela.title("PiTU - Programa Principal")
    janela.geometry("1000x700")

    label = ctk.CTkLabel(janela, text="Bem-vindo ao PiTU!", font=("Arial", 28))
    label.pack(pady=20)

    # Aqui você adiciona os módulos do PiTU (botões, menus, etc.)
    # Exemplo:
    botao = ctk.CTkButton(janela, text="Abrir Calculador de Diretórios")
    botao.pack(pady=10)

    janela.mainloop()

# Inicia com Splash
mostrar_splash()