"""Analista de dados conversacional da demo ge-05.

Usa o dataset público `bigquery-public-data.thelook_ecommerce` (e-commerce fictício),
então não há dado de cliente envolvido. As consultas rodam e são cobradas no projeto
de demo (GOOGLE_CLOUD_PROJECT), somente leitura e com teto de bytes processados.
"""

import os

import google.auth
from google.adk.agents import Agent
from google.adk.integrations.bigquery import BigQueryCredentialsConfig, BigQueryToolset
from google.adk.integrations.bigquery.config import BigQueryToolConfig, WriteMode

DATASET = "bigquery-public-data.thelook_ecommerce"

_credentials, _ = google.auth.default()

bigquery_toolset = BigQueryToolset(
    credentials_config=BigQueryCredentialsConfig(credentials=_credentials),
    bigquery_tool_config=BigQueryToolConfig(
        write_mode=WriteMode.BLOCKED,  # só leitura: nenhuma escrita ou DDL
        compute_project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
        maximum_bytes_billed=int(os.getenv("BQ_MAX_BYTES_BILLED", "5000000000")),
        max_query_result_rows=100,
        application_name="vetryak-demo-ge-05",
        job_labels={"owner": "vetryak", "purpose": "demo", "demo": "ge-05"},
    ),
)

INSTRUCAO = f"""
Você é um analista de dados da diretoria de uma loja online (dados fictícios do dataset
`{DATASET}`). Responda em português, para um público executivo.

Como trabalhar:
1. Antes de escrever SQL, use as ferramentas de metadados para conferir tabelas e colunas
   do dataset `{DATASET}` (principais: orders, order_items, products, users,
   distribution_centers).
2. Escreva SQL padrão do BigQuery, sempre com nomes totalmente qualificados
   (`{DATASET}.<tabela>`), filtrando por período quando fizer sentido.
3. Responda com: (a) a resposta em uma frase, (b) uma tabela curta com os números,
   (c) a consulta SQL usada, em bloco de código, para auditoria.
4. Se a pergunta for ambígua (ex.: "vendas" = receita ou quantidade?), diga qual
   interpretação usou.
5. Nunca invente números: se a consulta falhar ou não houver dados, diga isso.
"""

root_agent = Agent(
    name="analista_dados",
    model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    description="Responde perguntas de negócio consultando o BigQuery e mostra o SQL usado.",
    instruction=INSTRUCAO,
    tools=[bigquery_toolset],
)
