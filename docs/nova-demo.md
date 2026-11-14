# Como criar uma nova demo

1. Gere a estrutura:

   ```bash
   moon generate demo
   ```

   O gerador pergunta o **contexto** (pasta em `demos/`), o **id** (ex.: `ge-06-minha-demo`)
   e o **título**, e cria `demos/<contexto>/<id>/` a partir de `templates/demo/`.

   Sem moon? Copie `templates/demo/` para a pasta nova e troque os `{{ ... }}` à mão.

2. Ajuste `moon.yml`: adicione a tag `terraform` se tiver `infra/` (e o override de
   `tf-validate`) e `language: "python"` se tiver `agent/`. Use `ge-03` como referência.
3. Preencha o `README.md` (principalmente `## Roteiro` e `## Limpeza`).
4. Adicione a demo na tabela do `README.md` do contexto e do `README.md` da raiz.
5. Valide:

   ```bash
   moon run <id>:check-readme
   moon check <id>
   ```

6. Abra um PR usando o template (checklist de segredos incluso).
