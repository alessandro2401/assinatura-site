# Resumo das Capacidades do Conector Canva MCP

## Visão Geral

O conector Canva MCP oferece integração completa com a plataforma Canva através de **17 ferramentas** que permitem gerenciar designs, pastas, comentários e exportações de forma programática.

---

## Categorias de Funcionalidades

### 📁 **1. Gerenciamento de Designs**

#### **search-designs**
Busca designs (documentos, apresentações, vídeos, whiteboards, planilhas) no Canva.

**Parâmetros principais:**
- `query`: Termo de busca para filtrar por título ou conteúdo
- `ownership`: Filtrar por propriedade (`any`, `owned`, `shared`)
- `sort_by`: Ordenação (`relevance`, `modified_descending`, `modified_ascending`, `title_descending`, `title_ascending`)
- `continuation`: Token para paginação

**Retorna:** Lista de designs com ID, título, thumbnail, URLs, datas e contagem de páginas.

---

#### **get-design**
Obtém informações detalhadas sobre um design específico.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)

**Retorna:** Detalhes completos incluindo proprietário, thumbnail, URLs de edição/visualização, timestamps e número de páginas.

---

#### **get-design-pages**
Lista as páginas de um design (apresentações, por exemplo).

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `offset`: Número de páginas a pular (paginação)
- `limit`: Número máximo de páginas a retornar

**Retorna:** Array de páginas com índice e thumbnail de cada uma.

---

#### **get-design-content**
Extrai o conteúdo de texto de um design.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `content_types`: Tipos de conteúdo a recuperar (atualmente apenas `richtexts`)
- `pages`: Array opcional de números de página

**Retorna:** Conteúdo textual do design.

**Nota:** Para edição, use `start-editing-transaction` em vez desta ferramenta.

---

### 📤 **2. Exportação de Designs**

#### **get-export-formats**
Verifica os formatos de exportação disponíveis para um design.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)

**Retorna:** Lista de formatos suportados (PDF, JPG, PNG, PPTX, GIF, MP4).

**Uso recomendado:** Sempre chamar antes de `export-design` para garantir compatibilidade.

---

#### **export-design**
Exporta um design para vários formatos.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `format`: Objeto com configurações de formato
  - `type`: Formato desejado (pdf, jpg, png, pptx, gif, mp4)
  - `pages`: Páginas específicas a exportar (opcional)
  - `width`, `height`: Dimensões para imagens
  - `transparent_background`: Fundo transparente (PNG)
  - `export_quality`: Qualidade (`regular` ou `pro`)

**Retorna:** URL de download do arquivo exportado.

**Importante:** Sempre exibir a URL de download ao usuário.

---

### 🗂️ **3. Gerenciamento de Pastas**

#### **list-folder-items**
Lista itens em uma pasta do Canva.

**Parâmetros principais:**
- `folder_id`: ID da pasta (use `root` para pasta raiz)
- `item_types`: Filtrar por tipo (`design`, `folder`, `image`)
- `sort_by`: Ordenação dos resultados
- `continuation`: Token para paginação

**Retorna:** Array de itens (designs, pastas ou imagens) com metadados completos.

---

#### **create-folder**
Cria uma nova pasta no Canva.

**Parâmetros principais:**
- `parent_folder_id`: ID da pasta pai (use `root` para nível superior)
- `name`: Nome da pasta (obrigatório)

**Retorna:** Detalhes da pasta criada incluindo ID e URL.

---

#### **move-item-to-folder**
Move itens (designs, pastas, imagens) para uma pasta específica.

**Parâmetros principais:**
- `item_id`: ID do item a mover (obrigatório)
- `to_folder_id`: ID da pasta de destino (use `root` para mover para o nível superior)

**Retorna:** Confirmação da movimentação.

---

### 💬 **4. Comentários e Colaboração**

#### **comment-on-design**
Adiciona um comentário a um design.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `message_plaintext`: Texto do comentário (obrigatório)

**Retorna:** Confirmação do comentário adicionado.

**Visibilidade:** O comentário será visível para todos os usuários com acesso ao design.

---

#### **list-comments**
Lista comentários de um design específico.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `comment_resolution`: Filtrar por status (`resolved` ou `unresolved`)
- `limit`: Número máximo de comentários (1-100, padrão 50)
- `continuation`: Token para paginação

**Retorna:** Lista de comentários com metadados.

---

#### **list-replies**
Lista respostas de um comentário específico.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `comment_id`: ID do comentário (obrigatório)

**Retorna:** Array de respostas ao comentário.

---

#### **reply-to-comment**
Responde a um comentário existente.

**Parâmetros principais:**
- `design_id`: ID do design (obrigatório)
- `comment_id`: ID do comentário (obrigatório)
- `message_plaintext`: Texto da resposta (obrigatório)

**Retorna:** Confirmação da resposta adicionada.

---

### 📥 **5. Importação e Upload**

#### **import-design-from-url**
Importa um arquivo de uma URL como um novo design do Canva.

**Parâmetros principais:**
- `url`: URL do arquivo a importar (obrigatório)
- `name`: Nome para o novo design (obrigatório)

**Retorna:** Detalhes do design importado.

---

#### **upload-asset-from-url**
Faz upload de um asset (imagem, vídeo) de uma URL para o Canva.

**Parâmetros principais:**
- `url`: URL do asset (obrigatório)
- `name`: Nome para o asset (obrigatório)

**Retorna:** Confirmação do upload.

**Nota:** Se retornar erro de "Missing scopes: [asset:write]", o usuário precisa desconectar e reconectar o conector para obter o escopo necessário.

---

### 🤖 **6. Geração com IA**

#### **generate-design**
Gera designs usando IA.

**Parâmetros principais:**
- `query`: Descrição do design a gerar (obrigatório)

**Retorna:** IDs de candidatos de design gerados.

**Requisito:** Requer plano Canva Pro.

**Importante:** Traduzir todos os parâmetros e queries para inglês antes de chamar.

---

#### **create-design-from-candidate**
Converte um candidato de design gerado por IA em um design editável.

**Parâmetros principais:**
- `candidate_id`: ID do candidato retornado por `generate-design` (obrigatório)

**Retorna:** Resumo do design com `design_id` que pode ser usado com ferramentas de edição.

**Fluxo:** `generate-design` → `create-design-from-candidate` → ferramentas de edição

---

## Considerações Importantes

### 🔐 **Autenticação**
- A autenticação OAuth é acionada automaticamente quando necessário
- Alguns recursos podem exigir reconexão para obter escopos adicionais

### 🌐 **Tradução**
- **Sempre traduzir parâmetros e queries para inglês** antes de chamar ferramentas de geração de IA
- Ferramentas de busca e gerenciamento funcionam com qualquer idioma

### 📄 **Formatos de Exportação**
- Sempre usar `get-export-formats` antes de `export-design`
- Formatos disponíveis variam por tipo de design

### 🔄 **Paginação**
- Muitas ferramentas suportam paginação via token `continuation`
- Use o token retornado para obter a próxima página de resultados

### 🎨 **Edição de Designs**
- Para edição, use `start-editing-transaction` (não testado nesta demonstração)
- `get-design-content` é apenas para leitura

---

## Casos de Uso Práticos

### 1. **Buscar e Exportar um Design**
```
1. search-designs → encontrar design
2. get-export-formats → verificar formatos
3. export-design → exportar para PDF/PNG/etc
```

### 2. **Organizar Designs em Pastas**
```
1. create-folder → criar nova pasta
2. search-designs → encontrar designs
3. move-item-to-folder → mover para a pasta
```

### 3. **Colaboração em Designs**
```
1. search-designs → encontrar design
2. comment-on-design → adicionar comentário
3. list-comments → ver comentários existentes
4. reply-to-comment → responder comentários
```

### 4. **Criar Design com IA**
```
1. generate-design → gerar candidatos
2. create-design-from-candidate → converter em design editável
3. export-design → exportar resultado
```

### 5. **Importar e Organizar Assets**
```
1. upload-asset-from-url → fazer upload de imagem
2. import-design-from-url → importar documento
3. create-folder → criar pasta organizacional
4. move-item-to-folder → organizar itens
```

---

## Limitações Conhecidas

- `get-design-content` suporta apenas `richtexts` atualmente
- `get-design-pages` não funciona com designs sem páginas (ex: Canva Docs)
- Geração de IA requer plano Canva Pro
- Alguns recursos podem exigir escopos adicionais de API

---

## Conclusão

O conector Canva MCP oferece uma **API completa e robusta** para automação de workflows de design, permitindo:

- ✅ Busca e gerenciamento de designs
- ✅ Exportação em múltiplos formatos
- ✅ Organização com pastas
- ✅ Colaboração via comentários
- ✅ Importação de assets externos
- ✅ Geração de designs com IA

Todas as ferramentas testadas funcionaram perfeitamente, retornando dados estruturados e completos em formato JSON.
