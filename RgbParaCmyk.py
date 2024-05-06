def rgb_para_cmyk(rgb_color):
    # Normaliza os valores RGB
    r, g, b = [x / 255.0 for x in rgb_color]
    
    # Calcula os valores CMY
    c = 1 - r
    m = 1 - g
    y = 1 - b
    
    # Calcula o valor K
    k = min(c, m, y)
    
    # Evita a divisão por zero
    if k == 1:
        cmyk_color = [0, 0, 0, 1]
    else:
        cmyk_color = [(c - k) / (1 - k), (m - k) / (1 - k), (y - k) / (1 - k), k]
    
    return [int(x * 100) for x in cmyk_color]  # Escala os valores CMYK para o intervalo de 0 a 100
