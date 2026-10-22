import requests
from bs4 import BeautifulSoup

# ETAPA 1 - Enderecos
URL_PAGINA = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/"

N8N_WEBHOOK = "http://127.0.0.1:5678/webhook-test/clientes"

# ETAPA 2 - Baixar a pagina de clientes
resposta_pagina = requests.get(URL_PAGINA, timeout=20)
resposta_pagina.raise_for_status()

# ETAPA 3 - Extrair os clientes
soup = BeautifulSoup(resposta_pagina.text, "html.parser")
linhas = soup.select("#clientes tbody tr")

clientes = []

for linha in linhas:
    colunas = linha.find_all("td")

    cliente = {
        "nome": colunas[0].get_text(strip=True),
        "email": colunas[1].get_text(strip=True),
        "saldo": colunas[2].get_text(strip=True),
        "perfil": colunas[3].get_text(strip=True),
    }

    clientes.append(cliente)

# ETAPA 4 - Conferir os dados extraidos
print("Clientes encontrados:")

for cliente in clientes:
    print(cliente)

print(f"\nTotal de clientes: {len(clientes)}")

# ETAPA 5 - Teste local de envio ao Webhook
if not clientes:
    print("Nenhum cliente encontrado. Envio cancelado.")
else:
    try:
        resposta_n8n = requests.post(
            N8N_WEBHOOK,
            json={"clientes": clientes},
            timeout=30
        )

        print("\nResultado do teste com n8n:")
        print("Status HTTP:", resposta_n8n.status_code)
        print("Resposta:", resposta_n8n.text)

        resposta_n8n.raise_for_status()

    except requests.RequestException as erro:
        print("\nFalha de comunicacao com o n8n:")
        print(erro)
