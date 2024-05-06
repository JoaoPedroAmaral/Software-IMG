# Criar a janela principal
import tkinter as tk
from PIL import Image, ImageTk
from CMYK import CMYKEditorApp, compare_images, open_image_RGB
from TransformarExcelEmIMG import ImageEditorApp, open_image
from TransformarIMGparaExcel import IMGExcel, select_image_convert

# Função para comparar RGB e CMYK
def compare_rgb_cmyk():
    if app.selected_color:
        rgb_color = app.selected_color
        cmyk_color = cmyk.rgb_para_cmyk(rgb_color)

# Função para exibir a imagem em tons de cinza
def show_gray_image(img_path, img_label):
    # Carregar a imagem em tons de cinza
    gray_image = Image.open(img_path).convert("L")  # Converter para escala de cinza
    # Converter a imagem para o formato suportado pelo Tkinter
    gray_image_tk = ImageTk.PhotoImage(gray_image)
    # Exibir a imagem em um widget de imagem na interface
    img_label.config(image=gray_image_tk)
    img_label.image = gray_image_tk  # Manter uma referência para evitar a coleta de lixo
    # Atualizar o widget de imagem
    img_label.update_idletasks()

# Função para gerar as três versões da imagem em tons de cinza
def generate_gray_images(img_path):
    gray_images = []

    # 1° tom: Converter para tons de cinza usando o método médio (R+G+B dividido por 3)
    gray_image_avg = Image.open(img_path).convert("L")  # Converter para escala de cinza
    gray_images.append(gray_image_avg)

    # 2° tom: Converter para tons de cinza usando o método máximo (maior valor entre R, G e B)
    rgb_image = Image.open(img_path)
    gray_image_max = rgb_image.split()[0].point(lambda x: max(x))  # Encontrar o máximo entre os canais RGB
    gray_images.append(gray_image_max)

    # 3° tom: Converter para tons de cinza usando pesos personalizados (xR + yG + zB)
    # Aqui, você pode definir seus próprios pesos x, y e z e calcular a soma ponderada dos canais RGB
    # Exemplo: x = 0.3, y = 0.59, z = 0.11 (valores padrão para conversão para tons de cinza)
    gray_image_custom = rgb_image.convert("L", matrix=(0.3, 0.59, 0.11, 0))  # Aplicar pesos personalizados
    gray_images.append(gray_image_custom)

    return gray_images

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

# Botão para mostrar a imagem em tons de cinza
show_gray_image_button = tk.Button(root, text="Mostrar Imagem em Tons de Cinza", command=lambda: show_gray_image("IMG\\winx.png", panel))
show_gray_image_button.pack(pady=5)

panel.pack()

root.status = status  # Para acessar a barra de status na classe ImageEditorApp

root.mainloop()