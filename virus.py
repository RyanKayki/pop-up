import tkinter as tk

def abrir_janela():
    nova_janela = tk.Toplevel(janela_principal)
    nova_janela.title("Janela Secundária")
    nova_janela.geometry("200x100")
    tk.Label(nova_janela, text="Vocë foi Hackeado, uga uga").pack(pady=20)
    nova_janela.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(nova_janela))

def fechar_janela(janela):
    janela.withdraw()  # Minimiza a janela
    abrir_janela()

# Configuração da janela principal
janela_principal = tk.Tk()
janela_principal.title("Minigame de Janelas")
janela_principal.geometry("400x200")

# Botão para abrir a janela secundária
botao_abrir = tk.Button(janela_principal, text="Abrir Janela", width=15, height=2, command=abrir_janela)
botao_abrir.pack(pady=20)

janela_principal.mainloop()
