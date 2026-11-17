# Deploy do agente no Agent Engine e publicação no Gemini Enterprise

> Testado com `google-adk` 2.14. Os comandos e telas do ADK e do Gemini Enterprise mudam com frequência. Confira
> `uv run adk deploy agent_engine --help` e a documentação antes de apresentar.

## 1. Testar localmente

```bash
cp agent/service_desk_agent/.env.example agent/service_desk_agent/.env   # preencha
gcloud auth application-default login
uv sync
moon run ge-03-service-desk-agente:dev     # ou: uv run adk web agent
```

Abra http://localhost:8000, escolha `service_desk_agent` e teste os prompts do roteiro.

## 2. Infra

```bash
cd infra && cp terraform.example.tfvars terraform.tfvars && terraform init && terraform apply
```

## 3. Deploy no Vertex AI Agent Engine

```bash
uv run adk deploy agent_engine \
  --project <PROJECT_ID_DA_DEMO> \
  --region us-central1 \
  --display_name "Service Desk Nimbus (demo)" \
  agent/service_desk_agent
```

Anote o **resource name** do Reasoning Engine retornado
(`projects/<n>/locations/us-central1/reasoningEngines/<id>`).

## 4. Registrar no Gemini Enterprise

No console do Gemini Enterprise, no app da demo, vá em **Agentes** e adicione um agente
personalizado apontando para o resource name do Agent Engine. Dê nome e descrição em
português, porque é isso que o usuário final vê na galeria de agentes.

## 5. Limpeza

Apague o Reasoning Engine (console do Vertex AI → Agent Engine, ou API), remova o agente
do app e rode `terraform destroy`.
