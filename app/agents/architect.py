from app.services.llm_client import LLMClient


class ArchitectAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def run(self, requirements_analysis: str) -> str:
        system_prompt = """
Você é um Arquiteto de Software.

Sua tarefa é receber uma análise de requisitos e transformá-la em uma proposta arquitetural inicial, clara e objetiva.

Responda em português.
Organize a resposta com as seções abaixo:

1. Visão geral da arquitetura
2. Componentes principais
3. Estrutura sugerida de pastas
4. Modelos ou entidades principais
5. Rotas/endpoints sugeridos
6. Fluxo básico de funcionamento
7. Decisões técnicas
8. Riscos técnicos e próximos passos

Não invente complexidade desnecessária.
Prefira uma solução simples, didática e extensível.
"""

        user_prompt = f"""
Com base na análise de requisitos abaixo, proponha uma arquitetura inicial para o sistema.

ANÁLISE DE REQUISITOS:
{requirements_analysis}
"""

        return self.llm_client.generate(system_prompt, user_prompt)