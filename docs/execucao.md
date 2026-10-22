# Guia de execução e diagnóstico

Este documento complementa o [Quickstart do README](../README.md#quickstart--primeira-execução-local). Não publique seu endereço de loopback nem exponha a porta 5678.

## Requisitos materiais

- **Ambiente reproduzido:** Windows PowerShell 5.1, Python 3.12.10 (64-bit), n8n 2.41.6 local.
- Bibliotecas Python do arquivo [requirements.txt](../requirements.txt). Instale preferencialmente em um ambiente virtual.
- Acesso HTTP(S) às fontes fictícias [página de clientes](https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/) e [CSV de investimentos](https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/data.csv).
- Workflow importado de [n8n/workflow.json](../n8n/workflow.json). A cópia remove identificadores de instalação; **não foi reimportada em outra instância como teste independente**.

## Primeiro uso

1. Siga o Quickstart do README para criar o `.venv`.
2. Mantenha o n8n local iniciado e abra o workflow importado no editor.
3. No nó **Webhook**, confira método `POST`, caminho `clientes` e resposta **Using Respond to Webhook Node**. No nó final, confira **All Incoming Items** e HTTP 200.
4. Use **Execute workflow** no **canvas** para aguardar a URL de teste; não use apenas o disparo isolado do nó Webhook caso deseje percorrer os nós seguintes.
5. Execute `rpa/extracao_clientes_teste.py` com o interpretador do ambiente virtual enquanto o n8n aguarda.
6. Confira a sequência Webhook → HTTP Request → Code CSV → Associação → Mensagens → Respond. A saída final deve ser um array de clientes com `opcoes_elegiveis` e `mensagem`.

**Linux/macOS (orientação não verificada em máquina real):** substitua os comandos de Windows por `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt` e `.venv/bin/python rpa/extracao_clientes_teste.py`.

## Diagnóstico de problemas comuns

| Sintoma | Possível causa e ação |
| --- | --- |
| HTTP 404 `webhook "clientes" is not registered` | Reabra o editor, acione **Execute workflow** e execute o Python **uma vez** durante a escuta. A URL de teste é temporária. |
| HTTP 200 com corpo vazio | Verifique se o **Respond to Webhook** executou e está após os nós de mensagens. Disparar somente o trigger pode não percorrer todo o fluxo. |
| `ModuleNotFoundError: requests/bs4` | Confira se está executando o Python do `.venv` e se instalou o `requirements.txt` nele. |
| n8n sem clientes | Confira o nome do campo `clientes`, o caminho do Webhook e o JSON recebido no nó inicial. |
| CSV sem produtos ou erros no Code | Confirme URL, conectividade e cabeçalho `perfil,produto,minimo,rentabilidade`. |
| Google Colab remoto não conecta a `127.0.0.1` | Execute Python localmente na mesma máquina do n8n; não exponha a porta como solução automática. |
| Espera prolongada | Verifique se o teste foi acionado no canvas, a URL de teste corresponde à configurada e não existe uma sessão antiga pendente. |

## O que este laboratório não faz

Não executa operações financeiras, não valida suitability regulatória, não usa dados bancários reais, não envia e-mails, não fornece rentabilidade de mercado em tempo real e não utiliza IA generativa. As mensagens vêm de **templates fixos** e a seleção depende apenas de perfil e saldo mínimo.
