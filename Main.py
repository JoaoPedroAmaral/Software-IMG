# Criar a janela principal
import tkinter as tk
from CMYK import CMYKEditorApp, compare_images, open_image_RGB
from TransformarExcelEmIMG import ImageEditorApp, open_image
from TransformarIMGparaExcel import IMGExcel, select_image_convert

# Função para comparar RGB e CMYK
def compare_rgb_cmyk():
    if app.selected_color:
        rgb_color = app.selected_color
        cmyk_color = cmyk.rgb_para_cmyk(rgb_color)


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
file_menu.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
root.config(menu=menu_bar)

panel = tk.Label(root)

# Botão para selecionar uma imagem
select_button = tk.Button(root, text="Gerar Excel", command=lambda:(select_image_convert(IMGExc), open_image(app)))
select_button.pack(pady=5)

compare_button = tk.Button(root, text="Comparar RGB e CMYK", command=lambda: (open_image_RGB(cmyk), compare_images(cmyk)))
compare_button.pack(pady=5)

root.status = status  # Para acessar a barra de status na classe ImageEditorApp

root.mainloop()


