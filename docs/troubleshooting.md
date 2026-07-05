- Python Not Found
   * Error:
     python is not recognized as an internal or external command
   * Debug
     ```` bash
     python --version
     ````

- Virtual Environment Not Activated
   * Error:
     ModuleNotFoundError
   * Debug
     ```` bash
     .venv\Scripts\activate
     ````

- Ollama Not Installed
   * Error:
     Connection refused
   * Debug
    ```` bash
    ollama serve
    ````
- Ollama Model Missing
   * Error:
     model not found
   * Debug
     ```` bash
     ollama pull qwen3:8b
     ````

- Docker Engine Not Running
   * Error:
     Cannot connect to the Docker daemon
   * Debug
     ```` bash
     docker ps
     ````

- Kubernetes Cluster Not Running
   * Error:
     The connection to the server localhost:6443 was refused
   * Debug
    ```` bash
    minikube start
    ````

- Agent Cannot Execute Kubernetes Commands
   * Error:
     kubectl is not configured
   * Debug 
     ```` bash
     kubectl config current-context
     ````                                
