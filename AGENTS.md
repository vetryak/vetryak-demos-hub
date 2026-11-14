# AGENTS.md — vetryak-demos-hub

Este arquivo é a **fonte única de instruções** para qualquer agente de IA que trabalhe neste
repositório (Claude Code, Gemini CLI, GitHub Copilot, Cursor, Codex e afins).
`CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md` apenas apontam para cá.
Se precisar mudar uma regra, mude **aqui**.

## Contexto

- Repositório de demos da **Vetryak** (parceira Google Cloud) para apresentar a clientes.
- Objetivo: montar e apresentar demos rápido, com roteiro pronto e infraestrutura reproduzível.
- Idioma: **português (BR)** em documentação, comentários de roteiro e mensagens de commit.
  Código (nomes de variáveis, funções) pode ficar em inglês.

## Arquitetura do repositório

- **Monorepo** gerenciado com [moonrepo](https://moonrepo.dev) (versão fixada em `.prototools`).
- **VSA (Vertical Slice Architecture)**: cada demo é uma fatia vertical **autocontida** com
  roteiro, código, infraestrutura e dados de exemplo na mesma pasta.

```
demos/<contexto>/<demo>/   # um projeto moon por demo (vertical slice)
  README.md                # roteiro de apresentação (obrigatório, seção "## Roteiro")
  moon.yml                 # id, tags e tarefas da demo
  infra/                   # Terraform da demo (opcional, tag "terraform")
  agent/                   # código de agente ADK/Python (opcional, tag "python")
  data/                    # dados de exemplo FICTÍCIOS
  docs/                    # arquitetura, prompts, FAQ/objeções
shared/<pacote>/           # código realmente compartilhado (só quando 2+ demos usam)
templates/demo/            # template do `moon generate demo`
docs/                      # convenções do repositório
.moon/                     # workspace e tarefas herdadas por tag
```

Contextos atuais em `demos/`: `gemini-enterprise`, `vertex-ai`, `dados-analytics`,
`seguranca`, `infra-redes`, `modernizacao-apps`. Novo contexto = nova pasta + `README.md`.

## Regras obrigatórias

1. **Sem segredos.** Nunca versione chaves, tokens, senhas, service account JSON, `.env`,
   `terraform.tfvars` ou IDs reais de projeto/organização/billing. Use `.env.example` e
   `*.tfvars.example` com placeholders (`<PROJECT_ID>`, `<REGION>`).
2. **Sem dados de clientes.** Dados em `data/` são sempre fictícios ou de datasets públicos.
   Nada de nome de cliente real em demo genérica; personalização por cliente fica fora deste repo.
3. **Fatia autocontida.** Uma demo não importa arquivos de outra demo. Se algo se repete em
   2+ demos, extraia para `shared/` e declare a dependência em `moon.yml` (`dependsOn`).
4. **README com roteiro.** Toda demo tem `README.md` com a seção `## Roteiro` (a tarefa
   `check-readme` falha sem ela). Siga a estrutura de `templates/demo/README.md`.
5. **Infra reproduzível e descartável.** Toda demo com recursos na nuvem documenta a
   seção `## Limpeza` (como destruir tudo para não gerar custo).
6. **Menor privilégio.** Service accounts com papéis mínimos; prefira Workload Identity /
   ADC a chaves exportadas.

## Comandos

```bash
proto install                      # instala a versão do moon fixada
moon projects                      # lista as demos (projetos)
moon tasks                         # lista tarefas
moon run :check-readme             # valida o README de todas as demos
moon check <id-da-demo>            # roda todas as tarefas de uma demo
moon generate demo                 # cria uma nova demo a partir do template
```

Tarefas herdadas por tag (ver `.moon/tasks/`):

| Tag         | Tarefas                      | Requer                    |
|-------------|------------------------------|---------------------------|
| (todas)     | `check-readme`               | shell                     |
| `terraform` | `tf-fmt`, `tf-validate`      | `terraform` no PATH       |
| `python`    | `lint`, `format-check`       | `uv` no PATH (usa `uvx`)  |

## Como trabalhar aqui (para agentes)

- Antes de editar uma demo, leia o `README.md` dela e o `moon.yml`.
- Para criar uma demo: `moon generate demo` (ou copie `templates/demo/`), depois ajuste
  `moon.yml` (`id` único, prefixo do contexto, ex.: `ge-06-...`) e preencha o roteiro.
- Mantenha mudanças dentro da fatia que está sendo alterada.
- Ao adicionar recursos Google Cloud, cite a API necessária em `## Pré-requisitos` e
  habilite-a no Terraform (`google_project_service`).
- Produtos e nomes Google Cloud mudam rápido: confira a documentação oficial
  (cloud.google.com) antes de afirmar nomes de console, limites ou preços.
- Commits: mensagens curtas em português, no imperativo (ex.: `adiciona roteiro da ge-03`).
