locals {
  apis = [
    "discoveryengine.googleapis.com",
    "storage.googleapis.com",
  ]
}

resource "google_project_service" "apis" {
  for_each = toset(local.apis)

  service            = each.value
  disable_on_destroy = false
}

# Bucket com os documentos FICTÍCIOS de data/, usado como fonte (data store do
# Cloud Storage) quando o cliente não tiver Drive/SharePoint de demo disponível.
resource "google_storage_bucket" "docs" {
  name                        = "${var.project_id}-ge04-docs"
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
  force_destroy               = true
  labels                      = var.labels

  depends_on = [google_project_service.apis]
}

resource "google_storage_bucket_object" "docs" {
  for_each = fileset("${path.module}/../data", "**/*.{md,csv}")

  bucket = google_storage_bucket.docs.name
  name   = each.value
  source = "${path.module}/../data/${each.value}"
}
