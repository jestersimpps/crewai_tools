# Reddit Scraper Tool

This repository contains a custom tool for CrewAI that allows you to scrape content from Reddit subreddits. The tool retrieves the top posts from a specified subreddit and collects the post titles, URLs, and comments.

## Getting Started

To use this tool, you'll need to have CrewAI installed and configured. Follow the instructions in the [CrewAI documentation](https://docs.crewai.com/getting-started/) to set up your environment.

### Prerequisites

This tool requires the `praw` library, which is the Python Reddit API Wrapper. You can install it using pip:

`pip install praw`

You'll also need to obtain Reddit API credentials (client ID, client secret, and user agent) to authenticate with the Reddit API. Follow the instructions in the [PRAW documentation](https://praw.readthedocs.io/en/stable/getting_started/authentication.html) to obtain these credentials.

### Usage

To use the `RedditScraper` tool, add the following environment variables to your `.env` file:

```python
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
```

### Tested with

- [ollama/dolphin-mistral] (https://ollama.com/library/dolphin-mistral)
