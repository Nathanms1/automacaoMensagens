# Envio de Mensagens via WhatsApp

Este é um aplicativo web desenvolvido com **Streamlit**, **Python**, e a biblioteca **pywhatkit** para enviar mensagens automaticamente via WhatsApp. O usuário pode carregar uma planilha de números de telefone e enviar uma mensagem personalizada para os contatos listados.

## Funcionalidades

- **Envio automático de mensagens**: Envia mensagens automaticamente para números listados em um arquivo Excel.
- **Formatação de mensagens**: Permite que você insira mensagens com formatação simples, como negrito e itálico.
- **Facilidade de uso**: A interface do usuário é simples e intuitiva, sem necessidade de configuração complexa.

## Requisitos

Antes de rodar o projeto localmente ou implantá-lo, você precisa garantir que tenha as seguintes dependências instaladas:

- **Python 3.x**
- **Bibliotecas**:
    - `streamlit`
    - `pandas`
    - `pywhatkit`
    - `tqdm`
    - `openpyxl`

Para instalar as dependências, você pode usar o comando:

```bash
pip install -r requirements.txt
