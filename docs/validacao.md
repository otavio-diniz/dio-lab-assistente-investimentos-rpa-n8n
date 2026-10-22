# Validação do MVP — cenário fictício

## Escopo da evidência

Fonte: execução local compartilhada pelo autor em **22/10/2026**, Windows + Python 3.12.10 + n8n 2.41.6. A extração acessa dez registros da página de laboratório da DIO; o n8n busca nove produtos do CSV didático e aplica critérios de perfil e aporte mínimo.

**Evidência observada:** Python apresenta `Total de clientes: 10`, `Status HTTP: 200` e resposta JSON com dez objetos, cada um com `nome`, `email`, `perfil`, `saldo`, `opcoes_elegiveis` e `mensagem`. O editor do n8n exibiu os seis nós concluídos com contagens 1/1/9/10/10/10. Essa é uma verificação funcional sobre uma amostra sintética, **não** um teste de desempenho ou avaliação financeira.

## Resultado da amostra

| Cliente fictício | Perfil | Saldo de teste (R$) | Produtos elegíveis |
| --- | --- | ---: | ---: |
| Ana Silva | Conservador | 12.500 | 3 |
| Bruno Lima | Moderado | 3.200 | 2 |
| Carla Souza | Arrojado | 28.900 | 3 |
| Daniel Oliveira | Conservador | 850 | 2 |
| Elena Rodrigues | Arrojado | 45.000 | 3 |
| Felipe Santos | Moderado | 7.800 | 3 |
| Gabriela Costa | Conservador | 1.500 | 3 |
| Henrique Alves | Moderado | 22.300 | 3 |
| Isabela Martins | Conservador | 500 | 2 |
| João Pereira | Arrojado | 15.000 | 3 |
| **Total** | **10 clientes** | — | **27 associações** |

Exemplo interpretativo: Bruno não recebe Fundo Multimercado (mínimo fictício R$ 5.000) porque seu saldo simulado é R$ 3.200. Isabela, com R$ 500, recebe Poupança e Tesouro Selic, mas não CDB Liquidez Diária (mínimo R$ 1.000). Em todos os casos exibidos, o produto respeita o perfil do registro.

## Critérios de aceitação da execução

1. O script deve identificar a tabela HTML e montar uma lista JSON de clientes.
2. O Webhook deve receber a lista em `body.clientes`.
3. O HTTP Request deve buscar o CSV e o primeiro Code deve estruturar **nove** registros.
4. O segundo Code deve produzir **dez** associações de cliente com listas elegíveis.
5. O terceiro Code deve acrescentar `mensagem` a cada cliente.
6. O nó Respond deve devolver HTTP 200 e um **array com dez mensagens**.

## Limitações e ensaios de robustez não realizados

Os testes acima são do cenário positivo da base original. Ainda não foram demonstrados testes automatizados de CSV com campos citados, variações de layout da página HTML, perfis inválidos, saldos malformados, ausência de investimentos elegíveis, indisponibilidade de serviços externos, concorrência de chamadas, reimportação do workflow em outra instância e portabilidade macOS/Linux.

As taxas constantes no CSV são **ilustrativas** e não podem ser interpretadas como rentabilidades atuais ou resultados de investimento. O workflow não utiliza LLM nem Gmail.

## Procedência

Base original: [digitalinnovationone/dio-lab-assistente-investimentos-rpa-n8n](https://github.com/digitalinnovationone/dio-lab-assistente-investimentos-rpa-n8n). O presente fork contém código e documentação complementares de aplicação educacional. Imagens da interface devem ser capturas autênticas, sanitizadas e vinculadas a uma execução real.
