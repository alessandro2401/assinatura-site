#!/usr/bin/env python3
"""
Script para criar assinatura de e-mail profissional para o GRUPO MMB - Versão 2
Com design mais limpo e profissional
"""

from PIL import Image, ImageDraw
import os

# Dimensões da assinatura (padrão para e-mail)
WIDTH = 650
HEIGHT = 180

# Cores do GRUPO MMB
BG_COLOR = (255, 255, 255)  # Branco
PRIMARY_COLOR = (0, 32, 63)  # Azul escuro do logo MMB
DIVIDER_COLOR = (200, 200, 200)  # Cinza claro para divisória

def create_email_signature_v2():
    """Cria a imagem da assinatura de e-mail versão 2"""
    
    # Criar imagem base
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Carregar logo principal
    logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
    logo_x = 20
    logo_y = 30
    
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Redimensionar logo mantendo proporção
        logo_height = 100
        aspect_ratio = logo.width / logo.height
        logo_width = int(logo_height * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Colar logo no lado esquerdo
        img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)
        logo_end_x = logo_x + logo_width
    else:
        logo_end_x = logo_x + 200
    
    # Adicionar linha divisória vertical
    divider_x = logo_end_x + 25
    draw.line([(divider_x, 20), (divider_x, HEIGHT - 20)], 
              fill=DIVIDER_COLOR, width=2)
    
    # Área para logos secundários
    secondary_start_x = divider_x + 25
    
    # Carregar e posicionar logos secundários em grid compacto
    secondary_logos = [
        '/home/ubuntu/upload/logommbbranca.png',
        '/home/ubuntu/upload/logomotorcyclebranca.png',
        '/home/ubuntu/upload/logoalphabranca.png',
        '/home/ubuntu/upload/juntospodemosmaisbranca.png',
        '/home/ubuntu/upload/logopotereseguroautobranca.png',
        '/home/ubuntu/upload/logosolucoescorretorabranca.png',
    ]
    
    # Criar fundo escuro para logos brancos
    dark_bg_x = secondary_start_x - 10
    dark_bg_width = WIDTH - dark_bg_x - 10
    dark_bg_y = 15
    dark_bg_height = HEIGHT - 30
    
    # Desenhar retângulo com cantos arredondados (simulado)
    draw.rectangle(
        [(dark_bg_x, dark_bg_y), (WIDTH - 10, dark_bg_y + dark_bg_height)],
        fill=PRIMARY_COLOR
    )
    
    # Posicionar logos secundários em grid 3x2
    logo_size = 45
    logos_per_row = 3
    spacing_x = 15
    spacing_y = 12
    start_x = secondary_start_x + 5
    start_y = 25
    
    for idx, logo_path in enumerate(secondary_logos):
        if os.path.exists(logo_path):
            try:
                sec_logo = Image.open(logo_path)
                
                # Redimensionar mantendo proporção
                sec_logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
                
                row = idx // logos_per_row
                col = idx % logos_per_row
                
                x = start_x + col * (logo_size + spacing_x)
                y = start_y + row * (logo_size + spacing_y)
                
                # Centralizar logo na célula
                x_offset = (logo_size - sec_logo.width) // 2
                y_offset = (logo_size - sec_logo.height) // 2
                
                img.paste(sec_logo, (x + x_offset, y + y_offset), 
                         sec_logo if sec_logo.mode == 'RGBA' else None)
            except Exception as e:
                print(f"Erro ao processar {logo_path}: {e}")
    
    # Salvar imagem
    output_path = '/home/ubuntu/assinatura_email_mmb_v2.png'
    img.save(output_path, 'PNG', quality=95, optimize=True)
    print(f"Assinatura v2 criada com sucesso: {output_path}")
    
    # Criar também versão HTML para uso em e-mail
    create_html_signature(output_path)
    
    return output_path

def create_html_signature(image_path):
    """Cria código HTML para a assinatura de e-mail"""
    
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .signature { max-width: 650px; }
        .signature img { display: block; max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <div class="signature">
        <img src="assinatura_email_mmb_v2.png" alt="GRUPO MMB - Assinatura de E-mail" />
    </div>
</body>
</html>"""
    
    html_path = '/home/ubuntu/assinatura_email_mmb.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML da assinatura criado: {html_path}")

if __name__ == '__main__':
    create_email_signature_v2()
