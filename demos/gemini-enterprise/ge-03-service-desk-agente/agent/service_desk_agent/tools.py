"""Ferramentas do agente de service desk.

Para a demo, os dados ficam em memória (FICTÍCIOS). Em um piloto, troque o corpo destas
funções por chamadas à API do ITSM do cliente (ServiceNow, Jira Service Management etc.),
mantendo as mesmas assinaturas e docstrings: é delas que o modelo tira quando usar cada
ferramenta.
"""

from __future__ import annotations

import itertools
from datetime import UTC, datetime

_KB = [
    {
        "id": "KB-101",
        "titulo": "Como redefinir a senha do e-mail corporativo",
        "conteudo": "Acesse o portal de autoatendimento, clique em 'Esqueci a senha' e "
        "confirme o código enviado ao celular cadastrado.",
    },
    {
        "id": "KB-204",
        "titulo": "VPN não conecta no trabalho remoto",
        "conteudo": "Verifique se o cliente de VPN está na versão 5.2 ou superior, "
        "reinicie o serviço e tente a conexão pelo servidor 'sp-02'.",
    },
    {
        "id": "KB-310",
        "titulo": "Solicitar monitor adicional",
        "conteudo": "Abra um chamado na categoria 'Equipamentos'. Requer acordo de "
        "trabalho remoto ativo e aprovação do gestor.",
    },
]

_STATUS = {
    "email": "operacional",
    "vpn": "degradado: lentidão no servidor sp-01 desde 08:40, equipe atuando",
    "erp": "operacional",
    "wifi-escritorio-sp": "operacional",
}

_CHAMADOS: dict[str, dict] = {
    "INC-1042": {
        "id": "INC-1042",
        "titulo": "Notebook não liga",
        "status": "em atendimento",
        "prioridade": "alta",
        "categoria": "Equipamentos",
        "atualizado_em": "2026-11-13T16:20:00Z",
    },
}
_seq = itertools.count(1043)


def buscar_base_conhecimento(consulta: str) -> dict:
    """Busca artigos na base de conhecimento de TI.

    Use antes de abrir um chamado, para tentar resolver a dúvida do usuário.

    Args:
        consulta: palavras-chave do problema, por exemplo "vpn não conecta".

    Returns:
        Dicionário com a lista de artigos encontrados (id, titulo, conteudo).
    """
    termos = consulta.lower().split()
    achados = [
        a for a in _KB if any(t in (a["titulo"] + " " + a["conteudo"]).lower() for t in termos)
    ]
    return {"artigos": achados, "total": len(achados)}


def status_servicos(servico: str | None = None) -> dict:
    """Consulta o status atual dos serviços de TI (incidentes em andamento).

    Args:
        servico: nome do serviço (email, vpn, erp, wifi-escritorio-sp). Vazio = todos.

    Returns:
        Dicionário serviço -> status.
    """
    if servico:
        chave = servico.lower()
        return {chave: _STATUS.get(chave, "serviço não encontrado")}
    return dict(_STATUS)


def consultar_chamado(chamado_id: str) -> dict:
    """Consulta o andamento de um chamado existente.

    Args:
        chamado_id: identificador do chamado, por exemplo "INC-1042".

    Returns:
        Dados do chamado ou um erro se não existir.
    """
    chamado = _CHAMADOS.get(chamado_id.upper())
    return chamado or {"erro": f"Chamado {chamado_id} não encontrado."}


def abrir_chamado(titulo: str, descricao: str, categoria: str, prioridade: str = "media") -> dict:
    """Abre um novo chamado no service desk.

    Só use depois de confirmar com o usuário o título, a categoria e a prioridade.

    Args:
        titulo: resumo curto do problema.
        descricao: detalhes, incluindo o que o usuário já tentou.
        categoria: uma de "Acesso", "Equipamentos", "Rede", "Sistemas".
        prioridade: "baixa", "media" ou "alta".

    Returns:
        Dados do chamado criado, incluindo o id.
    """
    chamado_id = f"INC-{next(_seq)}"
    chamado = {
        "id": chamado_id,
        "titulo": titulo,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "status": "aberto",
        "atualizado_em": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    _CHAMADOS[chamado_id] = chamado
    return chamado
