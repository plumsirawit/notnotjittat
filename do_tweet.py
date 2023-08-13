import requests
import json
import secret

bearer_token = secret.BEARER_TOKEN

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "notnotjittat"
    return r


def connect_to_endpoint(url):
    response = requests.request("POST", url, auth=bearer_oauth, json={"text": "กราบ สวัสดีครับ"})
    print(response.status_code)
    return response.json()


def main():
    url = "https://api.twitter.com/2/tweets"
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
