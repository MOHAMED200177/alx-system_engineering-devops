import requests


def number_of_subscribers(subreddit):
    # Construct the URL for querying the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'Custom User Agent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 302:
        # If the subreddit is invalid and it redirects, return 0
        return 0
    else:
        # Handle other error cases
        print("Error:", response.status_code)
        return 0


# Example usage:
subreddit_name = "python"
print(
    f"The number of subscribers in r/{subreddit_name}: {number_of_subscribers(subreddit_name)}")
