# AI-Assistant-for-kubernetes-and-docker-using-LangChain-and-Ollama

A simple LangChain agent that uses a local LLM (via Ollama) to answer Kubernetes and Docker questions by calling real kubectl and docker commands as tools.


## What it does

The agent is wired up with two tools:

- `get_pods` — runs `kubectl get pods -A` and returns the output
- `get_docker_containers` — runs `docker ps` and returns the output

You ask a question in natural language; the LLM decides which tool to call and answers based on the live cluster / Docker state.

## Project Layout 

 ```text
AI-assistant-for-kubernetes-and-docker-using-LangChain-and-Ollama/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
│
├── kubernetes/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── LICENSE
```

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally with the `qwen3:8b` model pulled:
  ```bash
  ollama pull qwen3:8b
  ```
- `kubectl` configured against a cluster (for pod queries)
- `docker` running locally (for container queries)

## Setup

```bash
git clone  https://github.com/Abhi-anand735/AI-Assistant-for-kubernetes-and-docker-using-LangChain-and-Ollama.git
cd ai-assistant

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python agent.py
```

Example prompts:

```
Ask your Kubernetes Agent a Question: > show me all pods
Ask your Kubernetes Agent a Question: > what containers are running on docker?
```

## Future Enhancements

- Extend the application to support multiple local LLMs such as Mistral, DeepSeek.
- Develop a graphical user interface that allows users to Chat with the assistant,
  View Kubernetes resources.




