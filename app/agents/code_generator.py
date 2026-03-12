from app.services.llm_client import LLMClient


class CodeGeneratorAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def run(self, planning_text: str) -> dict:
        system_prompt = """
Você é um Gerador de Código Python.

Sua tarefa é receber um plano técnico e gerar dois arquivos Python iniciais para um MVP de gerenciamento de tarefas:

1. task.py
2. task_service.py

Regras:
- Responda em português apenas nas explicações, mas o código deve estar em inglês.
- Retorne a resposta em um formato bem delimitado.
- Gere código simples, limpo e didático.
- Não use bibliotecas externas desnecessárias.
- O arquivo task.py deve conter uma dataclass Task.
- O arquivo task_service.py deve conter uma classe TaskService com operações básicas:
  - create_task
  - list_tasks
  - complete_task
  - delete_task
"""

        user_prompt = f"""
Com base no plano técnico abaixo, gere os arquivos solicitados.

PLANO TÉCNICO:
{planning_text}

Retorne exatamente neste formato:

===FILE:task.py===
<conteúdo do arquivo>

===FILE:task_service.py===
<conteúdo do arquivo>
"""

        response = self.llm_client.generate(system_prompt, user_prompt)
        return self._parse_generated_files(response)

    def _parse_generated_files(self, response_text: str) -> dict:
        files = {}

        markers = ["task.py", "task_service.py"]

        for index, marker in enumerate(markers):
            start_token = f"===FILE:{marker}==="
            start_index = response_text.find(start_token)

            if start_index == -1:
                files[marker] = f"# Arquivo {marker} não foi gerado corretamente.\n"
                continue

            content_start = start_index + len(start_token)

            if index + 1 < len(markers):
                next_token = f"===FILE:{markers[index + 1]}==="
                end_index = response_text.find(next_token, content_start)
                if end_index == -1:
                    content = response_text[content_start:].strip()
                else:
                    content = response_text[content_start:end_index].strip()
            else:
                content = response_text[content_start:].strip()

            files[marker] = content + "\n"

        return files