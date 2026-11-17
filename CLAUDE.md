# CLAUDE.md

As instruções do repositório ficam em `AGENTS.md` (fonte única para todos os agentes).

@AGENTS.md

## Específico do Claude Code

- Use `moon` para validar mudanças antes de propor commit (`moon run :check-readme`,
  `moon check <id>`).
- Se `terraform` ou `uv` não estiverem instalados, diga que a tarefa não rodou em vez de
  assumir que passou.
