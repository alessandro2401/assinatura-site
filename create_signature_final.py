#!/usr/bin/env python3
"""
Script para criar assinatura de e-mail profissional para o GRUPO MMB - Versão Final
Design limpo, profissional e otimizado para e-mail
"""

from PIL import Image, ImageDraw
import os

# Dimensões da assinatura (padrão para e-mail)
WIDTH = 700
HEIGHT = 160

# Cores do GRUPO MMB
BG_COLOR = (255, 255, 255)  # Branco
PRIMARY_COLOR = (0, 32, 63)  # Azul escuro do logo MMB
DIVIDER_COLOR = (220, 220, 220)  # Cinza claro para divisória

def create_final_signature():
    """Cria a versão final da assinatura de e-mail"""
    
    # Criar imagem base
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # === LOGO PRINCIPAL ===
    logo_path = '/home/ubuntu/upload/LOGO_MMB.png'
    logo_x = 15
    logo_y = 20
    
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Redimensionar logo mantendo proporção
        logo_height = 110
        aspect_ratio = logo.width / logo.height
        logo_width = int(logo_height * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Colar logo no lado esquerdo
        img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)
        logo_end_x = logo_x + logo_width
    else:
        logo_end_x = logo_x + 250
    
    # === LINHA DIVISÓRIA ===
    divider_x = logo_end_x + 30
    draw.line([(divider_x, 15), (divider_x, HEIGHT - 15)], 
              fill=DIVIDER_COLOR, width=3)
    
    # === ÁREA DE LOGOS SECUNDÁRIOS ===
    secondary_start_x = divider_x + 30
    
    # Lista de logos secundários
    secondary_logos = [
        '/home/ubuntu/upload/logommbbranca.png',
        '/home/ubuntu/upload/logomotorcyclebranca.png',
        '/home/ubuntu/upload/logoalphabranca.png',
        '/home/ubuntu/upload/juntospodemosmaisbranca.png',
        '/home/ubuntu/upload/logopotereseguroautobranca.png',
        '/home/ubuntu/upload/logosolucoescorretorabranca.png',
    ]
    
    # Criar fundo escuro para logos brancos
    dark_bg_x = secondary_start_x - 15
    dark_bg_width = WIDTH - dark_bg_x - 15
    dark_bg_y = 10
    dark_bg_height = HEIGHT - 20
    
    # Desenhar retângulo com fundo escuro
    draw.rectangle(
        [(dark_bg_x, dark_bg_y), (WIDTH - 15, dark_bg_y + dark_bg_height)],
        fill=PRIMARY_COLOR
    )
    
    # === POSICIONAR LOGOS SECUNDÁRIOS ===
    # Grid 3x2 com espaçamento otimizado
    logo_size = 50
    logos_per_row = 3
    spacing_x = 20
    spacing_y = 15
    start_x = secondary_start_x
    start_y = 20
    
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
    
    # === SALVAR IMAGEM ===
    output_path = '/home/ubuntu/assinatura_email_mmb_final.png'
    img.save(output_path, 'PNG', quality=100, optimize=True)
    print(f"✓ Assinatura final criada: {output_path}")
    
    # Criar versão HTML
    create_html_signature(output_path)
    
    # Criar guia de uso
    create_usage_guide()
    
    return output_path

def create_html_signature(image_path):
    """Cria código HTML completo para a assinatura de e-mail"""
    
    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assinatura de E-mail - GRUPO MMB</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .signature-container {
            max-width: 700px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .signature {
            max-width: 700px;
            border: 1px solid #e0e0e0;
        }
        .signature img {
            display: block;
            max-width: 100%;
            height: auto;
        }
        .instructions {
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-left: 4px solid #00203f;
        }
        .instructions h3 {
            margin-top: 0;
            color: #00203f;
        }
        .instructions ol {
            padding-left: 20px;
        }
        .instructions li {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <div class="signature-container">
        <h2 style="color: #00203f; margin-top: 0;">Assinatura de E-mail - GRUPO MMB</h2>
        
        <div class="signature">
            <img src="assinatura_email_mmb_final.png" alt="GRUPO MMB - Assinatura de E-mail" />
        </div>
        
        <div class="instructions">
            <h3>Como usar esta assinatura:</h3>
            <ol>
                <li><strong>Gmail:</strong> Configurações → Geral → Assinatura → Inserir imagem</li>
                <li><strong>Outlook:</strong> Arquivo → Opções → Email → Assinaturas → Inserir imagem</li>
                <li><strong>Apple Mail:</strong> Preferências → Assinaturas → Arrastar imagem</li>
                <li><strong>Thunderbird:</strong> Configurações da conta → Inserir HTML</li>
            </ol>
            <p><strong>Dica:</strong> Para melhor compatibilidade, hospede a imagem online e use o link na assinatura.</p>
        </div>
    </div>
</body>
</html>"""
    
    html_path = '/home/ubuntu/assinatura_email_mmb_final.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML da assinatura criado: {html_path}")

def create_usage_guide():
    """Cria guia de uso da assinatura"""
    
    guide_content = """# Guia de Uso - Assinatura de E-mail GRUPO MMB

## Arquivos Gerados

1. **assinatura_email_mmb_final.png** - Imagem da assinatura (700x160px)
2. **assinatura_email_mmb_final.html** - Página HTML com preview e instruções
3. **guia_de_uso.md** - Este arquivo

## Como Configurar a Assinatura

### Gmail (Web)
1. Acesse Gmail → Configurações (ícone de engrenagem) → Ver todas as configurações
2. Vá para a aba "Geral"
3. Role até "Assinatura"
4. Clique em "Criar nova" e dê um nome
5. Clique no ícone de imagem e faça upload do arquivo PNG
6. Ajuste o tamanho se necessário
7. Role até o final e clique em "Salvar alterações"

### Outlook (Desktop)
1. Arquivo → Opções → Email
2. Clique em "Assinaturas..."
3. Clique em "Nova" e dê um nome
4. Clique no ícone de imagem e selecione o arquivo PNG
5. Clique em "OK" para salvar

### Outlook (Web)
1. Configurações (ícone de engrenagem) → Exibir todas as configurações do Outlook
2. Email → Redação e resposta
3. Role até "Assinatura de email"
4. Clique no ícone de imagem e faça upload do arquivo PNG
5. Clique em "Salvar"

### Apple Mail
1. Mail → Preferências → Assinaturas
2. Clique no "+" para criar nova assinatura
3. Dê um nome
4. Arraste o arquivo PNG para a área de assinatura
5. Feche a janela (salva automaticamente)

### Thunderbird
1. Ferramentas → Configurações da conta
2. Selecione a conta de email
3. Marque "Anexar a assinatura do arquivo a seguir"
4. Clique em "Escolher..." e selecione o arquivo PNG
5. Clique em "OK"

## Dicas Importantes

### Para Melhor Compatibilidade
- **Hospede a imagem online**: Faça upload da imagem para um servidor web e use o link
- **Tamanho ideal**: A assinatura tem 700x160px, ideal para e-mails
- **Formato**: PNG com fundo branco para melhor compatibilidade

### Hospedagem da Imagem
Você pode hospedar a imagem em:
- Google Drive (compartilhar publicamente)
- Dropbox (link público)
- Servidor web da empresa
- Serviços como Imgur ou ImgBB

### Código HTML para Assinatura (com link da imagem)
```html
<img src="URL_DA_IMAGEM_AQUI" alt="GRUPO MMB" width="700" height="160" />
```

Substitua `URL_DA_IMAGEM_AQUI` pelo link da imagem hospedada.

## Especificações Técnicas

- **Dimensões**: 700 x 160 pixels
- **Formato**: PNG
- **Qualidade**: Alta (100%)
- **Fundo**: Branco (#FFFFFF)
- **Cores principais**: Azul escuro (#00203F) do logo MMB
- **Logos incluídos**: 
  - Logo principal GRUPO MMB (esquerda)
  - 6 logos secundários (direita, fundo azul escuro)

## Suporte

Para dúvidas ou ajustes na assinatura, entre em contato com o departamento de TI ou Marketing.

---

**GRUPO MMB**  
*Mobilidade • Multiproteção • Benefícios*
"""
    
    guide_path = '/home/ubuntu/guia_de_uso.md'
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print(f"✓ Guia de uso criado: {guide_path}")

if __name__ == '__main__':
    create_final_signature()
    print("\n" + "="*60)
    print("✓ ASSINATURA DE E-MAIL CRIADA COM SUCESSO!")
    print("="*60)
    print("\nArquivos gerados:")
    print("  • assinatura_email_mmb_final.png")
    print("  • assinatura_email_mmb_final.html")
    print("  • guia_de_uso.md")
    print("\nAbra o arquivo HTML no navegador para ver o preview!")
