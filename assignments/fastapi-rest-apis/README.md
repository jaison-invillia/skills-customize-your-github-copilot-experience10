# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar uma API REST simples usando o framework FastAPI em Python. Os estudantes vão implementar endpoints para criar, listar e recuperar recursos, além de documentar a API utilizando a interface automática (OpenAPI/Swagger) fornecida pelo FastAPI.

## 📝 Tasks

### 🛠️ Configurar o projeto e rodar a API

#### Description
Crie um ambiente virtual, instale as dependências listadas em `requirements.txt` e inicie a aplicação FastAPI localmente.

#### Requirements
Completed program should:

- Ter um arquivo `starter-code.py` executável que inicia um servidor FastAPI
- As dependências do projeto devem estar em `requirements.txt`
- A API deve expor a documentação automática em `/docs`


### 🛠️ Implementar endpoints básicos de tarefas

#### Description
Implemente endpoints para gerenciar uma lista simples de tarefas (to-do). Não é necessário persistir dados em banco — uma lista em memória é suficiente para esta tarefa.

#### Requirements
Completed program should:

- GET /tasks — retorna a lista de tarefas
- GET /tasks/{id} — retorna uma tarefa específica ou 404 se não existir
- POST /tasks — cria uma nova tarefa (campo: title)
- Responder com JSON e usar Pydantic para validação de entrada/saída


### 🛠️ (Opcional) Adicionar testes e melhorias

#### Description
Adicione testes simples para a API usando `requests` ou `httpx`/`pytest` (opcional).

#### Requirements
Completed program should:

- Incluir pelo menos 1 teste que verifica criação e listagem de tarefas (opcional)

---

### Como entregar

- Suba o código para o repositório do curso na pasta `assignments/fastapi-rest-apis`
- Inclua instruções para rodar no README (ex.: criar virtualenv, pip install -r requirements.txt, uvicorn starter-code:app --reload)

Boa sorte! Pense em boas mensagens de erro e validação de entrada.
