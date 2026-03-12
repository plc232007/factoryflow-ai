import json
from datetime import datetime


class ReporterAgent:
    def run(
        self,
        requirement_text: str,
        mode: str,
        generated_files: list[str],
    ) -> str:
        report = {
            "project": "FactoryFlow AI",
            "status": "success",
            "mode": mode,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "requirement_summary": requirement_text,
            "agents_executed": [
                "AnalystAgent",
                "ArchitectAgent",
                "PlannerAgent",
                "CodeGeneratorAgent",
                "TestGeneratorAgent",
            ],
            "generated_files": generated_files,
        }

        return json.dumps(report, indent=2, ensure_ascii=False)