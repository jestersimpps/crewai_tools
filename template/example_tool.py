from crewai_tools import tool


@tool("Tool Name")
def tool_name(param1, param2) -> str:
    """
    Tool description
    This tool allows you to perform a specific task or operation.
    You can provide the necessary inputs and the tool will return the desired output.
    Example usage: run('<tool-name>', <input1>, <input2>)
    """
    # Your code here
    # Use os.environ.get("KEY") to get environment variables or API keys 