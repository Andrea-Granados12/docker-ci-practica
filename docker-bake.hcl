group "default" {
  targets = ["build"]
}

target "build" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["docker-ci-practica:latest"]
}

target "validate-build" {
  inherits = ["build"]
}¿