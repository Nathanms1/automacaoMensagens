import pandas as pd
import pywhatkit as kit
import time
import streamlit as st
from tqdm import tqdm  # Para a barra de progresso

# Título do Aplicativo
st.title("Envio de Mensagens via WhatsApp")

# Exemplo de planilha
st.markdown("""
    Para facilitar, você pode usar a planilha de exemplo. Clique no botão abaixo para ser redirecionado para o link da planilha.
""")

# Botão para abrir a planilha em uma nova guia
st.markdown("""
    <a href="https://docs.google.com/spreadsheets/d/1YtraQZwNrjoOo9BE1jNi3EAQjO_dQrR-KHtDr_oLkWQ/edit?usp=sharing" target="_blank">
        <button style="font-size: 16px; padding: 10px 20px; margin:0 0 30px 0; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">Acessar Planilha de Exemplo</button>
    </a>
""", unsafe_allow_html=True)

# Upload do arquivo Excel
arquivo = st.file_uploader("Carregar o arquivo Excel com números", type=["xlsx"])

# Campo de texto para a mensagem
mensagem = st.text_area("Digite a mensagem que deseja enviar")

# Alerta para garantir que o WhatsApp Web esteja aberto
st.warning("Certifique-se de que o WhatsApp Web esteja aberto e visível no navegador antes de iniciar o envio.")

# Botão para iniciar o envio
if st.button("Enviar Mensagens"):
    if arquivo and mensagem:
        # Ler a planilha com números
        df = pd.read_excel(arquivo)

        # Limpar números (remover espaços e garantir que estejam no formato correto)
        df['Número'] = df['Número'].astype(str).str.replace(r'\D', '', regex=True)

        # Barra de progresso
        with st.spinner('Enviando mensagens...'):
            for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Enviando", unit="msg"):
                numero = "+55" + row['Número']  # Adiciona o código do país

                # Enviar mensagens
                try:
                    kit.sendwhatmsg_instantly(numero, mensagem)
                    st.write(f"Mensagem enviada para {numero}")
                    time.sleep(15)  # Aguarda para garantir que o WhatsApp Web carregue a mensagem
                except Exception as e:
                    st.error(f"Erro ao enviar mensagem para {numero}: {str(e)}")

        st.success("Todas as mensagens foram enviadas.")
    else:
        st.error("Por favor, carregue o arquivo Excel e insira uma mensagem.")