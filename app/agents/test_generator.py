from app.services.llm_client import LLMClient


class TestGeneratorAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def run(self, planning_text: str, generated_code: dict) -> dict:
        system_prompt = """
Você é um Gerador de Testes Python.

Sua tarefa é receber um plano técnico e arquivos de código já gerados, e então criar um arquivo de teste automatizado.

Regras:
- Gere um arquivo chamado test_task_service.py
- Use pytest
- O teste deve validar:
  - criação de tarefa
  - listagem de tarefas
  - conclusão de tarefa
  - exclusão de tarefa
  - erro para prioridade inválida
- Retorne no formato delimitado especificado pelo usuário
"""

        code_context = "\n\n".join(
            [f"ARQUIVO: {filename}\n{content}" for filename, content in generated_code.items()]
        )

        user_prompt = f"""
Com base no plano técnico abaixo e no código já gerado, crie os testes automatizados.

PLANO TÉCNICO:
{planning_text}

CÓDIGO GERADO:
{code_context}

Retorne exatamente neste formato:

===FILE:test_task_service.py===
<conteúdo do arquivo>
"""

        response = self.llm_client.generate(system_prompt, user_prompt)
        return self._parse_generated_files(response)

    def _parse_generated_files(self, response_text: str) -> dict:
        marker = "===FILE:test_task_service.py==="
        start_index = response_text.find(marker)

        if start_index == -1:
            return {
                "test_task_service.py": "# Arquivo test_task_service.py não foi gerado corretamente.\n"
            }

        content = response_text[start_index + len(marker):].strip()
        return {"test_task_service.py": content + "\n"}