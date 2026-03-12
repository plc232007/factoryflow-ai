from app.agents.analyst import AnalystAgent
from app.agents.architect import ArchitectAgent
from app.agents.planner import PlannerAgent
from app.agents.code_generator import CodeGeneratorAgent
from app.agents.test_generator import TestGeneratorAgent
from app.agents.reporter import ReporterAgent
from app.services.file_writer import FileWriter
from app.services.llm_client import LLMClient


class FactoryOrchestrator:
    def __init__(self):
        self.llm_client = LLMClient()
        self.analyst = AnalystAgent(self.llm_client)
        self.architect = ArchitectAgent(self.llm_client)
        self.planner = PlannerAgent(self.llm_client)
        self.code_generator = CodeGeneratorAgent(self.llm_client)
        self.test_generator = TestGeneratorAgent(self.llm_client)
        self.reporter = ReporterAgent()

    def run(self, requirement_text: str) -> dict:
        analysis = self.analyst.run(requirement_text)
        architecture = self.architect.run(analysis)
        planning = self.planner.run(architecture)
        generated_code = self.code_generator.run(planning)
        generated_tests = self.test_generator.run(planning, generated_code)

        FileWriter.write_text("outputs/requirements_analysis.md", analysis)
        FileWriter.write_text("outputs/architecture.md", architecture)
        FileWriter.write_text("outputs/tasks.md", planning)

        for filename, content in generated_code.items():
            FileWriter.write_text(f"generated/{filename}", content)

        for filename, content in generated_tests.items():
            FileWriter.write_text(f"generated/{filename}", content)

        generated_files = [
            "outputs/requirements_analysis.md",
            "outputs/architecture.md",
            "outputs/tasks.md",
            "generated/task.py",
            "generated/task_service.py",
            "generated/test_task_service.py",
            "outputs/report.json",
        ]

        report_json = self.reporter.run(
            requirement_text=requirement_text,
            mode="mock" if self.llm_client.mock_mode else "real",
            generated_files=generated_files,
        )

        FileWriter.write_text("outputs/report.json", report_json)

        return {
            "status": "success",
            "mode": "mock" if self.llm_client.mock_mode else "real",
            "generated_files": generated_files,
            "analysis": analysis,
            "architecture": architecture,
            "planning": planning,
            "generated_code": generated_code,
            "generated_tests": generated_tests,
            "report": report_json,
        }