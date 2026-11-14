locals {
  apis = [
    "discoveryengine.googleapis.com",
    "aiplatform.googleapis.com",
    "bigquery.googleapis.com",
    "storage.googleapis.com",
  ]
}

resource "google_project_service" "apis" {
  for_each = toset(local.apis)

  service            = each.value
  disable_on_destroy = false
}

# Conta de serviço com o mínimo para o agente: rodar consultas (job user) e chamar o
# Gemini no Vertex AI. O dataset público dispensa papel de leitura de dados.
# Use-a no deploy: adk deploy agent_engine --service_account <email>
resource "google_service_account" "agent" {
  account_id   = "ge05-analista-dados"
  display_name = "Demo ge-05 - analista de dados (agente)"
}

resource "google_project_iam_member" "agent" {
  for_each = toset([
    "roles/bigquery.jobUser",
    "roles/aiplatform.user",
  ])

  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.agent.email}"
}
