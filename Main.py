# Criar a janela principal
import tkinter as tk
from TransformarIMGparaExcel import select_image


root = tk.Tk()
root.title("Selecione uma imagem pequena pelo amor de Deus!")
#setta um novo formato 300 por 100
root.geometry("700x700")

# Botão para selecionar uma imagem
select_button = tk.Button(root, text="Gerar Excel", command=select_image)
select_button.pack(pady=20)

# Executar o loop principal da interface gráfica
root.mainloop() #função do TK tlgd

#Se o arquivo for grande essa porra demora para cacete!