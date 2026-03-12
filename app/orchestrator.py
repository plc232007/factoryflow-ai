from app.agents.analyst import AnalystAgent
from app.services.file_writer import FileWriter
from app.services.llm_client import LLMClient


class FactoryOrchestrator:
    def __init__(self):
        self.llm_client = LLMClient()
        self.analyst = AnalystAgent(self.llm_client)

    def run(self, requirement_text: str) -> dict:
        analysis = self.analyst.run(requirement_text)

        FileWriter.write_text("outputs/requirements_analysis.md", analysis)

        return {
            "status": "success",
            "mode": "mock" if self.llm_client.mock_mode else "real",
            "generated_files": [
                "outputs/requirements_analysis.md"
            ],
            "analysis": analysis,
        }