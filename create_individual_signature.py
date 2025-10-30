#!/usr/bin/env python3
"""
Script para criar assinatura de e-mail individual para colaboradores do GRUPO MMB
Design profissional com logo e informações do colaborador
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dimensões da assinatura
WIDTH = 600
HEIGHT = 180

# Cores do GRUPO MMB
BG_COLOR = (255, 255, 255)  # Branco
PRIMARY_COLOR = (0, 32, 63)  # Azul escuro do logo MMB
TEXT_COLOR = (60, 60, 60)  # Cinza escuro para texto
ACCENT_COLOR = (100, 149, 237)  # Azul mais claro para detalhes
DIVIDER_COLOR = (200, 200, 200)  # Cinza claro

def create_individual_signature(nome="Nome do Colaborador", 
                                departamento="Departamento do Colaborador",
                                email="email@grupommb.com.br"):
    """Cria assinatura individual com informações do colaborador"""
    
    # Criar imagem base
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # === CARREGAR LOGO ===
    logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
    logo_x = 20
    logo_y = 30
    
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Redimensionar logo
        logo_height = 100
        aspect_ratio = logo.width / logo.height
        logo_width = int(logo_height * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Colar logo
        img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)
        logo_end_x = logo_x + logo_width
    else:
        logo_end_x = 200
    
    # === LINHA DIVISÓRIA VERTICAL ===
    divider_x = logo_end_x + 30
    draw.line([(divider_x, 25), (divider_x, HEIGHT - 25)], 
              fill=DIVIDER_COLOR, width=2)
    
    # === ÁREA DE TEXTO ===
    text_start_x = divider_x + 30
    text_start_y = 40
    
    # Tentar usar fontes do sistema
    try:
        font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_dept = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        font_email = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        # Fallback para fonte padrão
        font_name = ImageFont.load_default()
        font_dept = ImageFont.load_default()
        font_email = ImageFont.load_default()
    
    # === DESENHAR TEXTOS ===
    
    # Nome (em negrito, azul escuro)
    draw.text((text_start_x, text_start_y), nome, 
              fill=PRIMARY_COLOR, font=font_name)
    
    # Departamento (cinza escuro)
    draw.text((text_start_x, text_start_y + 35), departamento, 
              fill=TEXT_COLOR, font=font_dept)
    
    # Linha decorativa
    line_y = text_start_y + 65
    draw.line([(text_start_x, line_y), (text_start_x + 200, line_y)], 
              fill=ACCENT_COLOR, width=2)
    
    # E-mail (com ícone simulado)
    email_y = text_start_y + 75
    draw.text((text_start_x, email_y), "✉", fill=ACCENT_COLOR, font=font_name)
    draw.text((text_start_x + 25, email_y + 2), email, 
              fill=TEXT_COLOR, font=font_email)
    
    # === RODAPÉ COM SLOGAN ===
    slogan_y = HEIGHT - 30
    try:
        font_slogan = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except:
        font_slogan = ImageFont.load_default()
    
    slogan = "Mobilidade • Multiproteção • Benefícios"
    draw.text((text_start_x, slogan_y), slogan, 
              fill=(150, 150, 150), font=font_slogan)
    
    # === SALVAR ===
    output_path = '/home/ubuntu/assinatura_individual_template.png'
    img.save(output_path, 'PNG', quality=95, optimize=True)
    print(f"✓ Assinatura individual criada: {output_path}")
    
    return output_path

def create_example_signatures():
    """Cria exemplos de assinaturas com diferentes perfis"""
    
    examples = [
        {
            "nome": "João Silva",
            "departamento": "Diretor Comercial",
            "email": "joao.silva@grupommb.com.br",
            "filename": "exemplo_diretor.png"
        },
        {
            "nome": "Maria Santos",
            "departamento": "Gerente de Marketing",
            "email": "maria.santos@grupommb.com.br",
            "filename": "exemplo_gerente.png"
        },
        {
            "nome": "Carlos Oliveira",
            "departamento": "Analista de TI",
            "email": "carlos.oliveira@grupommb.com.br",
            "filename": "exemplo_analista.png"
        }
    ]
    
    for ex in examples:
        img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)
        
        # Logo
        logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            logo_height = 100
            aspect_ratio = logo.width / logo.height
            logo_width = int(logo_height * aspect_ratio)
            logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
            img.paste(logo, (20, 30), logo if logo.mode == 'RGBA' else None)
            logo_end_x = 20 + logo_width
        else:
            logo_end_x = 200
        
        divider_x = logo_end_x + 30
        draw.line([(divider_x, 25), (divider_x, HEIGHT - 25)], 
                  fill=DIVIDER_COLOR, width=2)
        
        text_start_x = divider_x + 30
        text_start_y = 40
        
        try:
            font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
            font_dept = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            font_email = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            font_slogan = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        except:
            font_name = font_dept = font_email = font_slogan = ImageFont.load_default()
        
        # Textos
        draw.text((text_start_x, text_start_y), ex["nome"], 
                  fill=PRIMARY_COLOR, font=font_name)
        draw.text((text_start_x, text_start_y + 35), ex["departamento"], 
                  fill=TEXT_COLOR, font=font_dept)
        
        line_y = text_start_y + 65
        draw.line([(text_start_x, line_y), (text_start_x + 200, line_y)], 
                  fill=ACCENT_COLOR, width=2)
        
        email_y = text_start_y + 75
        draw.text((text_start_x, email_y), "✉", fill=ACCENT_COLOR, font=font_name)
        draw.text((text_start_x + 25, email_y + 2), ex["email"], 
                  fill=TEXT_COLOR, font=font_email)
        
        slogan_y = HEIGHT - 30
        slogan = "Mobilidade • Multiproteção • Benefícios"
        draw.text((text_start_x, slogan_y), slogan, 
                  fill=(150, 150, 150), font=font_slogan)
        
        output_path = f'/home/ubuntu/{ex["filename"]}'
        img.save(output_path, 'PNG', quality=95, optimize=True)
        print(f"✓ Exemplo criado: {ex['filename']}")

if __name__ == '__main__':
    print("="*60)
    print("CRIANDO ASSINATURAS INDIVIDUAIS - GRUPO MMB")
    print("="*60)
    
    # Criar template
    create_individual_signature()
    
    # Criar exemplos
    print("\nCriando exemplos com diferentes perfis...")
    create_example_signatures()
    
    print("\n" + "="*60)
    print("✓ ASSINATURAS CRIADAS COM SUCESSO!")
    print("="*60)
