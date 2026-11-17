"""Testes das ferramentas do service desk (sem depender do ADK nem de credenciais)."""

import importlib.util
from pathlib import Path

_PATH = Path(__file__).resolve().parents[1] / "agent" / "service_desk_agent" / "tools.py"
_spec = importlib.util.spec_from_file_location("tools", _PATH)
tools = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tools)


def test_busca_encontra_artigo_de_vpn():
    resultado = tools.buscar_base_conhecimento("vpn")
    assert resultado["total"] >= 1
    assert resultado["artigos"][0]["id"] == "KB-204"


def test_status_de_servico_desconhecido():
    assert tools.status_servicos("impressora") == {"impressora": "serviço não encontrado"}


def test_abrir_e_consultar_chamado():
    criado = tools.abrir_chamado("VPN caindo", "Já reiniciei o cliente.", "Rede", "alta")
    assert criado["id"].startswith("INC-")
    assert tools.consultar_chamado(criado["id"])["status"] == "aberto"


def test_chamado_inexistente():
    assert "erro" in tools.consultar_chamado("INC-0000")
