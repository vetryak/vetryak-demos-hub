variable "project_id" {
  description = "ID do projeto Google Cloud dedicado à demo."
  type        = string
}

variable "region" {
  description = "Região padrão dos recursos."
  type        = string
  default     = "us-central1"
}

variable "labels" {
  description = "Labels aplicados aos recursos (facilita achar e limpar)."
  type        = map(string)
  default = {
    owner   = "vetryak"
    purpose = "demo"
  }
}
