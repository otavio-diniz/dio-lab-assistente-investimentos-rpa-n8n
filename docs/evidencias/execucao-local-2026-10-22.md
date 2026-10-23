# Evidência de execução local — 22/10/2026

**Natureza:** registro público de uma execução local de demonstração, acompanhado de **captura de tela autêntica** do canvas n8n fornecida pelo autor. A descrição preserva o método, o resultado e as limitações sem revelar a estrutura pessoal da estação de trabalho.

## Contexto e entradas

- Projeto: Assistente de Investimentos com RPA e n8n; atividade Santander 2026 / DIO.
- Ambiente declarado: Windows, Python 3.12.10, n8n 2.41.6, Webhook de teste em loopback.
- Fontes: tabela HTML didática da DIO com 10 clientes fictícios e CSV didático da DIO com 9 produtos.
- Operações: extração com Requests/BeautifulSoup, POST em JSON para Webhook, consulta HTTP do CSV, associação por perfil/saldo, mensagem por template e retorno HTTP/JSON.

## Evidência visual fornecida pelo autor

![Workflow n8n executado com seis nós verdes, Webhook até Respond e dez itens retornados](fluxo-n8n-execucao-2026-10-22.png)

*Figura 1 — Captura autêntica fornecida pelo autor em 22/10/2026; representa apenas a execução local observada.*

A imagem apresentada pelo autor em 22/10/2026 exibe a cadeia executada com indicadores verdes em todos os seis nós:

1. **Webhook** — 1 item de entrada;
2. **Solicitação HTTP** — 1 item de resposta HTTP;
3. **Código em JavaScript** — 9 itens de produtos estruturados;
4. **Associar Clientes e Produtos** — 10 itens de clientes;
5. **Gerar Mensagens por Perfil** — 10 itens;
6. **Responder ao Webhook** — 10 itens.

Esses rótulos e contagens refletem a captura apresentada pelo autor; não são prova de que este workflow foi reimportado e executado a partir de um clone limpo por terceiro.

## Conferência da saída Python

```text
Total de clientes: 10
Status HTTP: 200
Resposta: [array JSON com 10 objetos, incluindo nome, perfil, saldo, opcoes_elegiveis e mensagem]
```

No cenário sintético, o total de associações elegíveis foi **27**, segundo a matriz de casos em [docs/validacao.md](../validacao.md). As mensagens utilizam regras estáticas, não IA generativa; não houve envio de e-mails nem execução de investimento.

## Limites de escopo e custódia

A **captura original do fluxo** foi incorporada ao caderno acadêmico privado e agora também consta neste repositório como arquivo PNG autêntico, com SHA-256 `21897b2f624587c1ef337658675389c7c17d499235734b5f8f844d7871951ab0`. O print é evidência da execução local, **não** da reimportação independente ou da execução em produção. O texto completo do console do autor não foi reproduzido porque inclui caminhos locais desnecessários à compreensão.

Um avaliador independente pode inspecionar [n8n/workflow.json](../../n8n/workflow.json), [rpa/extracao_clientes_teste.py](../../rpa/extracao_clientes_teste.py), [requirements.txt](../../requirements.txt) e [docs/execucao.md](../execucao.md) para repetir os passos declarados. Até que isso ocorra com evidência, **reprodutibilidade independente = não verificada**.
