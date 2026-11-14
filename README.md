# vetryak-demos-hub

Hub de demos da **Vetryak** sobre Google Cloud: cada demo vem com roteiro de apresentação,
infraestrutura reproduzível e dados de exemplo, para montar e apresentar a clientes rápido.

## Catálogo

| Contexto | Demos | Descrição |
|----------|-------|-----------|
| [Gemini Enterprise](demos/gemini-enterprise/) | 5 | Agentes, busca corporativa e automação com Gemini Enterprise |
| [Vertex AI](demos/vertex-ai/) | — | Modelos, RAG, avaliação e MLOps no Vertex AI |
| [Dados e Analytics](demos/dados-analytics/) | — | BigQuery, Looker, pipelines de dados |
| [Segurança](demos/seguranca/) | — | Security Command Center, IAM, VPC-SC, Google SecOps |
| [Infra e Redes](demos/infra-redes/) | — | Landing zone, rede híbrida, GKE, balanceamento |
| [Modernização de Apps](demos/modernizacao-apps/) | — | Cloud Run, GKE, CI/CD, migração de aplicações |

### Gemini Enterprise

| ID | Demo | Área do cliente | Tipo |
|----|------|-----------------|------|
| `ge-01` | [Assistente de conhecimento corporativo](demos/gemini-enterprise/ge-01-assistente-conhecimento/) | RH, Operações, todos | Sem código (conectores) |
| `ge-02` | [Revisão de contratos e compliance](demos/gemini-enterprise/ge-02-revisao-contratos/) | Jurídico, Compras | Sem código (Agent Designer) |
| `ge-03` | [Agente de service desk com ações](demos/gemini-enterprise/ge-03-service-desk-agente/) | TI, Suporte | Código (ADK + Agent Engine) |
| `ge-04` | [Copiloto comercial](demos/gemini-enterprise/ge-04-copiloto-comercial/) | Vendas, Customer Success | Sem código (conectores + agentes prontos) |
| `ge-05` | [Analista de dados conversacional](demos/gemini-enterprise/ge-05-analista-dados/) | Finanças, Diretoria, BI | Código (ADK + BigQuery) |

## Como o repositório é organizado

Monorepo com [moonrepo](https://moonrepo.dev) e **VSA (Vertical Slice Architecture)**:
cada demo é uma pasta autocontida, com tudo que ela precisa.

```
demos/
  <contexto>/                 # ex.: gemini-enterprise
    README.md                 # visão do contexto e lista das demos
    <demo>/                   # uma vertical slice = um projeto moon
      README.md               # roteiro de apresentação
      moon.yml                # id, tags, tarefas
      infra/  agent/  data/  docs/
shared/                       # código compartilhado entre demos (quando houver)
templates/demo/               # template para criar uma nova demo
docs/                         # convenções do repositório
.moon/                        # configuração do workspace e tarefas herdadas
```

A configuração do moon vem do template [vetryak/moon-base](https://github.com/vetryak/moon-base)
(versão em `.moon/moon-base.version`): `demos/<contexto>/<demo>` faz o papel de
`slices/<dominio>/<feature>` e `shared/` o de `libs/`. O CI (`.github/workflows/moon-ci.yml`)
roda `moon ci`, que executa só as tarefas das demos afetadas.

Detalhes em [docs/convencoes.md](docs/convencoes.md).

## Começando

Pré-requisitos: [proto](https://moonrepo.dev/proto) (ou moon instalado), `gcloud`,
e conforme a demo, `terraform`, `ruff`, `pytest` e [`uv`](https://docs.astral.sh/uv/)
(as tarefas usam o toolchain `system`, ou seja, as ferramentas já instaladas).

```bash
proto use                     # instala o moon na versão fixada em .prototools
moon projects                 # lista as demos
moon run :check-readme        # valida os roteiros
moon check ge-05-analista-dados   # roda as tarefas de uma demo
```

### Criar uma nova demo

```bash
moon generate demo
```

O gerador pergunta contexto, id e título e cria a pasta a partir de
[templates/demo/](templates/demo/). Passo a passo em [docs/nova-demo.md](docs/nova-demo.md).

## Uso com agentes de IA

As regras para agentes (Claude Code, Gemini CLI, Copilot, Cursor, Codex) ficam em
[AGENTS.md](AGENTS.md). `CLAUDE.md`, `.gemini/settings.json` e `.github/copilot-instructions.md`
apontam para ele, então há uma só fonte de verdade.

## Regras de ouro

- **Nada de segredos** nem IDs reais de projeto/organização no repositório.
- **Nada de dados de clientes**: só dados fictícios ou datasets públicos.
- Toda demo tem **roteiro** e **limpeza** (como destruir os recursos depois).

## Repositórios relacionados

- [vetryak/vetryak-docs-hub](https://github.com/vetryak/vetryak-docs-hub): propostas, planos e materiais internos.
- [vetryak/moon-base](https://github.com/vetryak/moon-base): template base de moonrepo da Vetryak.

## Licença

[GPL-3.0](LICENSE).
