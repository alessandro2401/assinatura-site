# TODO - Gerador de Assinatura GRUPO MMB

## Features Planejadas

- [x] Configurar tema e cores corporativas do GRUPO MMB
- [x] Adicionar logo oficial do GRUPO MMB aos assets
- [x] Criar componente de formulário para dados do colaborador
- [x] Implementar preview da assinatura em tempo real
- [x] Incorporar logo em base64 no preview
- [x] Criar gerador de código HTML para assinatura
- [x] Adicionar botão para copiar código HTML
- [x] Implementar layout invertido (dados à esquerda, logo à direita)
- [x] Adicionar instruções de uso
- [x] Criar seção de exemplos
- [x] Otimizar responsividade para mobile
- [x] Testar em diferentes navegadores
- [x] Criar checkpoint antes da publicação
- [x] Publicar site permanentemente

## Novas Features Solicitadas

- [x] Adicionar botão para gerar assinatura como imagem PNG
- [x] Implementar funcionalidade de download da imagem
- [x] Adicionar opção de escolher qualidade/tamanho da imagem

## Bugs Reportados

- [x] Corrigir erro ao gerar imagem PNG em dispositivos móveis
- [x] Implementar solução alternativa mais robusta para download de imagem

## Novos Bugs

- [x] Corrigir geração de PNG com tamanho 0 bytes (problema no carregamento da logo)

## Correções Solicitadas

- [x] Alterar domínio do e-mail de .com.br para .com (grupommb.com)

## Nova Solicitação

- [x] Modificar download PNG para capturar exatamente o preview visual (com borda, fundo e estilo do card)
- [x] Substituir html2canvas por dom-to-image para melhor compatibilidade
- [x] Copiar logo para diretório public do projeto
- [x] Testar e confirmar download PNG funcionando perfeitamente

## Ajustes de Tamanho

- [x] Redimensionar preview para seguir diretrizes de assinatura de e-mail (300-600px largura, 70-200px altura)
- [x] Ajustar para aproximadamente 550 x 160 pixels

## Bug Crítico Reportado

- [x] Corrigir erro NotFoundError ao clicar em Baixar PNG
- [x] Adicionar melhor tratamento de erros na função downloadAsImage
- [x] Garantir que toast não cause conflito com React rendering

## Bug de Layout Reportado

- [x] Corrigir imagem PNG sendo cortada na direita (logo do GRUPO MMB cortada)
- [x] Reduzir espaço sobrando na esquerda
- [x] Ajustar largura do preview para capturar todo o conteúdo

## Problema de Qualidade da Logo

- [x] Logo do GRUPO MMB está espremida e com baixa qualidade
- [x] Aumentar espaço reservado para a logo (mínimo 150-180px)
- [x] Ajustar proporções para manter aspect ratio original
- [x] Garantir que logo apareça nítida e bem dimensionada

## Ajuste de Espaçamento da Logo

- [x] Logo ainda está espremida
- [x] Aumentar ainda mais o espaço reservado (200-220px)
- [x] Diminuir um pouco o tamanho da logo (70-80px altura)
- [x] Dar mais "respiro" visual à logo
