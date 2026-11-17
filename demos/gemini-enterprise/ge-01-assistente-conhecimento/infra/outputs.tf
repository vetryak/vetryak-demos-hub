output "docs_bucket" {
  description = "Bucket com os documentos de exemplo (use como data store no Gemini Enterprise)."
  value       = "gs://${google_storage_bucket.docs.name}"
}
