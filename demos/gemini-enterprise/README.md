# Gemini Enterprise

Demos do **Gemini Enterprise** (plataforma de agentes do Google Cloud para empresas,
sucessora do Google Agentspace): busca e chat sobre os dados da empresa, agentes prontos
(como Deep Research e NotebookLM Enterprise), criação de agentes sem código
(Agent Designer) e publicação de agentes próprios construídos com ADK.

## As 5 demos

| ID | Demo | Pergunta do cliente que ela responde | Recursos mostrados |
|----|------|--------------------------------------|--------------------|
| [ge-01](ge-01-assistente-conhecimento/) | Assistente de conhecimento corporativo | "Meus colaboradores perdem tempo procurando informação espalhada em vários sistemas." | Conectores (Drive, SharePoint, Confluence), respostas com citações, respeito às permissões |
| [ge-02](ge-02-revisao-contratos/) | Revisão de contratos e compliance | "O jurídico demora dias para revisar contratos padrão." | Agent Designer (sem código), playbook como fonte, Deep Research |
| [ge-03](ge-03-service-desk-agente/) | Agente de service desk com ações | "Quero um agente que **faça** coisas, não só responda." | ADK, Vertex AI Agent Engine, ferramentas (abrir/consultar chamado), registro no Gemini Enterprise |
| [ge-04](ge-04-copiloto-comercial/) | Copiloto comercial | "Meu time de vendas chega despreparado nas reuniões." | Conectores de CRM e e-mail/agenda, brief de conta, geração de proposta |
| [ge-05](ge-05-analista-dados/) | Analista de dados conversacional | "A diretoria depende do BI para qualquer pergunta sobre números." | ADK + BigQuery (linguagem natural para SQL), dataset público, governança |

**Sugestão de combinação por reunião (45-60 min):** abra com a `ge-01` (valor imediato,
sem código), escolha uma demo de área (`ge-02` ou `ge-04`) e feche com uma demo de
extensibilidade (`ge-03` ou `ge-05`) para mostrar que dá para ir além do pronto.

## Pré-requisitos comuns

- Projeto Google Cloud **dedicado a demos**, com faturamento ativo.
- Licenças de Gemini Enterprise para os usuários da demo. Confira na documentação oficial
  qual **edição** libera cada recurso (conectores, Agent Designer, agentes próprios),
  porque isso muda com frequência.
- Identidade: Google Workspace / Cloud Identity, ou federação com outro IdP
  (ex.: Microsoft Entra ID) quando a demo usar fontes Microsoft.
- Papéis IAM para quem monta: administrador do Discovery Engine / Gemini Enterprise no
  projeto, e para as demos com código, acesso ao Vertex AI e ao Agent Engine.
- Dados de exemplo: **só fictícios** (cada demo traz os seus em `data/`) ou datasets públicos.

## Base de infraestrutura

As demos com `infra/` habilitam as APIs necessárias via Terraform:

```bash
cd demos/gemini-enterprise/<demo>/infra
cp terraform.tfvars.example terraform.tfvars   # preencha com o seu projeto de demo
terraform init && terraform apply
```

A criação do app do Gemini Enterprise e a ligação dos conectores são feitas no console
(algumas etapas exigem consentimento OAuth de administrador da fonte de dados).

## Links úteis

- Documentação: https://cloud.google.com/gemini-enterprise/docs
- ADK (Agent Development Kit): https://google.github.io/adk-docs/
- Vertex AI Agent Engine: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview
