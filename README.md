# FactoryFlow AI

> Protótipo de mini fábrica de software orientada por agentes de IA.

Recebe um requisito em linguagem natural e executa um pipeline multiagente para gerar documentação técnica, código Python e testes automatizados.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_SDK-latest-10a37f?style=flat-square)
![pytest](https://img.shields.io/badge/pytest-passing-green?style=flat-square)

---

## O que é

FactoryFlow AI demonstra, de forma prática, como agentes de IA especializados podem atuar em etapas distintas do ciclo de desenvolvimento de software — transformando um requisito em documentação, plano técnico, código e testes, de forma progressiva e auditável.

---

## Pipeline de agentes

| # | Agente | Responsabilidade |
|---|--------|-----------------|
| 1 | `AnalystAgent` | Interpreta o requisito e gera uma análise estruturada |
| 2 | `ArchitectAgent` | Converte a análise em uma proposta arquitetural |
| 3 | `PlannerAgent` | Transforma a arquitetura em um plano técnico de implementação |
| 4 | `CodeGeneratorAgent` | Gera os arquivos Python do domínio da aplicação |
| 5 | `TestGeneratorAgent` | Gera testes automatizados para o código produzido |
| 6 | `ReporterAgent` | Consolida a execução em um relatório final JSON |

---

## Artefatos gerados

Ao executar o pipeline, o projeto produz:

**Documentação** (`outputs/`)
- `requirements_analysis.md` — análise do requisito
- `architecture.md` — proposta arquitetural
- `tasks.md` — plano técnico de tarefas
- `report.json` — relatório consolidado da execução

**Código** (`generated/`)
- `task.py` — modelo de domínio
- `task_service.py` — camada de serviço
- `test_task_service.py` — testes automatizados

---

## Estrutura do projeto

```
factoryflow-ai/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── orchestrator.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── analyst.py
│   │   ├── architect.py
│   │   ├── planner.py
│   │   ├── code_generator.py
│   │   ├── test_generator.py
│   │   └── reporter.py
│   └── services/
│       ├── __init__.py
│       ├── llm_client.py
│       └── file_writer.py
├── generated/          # código gerado pelo pipeline
├── outputs/            # documentação gerada
├── .env.example
├── requirements.txt
└── README.md
```

---

## Modos de execução

### Mock
Usado quando `OPENAI_API_KEY` está vazia. Permite desenvolver, testar e demonstrar o pipeline sem nenhuma dependência de API externa. Ideal para onboarding e testes locais.

### Real
Usado com uma chave válida configurada. O pipeline chama o modelo configurado para gerar os artefatos com conteúdo real.

---

## Como executar

**1. Criar o ambiente virtual**

```bash
python -m venv .venv
```

**2. Ativar o ambiente**

```bash
# Git Bash
source .venv/Scripts/activate

# PowerShell
.venv\Scripts\Activate.ps1
```

**3. Instalar dependências**

```bash
pip install -r requirements.txt
```

**4. Configurar o ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=        # deixe vazio para rodar em modo mock
OPENAI_MODEL=gpt-4.1-mini
```

**5. Executar o pipeline**

```bash
python -m app.main
```

**6. Rodar os testes gerados**

```bash
pytest generated/test_task_service.py
```

---

## Exemplo de requisito de entrada

> Preciso de um sistema de gerenciamento de tarefas (To-Do List) simples. O usuário deve conseguir cadastrar uma tarefa com título, descrição e prioridade (baixa, média, alta). O sistema deve permitir listar as tarefas pendentes, marcar uma tarefa como concluída e excluir itens. A interface pode ser via linha de comando ou uma API REST básica.

---

## Conceitos demonstrados

- Orquestração de agentes de IA em pipeline sequencial
- Engenharia de contexto entre agentes
- Geração e encadeamento de artefatos intermediários
- Transformação progressiva de requisito em software
- Separação de responsabilidades por agente especializado
- Modo mock para desenvolvimento desacoplado de API externa
- Geração automatizada de testes com pytest
- Consolidação de execução em relatório estruturado

---

## Tecnologias

- Python 3.11+
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [OpenAI SDK](https://github.com/openai/openai-python)
- [pytest](https://docs.pytest.org/)

---

## Limitações atuais

- O modo mock gera saídas pré-definidas
- O código gerado cobre apenas o domínio To-Do List
- A API REST ainda não é gerada como artefato final
- Não há ciclo de auto-correção baseado em falha de testes

---

## Próximos passos

- [ ] Gerar uma API FastAPI real a partir do plano técnico
- [ ] Executar os testes automaticamente após geração
- [ ] Implementar avaliação de qualidade dos artefatos
- [ ] Criar CLI mais robusta ou interface web
- [ ] Suportar múltiplos domínios além de To-Do List

---

## Resumo

FactoryFlow AI é uma prova de conceito de pipeline multiagente para engenharia de software com IA. Agentes especializados transformam um requisito em documentação, plano técnico, código, testes e relatório final — de forma estruturada, auditável e extensível.