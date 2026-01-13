# Medium Article Generator

An AI-powered agentic workflow that performs comprehensive research (Web, Arxiv, YouTube) and generates a Medium-style article.

## Features

- **Multi-Agent Research:** Uses specialized agents for Arxiv, Wikipedia, HackerNews, Newspaper, and DuckDuckGo.
- **Social Media Insight:** Analyzes YouTube content for broader context.
- **Parallel Execution:** Runs web and social research in parallel for efficiency.
- **Report Generation:** Synthesizes findings into a readable, referenced article.

## Prerequisites

- Python 3.12+
- `uv` (recommended) or `pip`

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd medium-article-generator
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    # or
    pip install -e .
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    # Depending on your model choice (Mistral is default)
    MISTRAL_API_KEY=your_key_here
    # GOOGLE_API_KEY=...
    # OPENROUTER_API_KEY=...
    ```

## Usage

Run the generator with a topic:

```bash
python main.py "The Impact of AI on Global Economics in 2026"
```

The generated report will be saved in the `medium_file` directory.

## Architecture

- `src/agents`: Individual specialized agents.
- `src/teams`: Groups of agents (Research Team, YouTube Team).
- `src/workflow`: Orchestrates the teams and the final report generator.
