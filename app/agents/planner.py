from app.services.llm_client import LLMClient


class PlannerAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def run(self, architecture_text: str) -> str:
        system_prompt = """
Você é um Planejador Técnico de software.

Sua tarefa é receber uma proposta de arquitetura e transformá-la em um plano de implementação inicial para um MVP.

Responda em português.
Organize a resposta com as seções abaixo:

1. Objetivo do plano
2. Entregas do MVP
3. Tarefas técnicas priorizadas
4. Dependências entre tarefas
5. Ordem sugerida de implementação
6. Critérios de pronto
7. Riscos de execução

Seja objetivo, prático e didático.
Prefira um plano enxuto, mas realista.
"""

        user_prompt = f"""
Com base na arquitetura abaixo, gere um plano técnico inicial para implementação.

ARQUITETURA:
{architecture_text}
"""

        return self.llm_client.generate(system_prompt, user_prompt)