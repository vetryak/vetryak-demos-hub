# Convenções do repositório

## Vertical slices

Cada demo é uma **fatia vertical**: roteiro, código, infraestrutura e dados ficam juntos em
`demos/<contexto>/<demo>/`. Quem for apresentar só precisa abrir uma pasta.

- Uma demo **não importa** arquivos de outra.
- Código que se repete em 2+ demos vai para `shared/<pacote>/` (que também é projeto moon)
  e a demo declara `dependsOn: ["<pacote>"]` no `moon.yml`.

## Nomes e IDs

| Item | Padrão | Exemplo |
|------|--------|---------|
| Pasta de contexto | kebab-case, português | `gemini-enterprise`, `dados-analytics` |
| Pasta da demo | `<prefixo>-<nn>-<slug>` | `ge-03-service-desk-agente` |
| `id` no `moon.yml` | igual ao nome da pasta | `ge-03-service-desk-agente` |
| Prefixos | `ge` Gemini Enterprise, `vx` Vertex AI, `da` Dados, `sec` Segurança, `net` Infra/Redes, `app` Modernização | |

## Tags no `moon.yml`

As tags definem quais tarefas a demo herda de `.moon/tasks/`:

- `terraform`: a demo tem `infra/` → herda `tf-fmt` e `tf-validate`.
- `python`: a demo tem `agent/` → herda `lint` e `format-check` (ruff via `uvx`).
- Tag do contexto (ex.: `gemini-enterprise`) para filtrar: `moon run '#gemini-enterprise:check-readme'`.

## Estrutura do README da demo

Use [templates/demo/README.md](../templates/demo/README.md). Seções obrigatórias:

1. Resumo (problema, público, mensagem-chave)
2. Pré-requisitos
3. Arquitetura
4. Preparação (antes da reunião)
5. **Roteiro** (passo a passo com tempo estimado e o que falar)
6. Perguntas frequentes e objeções
7. **Limpeza**
8. Status (checklist do que já está pronto)

## Segurança

- Variáveis sensíveis só em `.env` local (ignorado pelo git) a partir do `.env.example`.
- Terraform: `terraform.tfvars` é ignorado; versione apenas `terraform.tfvars.example`.
- Antes de abrir PR, rode `gitleaks detect --config .gitleaks.toml` se tiver instalado.
- Projetos de demo devem ser **isolados** (projeto GCP dedicado), nunca ambiente de cliente.
