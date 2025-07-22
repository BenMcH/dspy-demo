# DSPy Demo

A comprehensive demonstration of DSPy (Declarative Self-improving Python) framework, showcasing its core features including signatures, modules, tool integration, evaluation, and optimization.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Docker (for Phoenix observability)

### Installation

1. Clone this repository and navigate to the project directory:
   ```bash
   cd dspy-demo
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Start Phoenix for observability (optional but recommended):
   ```bash
   docker compose up -d
   ```
   Phoenix will be available at http://localhost:6006

### Environment Setup

You'll need API keys for the language models used in the demos. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# For the Home Assistant MCP demo (optional)
HA_URL=your_home_assistant_url
HA_TOKEN=your_home_assistant_token
```

## Notebooks Overview

### 1. demo.ipynb - Core DSPy Concepts

This notebook introduces the fundamental concepts of DSPy:

- **Signatures**: Learn how to define inputs and outputs for your AI modules
  - Simple string-based signatures
  - Typed signatures with validation
  - Class-based signatures with documentation and field descriptions

- **Modules**: Explore different DSPy modules for various AI tasks
  - `dspy.Predict`: Basic zero-shot prediction
  - `dspy.ChainOfThought`: Multi-step reasoning
  - `dspy.ReAct`: Reasoning and action-taking with tools

- **Tool Integration**: See how to create and use custom tools
  - Mathematical operations example
  - Model Context Protocol (MCP) integration with Home Assistant

Start here to understand the building blocks of DSPy programming.

### 2. evaluation.ipynb - Optimization and Evaluation

This notebook demonstrates how to evaluate and optimize DSPy programs:

- **Dataset Preparation**: Working with customer service ticket classification
- **Evaluation Metrics**: Setting up quantitative success measures
- **Optimization**: Using DSPy's SIMBA optimizer to automatically improve performance
- **Performance Comparison**: Before and after optimization results

This is the natural next step after understanding the basics, showing how to systematically improve your AI programs.

## Key Features Demonstrated

- **Declarative Programming**: Write AI logic as structured code rather than prompt strings
- **Modular Design**: Compose different modules to build complex AI workflows
- **Tool Integration**: Connect AI models to external systems and APIs
- **Automatic Optimization**: Let DSPy improve your programs automatically
- **Observability**: Track AI program execution with Phoenix integration

## Dataset

The project includes `Bitext_Sample_Customer_Service_Training_Dataset.csv`, a sample customer service dataset used for demonstrating classification and evaluation capabilities.

## Getting Help

- [DSPy Documentation](https://dspy.ai/)
- [DSPy GitHub Repository](https://github.com/stanfordnlp/dspy)
- [Phoenix Observability Platform](https://phoenix.arize.com/)

## Next Steps

After working through both notebooks, consider:
- Adapting the examples to your specific use case
- Exploring additional DSPy modules and optimizers
- Building more complex multi-step AI programs
- Integrating with your existing systems using MCP or custom tools
