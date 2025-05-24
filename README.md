# ADK demo

This project, named **ADK demo**, is built using the Agent Development Kit (ADK).

## Installation

To set up the environment and install ADK, follow these steps:

1. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv

   # Activate the virtual environment
   # On Windows PowerShell:
   .venv\Scripts\Activate.ps1
   ```

2. **Install ADK**

   ```bash
   pip install google-adk
   ```

   For more details, refer to the [ADK Installation Guide](https://google.github.io/adk-docs/get-started/installation/).

## Running the Agent

To run your agent, navigate to the parent directory of your agent project and use one of the following methods:

1. **Dev UI**

   Launch the development UI with the following command:

   ```bash
   adk web
   ```

   Open the provided URL (usually `http://localhost:8000`) in your browser to interact with your agent.

2. **Terminal**

   Run the agent directly in the terminal:

   ```bash
   adk run multi_tool_agent
   ```

   For more details, refer to the [ADK Quickstart Guide](https://google.github.io/adk-docs/get-started/quickstart/#run-your-agent).
