import requests


def top_ten(subreddit):
    # Construct the URL for querying the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the titles of the first 10 hot posts from the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    elif response.status_code == 302:
        # If the subreddit is invalid and it redirects, print None
        print(None)
    else:
        # Handle other error cases
        print("Error:", response.status_code)


# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
