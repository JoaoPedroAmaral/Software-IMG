import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from AjusteBrilhoContraste import ImageAdjuster
from CMYK import CMYKEditorApp, compare_images, open_image_RGB
from TransformarExcelEmIMG import ImageEditorApp, open_image
from TransformarIMGparaExcel import IMGExcel, select_image_convert
from TonsCinza import ComparadorTonsCinza

def exibir_tons_cinza():
    global imagens_tk
    comparador = ComparadorTonsCinza("IMG/winx.png")
    tons_cinza = comparador.gerar_tons_cinza()
    imagens_tk = [ImageTk.PhotoImage(imagem) for imagem in tons_cinza]
    imagens_tk = [ImageTk.PhotoImage(imagem.resize((100, 100))) for imagem in tons_cinza]
    panel1.config(image=imagens_tk[0])
    panel2.config(image=imagens_tk[1])
    panel3.config(image=imagens_tk[2])
    
    imagem_panel1 = tons_cinza[0]
    imagem_panel1_resized = imagem_panel1.resize((200, 200))
    imagem_panel1_resized.save("IMG/cinza.png")
    
    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

root = tk.Tk()
root.title("Editor de Imagem")

# Definir o tamanho da janela
root.geometry("1000x600")  # Aumentei a altura da janela

# Criar uma frame principal para conter todos os elementos
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Barra de rolagem vertical
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Adicionar uma canvas para colocar os elementos e conectar com a barra de rolagem
canvas = tk.Canvas(main_frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Adicionar um frame para conter todos os elementos na canvas
content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

status = tk.StringVar()
status_label = tk.Label(content_frame, textvariable=status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

app = ImageEditorApp(content_frame)
IMGExc = IMGExcel(content_frame)
cmyk = CMYKEditorApp(content_frame)
ajuster = ImageAdjuster(content_frame, "IMG/winx.png")
ajuster = ImageAdjuster(content_frame, "IMG/cinza.png")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
root.config(menu=menu_bar)

select_button = tk.Button(content_frame, text="Gerar Excel", command=lambda:(select_image_convert(IMGExc), open_image(app)))
select_button.pack()

compare_button = tk.Button(content_frame, text="Comparar RGB e CMYK", command=lambda: (open_image_RGB(cmyk), compare_images(cmyk)))
compare_button.pack()

show_gray_image_button = tk.Button(content_frame, text="Mostrar Imagem em Tons de Cinza", command=exibir_tons_cinza)
show_gray_image_button.pack()

panel1 = tk.Label(content_frame)
panel1.pack(side=tk.LEFT)  # Movido o painel para o topo do frame

panel2 = tk.Label(content_frame)
panel2.pack(side=tk.LEFT)  # Movido o painel para o topo do frame

panel3 = tk.Label(content_frame)
panel3.pack(side=tk.LEFT)  # Movido o painel para o topo do frame

# Atualizar a geometria da canvas
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox(tk.ALL))

# Executar loop principal
root.mainloop()
