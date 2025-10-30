#!/usr/bin/env python3
"""
Script para criar assinatura de e-mail profissional para o GRUPO MMB
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dimensões da assinatura (padrão para e-mail)
WIDTH = 600
HEIGHT = 200

# Cores do GRUPO MMB (azul escuro do logo)
BG_COLOR = (255, 255, 255)  # Branco
PRIMARY_COLOR = (0, 32, 63)  # Azul escuro do logo MMB
SECONDARY_COLOR = (100, 100, 100)  # Cinza para texto secundário

def create_email_signature():
    """Cria a imagem da assinatura de e-mail"""
    
    # Criar imagem base
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Carregar logo principal
    logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Redimensionar logo mantendo proporção
        logo_height = 120
        aspect_ratio = logo.width / logo.height
        logo_width = int(logo_height * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Colar logo no lado esquerdo
        logo_x = 20
        logo_y = (HEIGHT - logo_height) // 2
        img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)
    
    # Carregar e posicionar logos secundários
    secondary_logos = [
        '/home/ubuntu/upload/logommbbranca.png',
        '/home/ubuntu/upload/logomotorcyclebranca.png',
        '/home/ubuntu/upload/logoalphabranca.png',
        '/home/ubuntu/upload/juntospodemosmaisbranca.png',
        '/home/ubuntu/upload/logopotereseguroautobranca.png',
        '/home/ubuntu/upload/logosolucoescorretorabranca.png',
    ]
    
    # Criar fundo escuro para logos brancos
    dark_bg_x = 320
    dark_bg_width = WIDTH - dark_bg_x - 20
    draw.rectangle(
        [(dark_bg_x, 20), (WIDTH - 20, HEIGHT - 20)],
        fill=PRIMARY_COLOR
    )
    
    # Posicionar logos secundários em grid
    logo_size = 50
    logos_per_row = 3
    spacing = 10
    start_x = dark_bg_x + 15
    start_y = 30
    
    for idx, logo_path in enumerate(secondary_logos):
        if os.path.exists(logo_path):
            try:
                sec_logo = Image.open(logo_path)
                # Redimensionar mantendo proporção
                sec_logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
                
                row = idx // logos_per_row
                col = idx % logos_per_row
                
                x = start_x + col * (logo_size + spacing)
                y = start_y + row * (logo_size + spacing)
                
                # Centralizar logo na célula
                x_offset = (logo_size - sec_logo.width) // 2
                y_offset = (logo_size - sec_logo.height) // 2
                
                img.paste(sec_logo, (x + x_offset, y + y_offset), 
                         sec_logo if sec_logo.mode == 'RGBA' else None)
            except Exception as e:
                print(f"Erro ao processar {logo_path}: {e}")
    
    # Adicionar linha divisória
    draw.line([(dark_bg_x - 10, 20), (dark_bg_x - 10, HEIGHT - 20)], 
              fill=PRIMARY_COLOR, width=2)
    
    # Salvar imagem
    output_path = '/home/ubuntu/assinatura_email_mmb.png'
    img.save(output_path, 'PNG', quality=95)
    print(f"Assinatura criada com sucesso: {output_path}")
    
    return output_path

if __name__ == '__main__':
    create_email_signature()
