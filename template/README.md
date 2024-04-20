<!-- 
STRUCTURE:

1. The title and a brief description of the tool.
2. The "Getting Started" section with a link to the CrewAI documentation.
3. The "Prerequisites" section explaining the required library and API credentials.
4. The "Usage" section with an example of how to create an instance of the `RedditScraper` class and use the `run` method.
5. The "Tested with" section listing the language model the tool has been tested with.
 -->


# Dummy Example Tool

This is a dummy example tool that demonstrates how to create a custom tool for CrewAI. This tool performs a simple task of generating random numbers.

## Getting Started

To use this tool, you'll need to have CrewAI installed and configured. Follow the instructions in the [CrewAI documentation](https://example.com/crewai-docs) to set up your environment.

### Prerequisites

This tool requires the `random` library, which is a built-in Python library for generating random numbers. No additional installation is required.

### Usage

To use the `RandomNumberGenerator` tool, create an instance of the `RandomNumberGenerator` class and call the `generate` method:

```python
from tools.random_number_generator import RandomNumberGenerator

number_generator = RandomNumberGenerator()
random_numbers = number_generator.generate(count=5, start=1, end=100)
print(random_numbers)

```

## Tested with

- [ollama/dolphin-mistral] (https://ollama.com/library/dolphin-mistral)
