#!/usr/bin/env python3
"""
Criador de assinatura GRUPO MMB - Layout Invertido
Dados à esquerda, logo à direita (menor)
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 650
HEIGHT = 180
BG_COLOR = (255, 255, 255)
PRIMARY_COLOR = (0, 32, 63)
TEXT_COLOR = (68, 68, 68)
ACCENT_COLOR = (100, 149, 237)
DIVIDER_COLOR = (220, 220, 220)

def create_inverted_signature(nome, departamento, email, output_filename):
    """Cria assinatura com layout invertido - dados à esquerda, logo à direita"""
    
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # === ÁREA DE TEXTO (ESQUERDA) ===
    text_x = 25
    text_y = 35
    
    # Carregar fontes
    try:
        font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        font_dept = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        font_email = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
        font_slogan = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 11)
        font_icon = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        font_name = font_dept = font_email = font_slogan = font_icon = ImageFont.load_default()
    
    # Nome
    draw.text((text_x, text_y), nome, fill=PRIMARY_COLOR, font=font_name)
    
    # Departamento
    draw.text((text_x, text_y + 40), departamento, fill=TEXT_COLOR, font=font_dept)
    
    # Linha decorativa com gradiente
    line_y = text_y + 75
    line_width = 220
    for i in range(line_width):
        color = (
            ACCENT_COLOR[0] + (255 - ACCENT_COLOR[0]) * i // line_width,
            ACCENT_COLOR[1] + (255 - ACCENT_COLOR[1]) * i // line_width,
            ACCENT_COLOR[2] + (255 - ACCENT_COLOR[2]) * i // line_width
        )
        draw.line([(text_x + i, line_y), (text_x + i, line_y + 2)], fill=color, width=1)
    
    # E-mail com ícone
    email_y = text_y + 90
    draw.text((text_x, email_y), "✉", fill=ACCENT_COLOR, font=font_icon)
    draw.text((text_x + 28, email_y + 3), email, fill=TEXT_COLOR, font=font_email)
    
    # Slogan
    slogan_y = HEIGHT - 30
    draw.text((text_x, slogan_y), "Mobilidade • Multiproteção • Benefícios", 
              fill=(150, 150, 150), font=font_slogan)
    
    # === DIVISÓRIA (CENTRO) ===
    text_end_x = text_x + 350  # Fim aproximado da área de texto
    divider_x = text_end_x + 20
    draw.line([(divider_x, 25), (divider_x, HEIGHT - 25)], 
              fill=DIVIDER_COLOR, width=3)
    
    # === LOGO (DIREITA - MENOR) ===
    logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
    logo_start_x = divider_x + 25
    
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Logo menor - 80px de altura
        logo_height = 80
        aspect_ratio = logo.width / logo.height
        logo_width = int(logo_height * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Centralizar verticalmente
        logo_y = (HEIGHT - logo_height) // 2
        
        # Centralizar horizontalmente na área disponível
        available_width = WIDTH - logo_start_x - 25
        logo_x = logo_start_x + (available_width - logo_width) // 2
        
        img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)
    
    # Salvar
    img.save(output_filename, 'PNG', quality=100, optimize=True)
    return output_filename

def create_all_inverted_examples():
    """Cria todos os exemplos com layout invertido"""
    
    examples = [
        {
            "nome": "Alessandro Marques",
            "departamento": "CEO - Chief Executive Officer",
            "email": "alessandro.marques@grupommb.com.br",
            "file": "assinatura_invertida_ceo.png"
        },
        {
            "nome": "João Silva",
            "departamento": "Diretor Comercial",
            "email": "joao.silva@grupommb.com.br",
            "file": "assinatura_invertida_diretor.png"
        },
        {
            "nome": "Maria Santos",
            "departamento": "Gerente de Marketing",
            "email": "maria.santos@grupommb.com.br",
            "file": "assinatura_invertida_gerente.png"
        },
        {
            "nome": "Carlos Oliveira",
            "departamento": "Analista de TI",
            "email": "carlos.oliveira@grupommb.com.br",
            "file": "assinatura_invertida_analista.png"
        },
        {
            "nome": "Ana Paula Costa",
            "departamento": "Coordenadora de RH",
            "email": "ana.costa@grupommb.com.br",
            "file": "assinatura_invertida_coordenadora.png"
        }
    ]
    
    print("="*70)
    print("CRIANDO ASSINATURAS INVERTIDAS - GRUPO MMB")
    print("Layout: Dados à esquerda | Logo à direita (menor)")
    print("="*70)
    print()
    
    created_files = []
    
    for ex in examples:
        output_path = f'/home/ubuntu/{ex["file"]}'
        create_inverted_signature(
            ex["nome"],
            ex["departamento"],
            ex["email"],
            output_path
        )
        created_files.append(output_path)
        print(f"✓ {ex['nome']:30} → {ex['file']}")
    
    # Criar template em branco
    template_path = '/home/ubuntu/assinatura_invertida_template.png'
    create_inverted_signature(
        "Nome do Colaborador",
        "Departamento do Colaborador",
        "email@grupommb.com.br",
        template_path
    )
    created_files.append(template_path)
    print(f"✓ {'Template':30} → assinatura_invertida_template.png")
    
    print()
    print("="*70)
    print(f"✓ {len(created_files)} ASSINATURAS INVERTIDAS CRIADAS COM SUCESSO!")
    print("="*70)
    
    return created_files

if __name__ == '__main__':
    create_all_inverted_examples()
