# Criar a janela principal
import tkinter as tk
from PIL import Image, ImageTk
from CMYK import CMYKEditorApp, compare_images, open_image_RGB

from TransformarExcelEmIMG import ImageEditorApp, open_image
from TransformarIMGparaExcel import IMGExcel, select_image_convert

from TonsCinza import ComparadorTonsCinza

def exibir_tons_cinza():
    global imagens_tk  # Mantendo uma referência global para as imagens para evitar a coleta de lixo prematura
    # Criar uma instância de ComparadorTonsCinza com o caminho da imagem desejada
    comparador = ComparadorTonsCinza("IMG/winx.png")
    # Gerar os tons de cinza
    tons_cinza = comparador.gerar_tons_cinza()
    
    # Converter as imagens para o formato suportado pelo Tkinter
    imagens_tk = [ImageTk.PhotoImage(imagem) for imagem in tons_cinza]

    # Exibir as imagens nos labels correspondentes
    panel1.config(image=imagens_tk[0])
    panel2.config(image=imagens_tk[1])
    panel3.config(image=imagens_tk[2])


# Inicializar a aplicação
root = tk.Tk()
root.title("Editor de Imagem")


# Barra de status para exibir a cor do pixel sob o cursor do mouse
status = tk.StringVar()
status_label = tk.Label(root, textvariable=status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

app = ImageEditorApp(root)
IMGExc = IMGExcel(root)
cmyk = CMYKEditorApp(root)


# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
root.config(menu=menu_bar)

panel = tk.Label(root)

# Botão para selecionar uma imagem
select_button = tk.Button(root, text="Gerar Excel", command=lambda:(select_image_convert(IMGExc), open_image(app)))
select_button.pack(side=tk.TOP)

compare_button = tk.Button(root, text="Comparar RGB e CMYK", command=lambda: (open_image_RGB(cmyk), compare_images(cmyk)))
compare_button.pack(side=tk.TOP)

# Botão para mostrar a imagem em tons de cinza
show_gray_image_button = tk.Button(root, text="Mostrar Imagem em Tons de Cinza", command=exibir_tons_cinza)
show_gray_image_button.pack(side=tk.TOP)


# Definir os labels onde as imagens serão exibidas
panel1 = tk.Label(root)
panel1.pack(side=tk.LEFT)

panel2 = tk.Label(root)
panel2.pack(side=tk.LEFT)


panel3 = tk.Label(root)
panel3.pack(side=tk.LEFT)


panel.pack()

root.status = status  # Para acessar a barra de status na classe ImageEditorApp

root.mainloop()