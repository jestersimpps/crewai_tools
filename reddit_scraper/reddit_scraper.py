import os
import praw
import time
from crewai_tools import tool


@tool("Reddit scraper")
def reddit_scraper(subreddit: str, max_comments_per_post: int) -> str:
    """
    This tool allows you to scrape content from a specified Reddit subreddit.
    You can provide the subreddit name and the maximum number of comments to retrieve per post.
    The tool will return a list of dictionaries, where each dictionary represents a post and contains the post
    title, URL, and a list of comments.
    Example usage: run('python', 10) don't use the r/ prefix
    """
    reddit = praw.Reddit(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=os.environ.get("REDDIT_USER_AGENT"),
    )
    subreddit = reddit.subreddit(subreddit)

    scraped_data = []

    for post in subreddit.hot(limit=12):
        post_data = {"title": post.title, "url": post.url, "comments": []}

        try:
            post.comments.replace_more(limit=0)  # Load top-level comments only
            comments = post.comments.list()
            if max_comments_per_post is not None:
                comments = comments[:7]

            for comment in comments:
                post_data["comments"].append(comment.body)

            scraped_data.append(post_data)

        except praw.exceptions.APIException as e:
            print(f"API Exception: {e}")
            time.sleep(60)  # Sleep for 1 minute before retrying

    return scraped_data
