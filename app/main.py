from app.orchestrator import FactoryOrchestrator


def main():
    print("=== FactoryFlow AI ===")
    print("Mini fábrica de software com agentes de IA\n")

    requirement_text = input("Descreva o requisito do sistema:\n> ")

    orchestrator = FactoryOrchestrator()
    result = orchestrator.run(requirement_text)

    print("\n=== Resultado ===")
    print(f"Status: {result['status']}")
    print(f"Modo de execução: {result['mode']}")

    print("\nArquivos gerados:")
    for file in result["generated_files"]:
        print(f"- {file}")

    print("\n=== Relatório final ===")
    print(result["report"])


if __name__ == "__main__":
    main()