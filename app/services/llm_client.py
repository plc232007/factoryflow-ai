import os
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class LLMClient:
    def __init__(self):
        load_dotenv()

        raw_api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

        placeholder_values = {
            "",
            "sua_chave_aqui",
            "your_api_key_here",
            "sk-xxxxxxxxxxxxxxxxxxxxxxxx",
        }

        self.api_key = raw_api_key
        self.mock_mode = raw_api_key in placeholder_values

        if not self.mock_mode:
            if OpenAI is None:
                raise ImportError(
                    "Pacote 'openai' não está instalado. Instale com: pip install openai"
                )
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        if self.mock_mode:
            return self._mock_generate(system_prompt, user_prompt)

        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.output_text
    
    def _mock_generate(self, system_prompt: str, user_prompt: str) -> str:
        prompt_lower = (system_prompt + "\n" + user_prompt).lower()

        if "analista de requisitos" in prompt_lower:
            return self._mock_requirements_analysis(user_prompt)

        if "arquiteto de software" in prompt_lower:
            return self._mock_architecture(user_prompt)

        if "planejador técnico" in prompt_lower:
            return self._mock_planning(user_prompt)

        if "gerador de código python" in prompt_lower:
            return self._mock_code_generation(user_prompt)

        if "gerador de testes python" in prompt_lower:
            return self._mock_test_generation(user_prompt)

        return (
            "# Resposta Mock\n\n"
            "O sistema está em modo mock. Nenhuma API externa foi chamada.\n"
        )

    def _mock_requirements_analysis(self, user_prompt: str) -> str:
        requirement_text = self._extract_requirement_text(user_prompt)

        return f"""# Análise de Requisitos

## 1. Objetivo do sistema
Desenvolver um sistema com base no requisito informado, permitindo transformar uma necessidade de negócio em uma especificação inicial para desenvolvimento.

## 2. Atores envolvidos
- Usuário final
- Administrador do sistema (se necessário)
- Sistema/API responsável pelo processamento

## 3. Entidades principais
Com base no requisito informado, as entidades mais prováveis são:
- Tarefa
- Usuário
- Status
- Prioridade

## 4. Regras de negócio
- O sistema deve validar os campos obrigatórios.
- Cada tarefa deve possuir título.
- A prioridade deve aceitar valores compatíveis com o requisito.
- O sistema deve permitir listar tarefas pendentes.
- O sistema deve permitir marcar tarefas como concluídas.
- O sistema deve permitir excluir tarefas.

## 5. Endpoints sugeridos
- POST /tasks
- GET /tasks
- GET /tasks/{{id}}
- PUT /tasks/{{id}}
- DELETE /tasks/{{id}}
- PATCH /tasks/{{id}}/complete

## 6. Critérios de aceitação
- O usuário deve conseguir cadastrar uma tarefa válida.
- O sistema deve rejeitar tarefas sem título.
- O usuário deve conseguir listar tarefas pendentes.
- O usuário deve conseguir concluir uma tarefa.
- O usuário deve conseguir excluir uma tarefa.

## 7. Riscos ou ambiguidades
- O requisito não define persistência em banco de dados.
- O requisito não define autenticação.
- O requisito permite CLI ou API REST, então a interface final precisa ser escolhida.
- Não estão definidos filtros adicionais de consulta.

## Requisito original analisado
{requirement_text}

## Observação
Esta resposta foi gerada em **modo mock**, sem chamada a um modelo externo.
"""

    def _mock_architecture(self, user_prompt: str) -> str:
        analysis_text = self._extract_analysis_text(user_prompt)

        return f"""# Proposta de Arquitetura

## 1. Visão geral da arquitetura
A arquitetura sugerida é uma aplicação backend simples, organizada em camadas, com foco em clareza, baixo acoplamento e facilidade de evolução. O sistema pode começar como uma API REST com responsabilidade única de gerenciar tarefas.

## 2. Componentes principais
- Camada de entrada: endpoints ou interface de execução
- Camada de orquestração: coordenação entre agentes e fluxo principal
- Camada de domínio: regras de negócio das tarefas
- Camada de persistência: armazenamento em memória ou arquivo, com possibilidade de evolução para banco de dados
- Camada de testes: validação dos comportamentos principais

## 3. Estrutura sugerida de pastas
```text
app/
├── main.py
├── orchestrator.py
├── agents/
│   ├── analyst.py
│   └── architect.py
├── services/
│   ├── llm_client.py
│   └── file_writer.py
├── domain/
│   └── task_service.py
├── models/
│   └── task.py
```

## 4. Modelos ou entidades principais

**Task**
- id
- title
- description
- priority
- completed
- created_at

## 5. Rotas/endpoints sugeridos
- POST /tasks
- GET /tasks
- GET /tasks/{{id}}
- PUT /tasks/{{id}}
- DELETE /tasks/{{id}}
- PATCH /tasks/{{id}}/complete

## 6. Fluxo básico de funcionamento
1. O usuário envia dados de uma tarefa.
2. O sistema valida os campos obrigatórios.
3. O serviço de domínio processa a solicitação.
4. O sistema salva ou atualiza a tarefa.
5. O resultado é devolvido ao usuário.

## 7. Decisões técnicas
- Python como linguagem principal
- Organização por responsabilidade
- Estrutura simples para facilitar entendimento
- Separação entre agentes, serviços e domínio
- Possibilidade futura de substituir mock por LLM real

## 8. Riscos técnicos e próximos passos
- Definir se a interface final será CLI ou API REST
- Escolher forma de persistência inicial
- Criar testes automatizados
- Adicionar agente gerador de backlog técnico
- Adicionar agente gerador de código

## Base utilizada
{analysis_text}

## Observação
Esta resposta foi gerada em **modo mock**, sem chamada a um modelo externo.
"""
    def _mock_planning(self, user_prompt: str) -> str:
        architecture_text = self._extract_architecture_text(user_prompt)

        return f"""# Plano Técnico Inicial

    ## 1. Objetivo do plano
    Definir uma sequência prática e priorizada de implementação para construir um MVP funcional do sistema proposto.

    ## 2. Entregas do MVP
    - Estrutura base do projeto
    - Modelo de dados principal
    - Serviço de domínio para tarefas
    - Endpoints principais de CRUD
    - Marcação de tarefa como concluída
    - Persistência simples em memória ou arquivo
    - Testes básicos dos fluxos principais

    ## 3. Tarefas técnicas priorizadas
    1. Criar estrutura base de pastas e módulos
    2. Definir modelo Task
    3. Implementar serviço de gerenciamento de tarefas
    4. Criar operações de cadastro e listagem
    5. Criar operação de conclusão de tarefa
    6. Criar operação de exclusão
    7. Adicionar validações de entrada
    8. Criar testes automatizados iniciais
    9. Documentar execução do projeto

    ## 4. Dependências entre tarefas
    - O modelo Task deve existir antes do serviço de domínio
    - O serviço deve existir antes dos endpoints
    - As validações devem acompanhar os endpoints
    - Os testes dependem dos comportamentos principais implementados

    ## 5. Ordem sugerida de implementação
    1. Estrutura base
    2. Modelos
    3. Serviço de domínio
    4. Endpoints
    5. Validações
    6. Testes
    7. Documentação

    ## 6. Critérios de pronto
    - O sistema deve permitir criar tarefas
    - O sistema deve listar tarefas existentes
    - O sistema deve concluir tarefas
    - O sistema deve excluir tarefas
    - O código deve estar organizado por responsabilidade
    - Deve existir documentação mínima para execução

    ## 7. Riscos de execução
    - Escopo crescer além do MVP
    - Mistura entre lógica de domínio e interface
    - Falta de testes nas regras principais
    - Escolha tardia entre CLI e API REST

    ## Base utilizada
    {architecture_text}

    ## Observação
    Esta resposta foi gerada em **modo mock**, sem chamada a um modelo externo.
    """
    def _mock_code_generation(self, user_prompt: str) -> str:
        return """===FILE:task.py===
    from dataclasses import dataclass, field
    from datetime import datetime
    from typing import Optional


    @dataclass
    class Task:
        id: int
        title: str
        description: str
        priority: str
        completed: bool = False
        created_at: datetime = field(default_factory=datetime.utcnow)
        completed_at: Optional[datetime] = None
    ===FILE:task_service.py===
    from datetime import datetime
    from typing import List

    from generated.task import Task


    class TaskService:
        def __init__(self):
            self.tasks: List[Task] = []
            self.next_id = 1

        def create_task(self, title: str, description: str, priority: str) -> Task:
            if not title.strip():
                raise ValueError("Title is required.")

            valid_priorities = {"low", "medium", "high"}
            if priority not in valid_priorities:
                raise ValueError("Priority must be: low, medium, or high.")

            task = Task(
                id=self.next_id,
                title=title,
                description=description,
                priority=priority,
            )
            self.tasks.append(task)
            self.next_id += 1
            return task

        def list_tasks(self) -> List[Task]:
            return self.tasks

        def complete_task(self, task_id: int) -> Task:
            task = self._find_task(task_id)
            task.completed = True
            task.completed_at = datetime.utcnow()
            return task

        def delete_task(self, task_id: int) -> None:
            task = self._find_task(task_id)
            self.tasks.remove(task)

        def _find_task(self, task_id: int) -> Task:
            for task in self.tasks:
                if task.id == task_id:
                    return task
            raise ValueError(f"Task with id {task_id} not found.")
    """
    
    def _mock_test_generation(self, user_prompt: str) -> str:
        return """===FILE:test_task_service.py===
import pytest

from generated.task_service import TaskService


def test_create_task():
    service = TaskService()

    task = service.create_task(
        title="Study Python",
        description="Practice classes and functions",
        priority="high",
    )

    assert task.id == 1
    assert task.title == "Study Python"
    assert task.completed is False


def test_list_tasks():
    service = TaskService()
    service.create_task("Task 1", "First task", "low")
    service.create_task("Task 2", "Second task", "medium")

    tasks = service.list_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_complete_task():
    service = TaskService()
    task = service.create_task("Finish report", "Write the final report", "medium")

    completed_task = service.complete_task(task.id)

    assert completed_task.completed is True
    assert completed_task.completed_at is not None


def test_delete_task():
    service = TaskService()
    task = service.create_task("Delete me", "Temporary task", "low")

    service.delete_task(task.id)

    tasks = service.list_tasks()
    assert len(tasks) == 0


def test_invalid_priority():
    service = TaskService()

    with pytest.raises(ValueError, match="Priority must be: low, medium, or high."):
        service.create_task(
            title="Bad priority",
            description="This should fail",
            priority="urgent",
        )
"""
    
    
    def _extract_architecture_text(self, user_prompt: str) -> str:
        marker = "ARQUITETURA:"
        if marker in user_prompt:
            return user_prompt.split(marker, 1)[1].strip()
        return user_prompt.strip()

    def _extract_requirement_text(self, user_prompt: str) -> str:
        marker = "REQUISITO:"
        if marker in user_prompt:
            return user_prompt.split(marker, 1)[1].strip()
        return user_prompt.strip()

    def _extract_analysis_text(self, user_prompt: str) -> str:
        marker = "ANÁLISE DE REQUISITOS:"
        if marker in user_prompt:
            return user_prompt.split(marker, 1)[1].strip()
        return user_prompt.strip()
    
    