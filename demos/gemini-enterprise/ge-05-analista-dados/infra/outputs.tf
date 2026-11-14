output "agent_service_account" {
  description = "Conta de serviço para usar no deploy do agente."
  value       = google_service_account.agent.email
}
