# Deploy do agente no Agent Engine e publicação no Gemini Enterprise

> Testado com `google-adk` 2.14. Confira `uv run adk deploy agent_engine --help` e a
> documentação antes de apresentar, porque comandos e telas mudam com frequência.

## 1. Infra

```bash
cd infra && cp terraform.example.tfvars terraform.tfvars && terraform init && terraform apply
```

Anote o output `agent_service_account`.

## 2. Testar localmente

```bash
cp agent/analista_dados/.env.example agent/analista_dados/.env   # preencha
gcloud auth application-default login
uv sync
moon run ge-05-analista-dados:dev     # ou: uv run adk web agent
```

## 3. Deploy no Vertex AI Agent Engine

```bash
uv run adk deploy agent_engine \
  --project <PROJECT_ID_DA_DEMO> \
  --region us-central1 \
  --display_name "Analista de Dados (demo)" \
  --service_account <agent_service_account> \
  agent/analista_dados
```

## 4. Registrar no Gemini Enterprise

No app da demo, em **Agentes**, adicione um agente personalizado apontando para o
resource name do Agent Engine (`projects/<n>/locations/us-central1/reasoningEngines/<id>`).

## 5. Limpeza

Apague o Reasoning Engine, remova o agente do app e rode `terraform destroy`.
