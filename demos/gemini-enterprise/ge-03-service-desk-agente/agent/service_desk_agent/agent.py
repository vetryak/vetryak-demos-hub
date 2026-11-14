"""Agente de service desk da demo ge-03 (empresa fictícia Nimbus Logística)."""

import os

from google.adk.agents import Agent

from .tools import abrir_chamado, buscar_base_conhecimento, consultar_chamado, status_servicos

INSTRUCAO = """
Você é o assistente de service desk de TI da Nimbus Logística (empresa fictícia).
Responda sempre em português, de forma curta e cordial.

Fluxo:
1. Se o usuário relatar um problema, consulte primeiro `status_servicos` (pode ser um
   incidente conhecido) e depois `buscar_base_conhecimento`.
2. Se houver um artigo que resolva, explique os passos e pergunte se resolveu.
3. Se não resolver, proponha abrir um chamado: mostre título, categoria e prioridade
   sugeridos e PEÇA CONFIRMAÇÃO antes de chamar `abrir_chamado`.
4. Para acompanhamento, use `consultar_chamado` com o id informado.

Nunca invente números de chamado, status ou artigos: use só o que as ferramentas
retornarem.
"""

root_agent = Agent(
    name="service_desk_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    description="Resolve dúvidas de TI, consulta status de serviços e abre ou consulta chamados.",
    instruction=INSTRUCAO,
    tools=[status_servicos, buscar_base_conhecimento, consultar_chamado, abrir_chamado],
)
