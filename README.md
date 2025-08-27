![](https://github.com/aysh34/LLMs/blob/main/llm.png)

## Overview

LLMs is an educational repository focused on learning and building intelligent agents powered by large language models. This repository provides practical examples, tutorials, and progressive stages for understanding LLMs, AI agents, and LLM agents. It's structured to help you start with basic concepts and progressively build more sophisticated agent capabilities.

## Key Features

- Educational progression from basic LLMs to advanced agents
- Stage 1: Basic prompt loops and reasoning patterns
- Stage 2: Function calling and tool integration
- Practical Jupyter notebooks with working examples
- Clear explanations of LLM vs AI agent vs LLM agent concepts
- Hands-on examples using Together AI and other LLM providers
- Startup-focused use cases and business applications

## Prerequisites

- Python 3.10+ (recommend using a virtual environment)
- Jupyter Notebook or JupyterLab for running the examples
- API keys for LLM providers (Together AI, OpenAI, etc.) - see individual notebooks for requirements
- Basic understanding of Python programming

## Quick Start

1. Clone the repository
    ```bash
    git clone https://github.com/aysh34/LLMs.git
    cd LLMs
    ```

2. Create and activate a virtual environment (recommended)
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS / Linux
    source .venv/bin/activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API keys by creating a .env file (example)
    ```
    TOGETHER_API_KEY=your_together_api_key_here
    OPENAI_API_KEY=your_openai_key_here
    ```
    Check individual notebooks for specific API key requirements.

5. Start with the conceptual overview
    ```bash
    jupyter notebook "notebooks/LLM_vs_AI_agent_vs_LLM_agent.ipynb"
    ```

6. Progress through the agent stages
    ```bash
    # Stage 1: Basic prompt loops
    jupyter notebook "agents/Stage1.Basic Prompt Loops/StartupGuideAgent.ipynb"
    
    # Stage 2: Function calling
    jupyter notebook "agents/Stage2.Function Calling (Tool Use via API)/BasicFunctionCalling.ipynb"
    ```

## Project Structure

```
LLMs/
├── agents/                                    # Progressive agent development stages
│   ├── Stage1.Basic Prompt Loops/           # Introduction to agent reasoning loops
│   └── Stage2.Function Calling (Tool Use via API)/  # Advanced agent capabilities
├── notebooks/                                # Educational and conceptual content
├── Generative AI with LangChain/            # LangChain-related examples
├── requirements.txt                          # Python dependencies
├── LICENCE                                   # License file
└── README.md                                 # This file
```

## Contributing

Contributions are welcome. Open an issue for bugs, questions, or feature requests.
