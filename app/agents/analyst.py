from app.services.llm_client import LLMClient


class AnalystAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def run(self, requirement_text: str) -> str:
        system_prompt = """
Você é um Analista de Requisitos de software.
Sua tarefa é transformar um requisito em linguagem natural em uma especificação objetiva e útil para desenvolvimento.

Responda em português.
Organize a resposta com as seções abaixo:

1. Objetivo do sistema
2. Atores envolvidos
3. Entidades principais
4. Regras de negócio
5. Endpoints sugeridos
6. Critérios de aceitação
7. Riscos ou ambiguidades

Se algo não estiver claro, sinalize como ambiguidade.
Não invente detalhes excessivos.
"""

        user_prompt = f"""
Analise o requisito abaixo e produza uma especificação clara:

REQUISITO:
{requirement_text}
"""

        return self.llm_client.generate(system_prompt, user_prompt)