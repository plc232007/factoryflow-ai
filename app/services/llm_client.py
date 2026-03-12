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

    def _extract_requirement_text(self, user_prompt: str) -> str:
        marker = "REQUISITO:"
        if marker in user_prompt:
            return user_prompt.split(marker, 1)[1].strip()
        return user_prompt.strip()