- Python Not Found
   * Cause:
     python is not recognized as an internal or external command
   * Debug:
     ```` bash
     python --version
     ````

- Virtual Environment Not Activated
   * Cause:
     ModuleNotFoundError
   * Debug:
     ```` bash
     .venv\Scripts\activate
     ````

- Ollama Not Installed
   * Cause:
     Connection refused
   * Debug:
    ```` bash
    ollama serve
    ````
- Ollama Model Missing
   * Cause:
     model not found
   * Debug:
     ```` bash
     ollama pull qwen3:8b
     ````

- Docker Engine Not Running
   * Cause:
     Cannot connect to the Docker daemon
   * Debug:
     ```` bash
     docker ps
     ````

- Kubernetes Cluster Not Running
   * Cause:
     The connection to the server localhost:6443 was refused
   * Debug:
    ```` bash
    minikube start
    ````

- Agent Cannot Execute Kubernetes Commands
   * Cause:
     kubectl is not configured
   * Debug: 
     ```` bash
     kubectl config current-context
     ````                                
