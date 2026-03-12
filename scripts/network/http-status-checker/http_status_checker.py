import requests


def check_website_status(url):
    """
    Checks the HTTP status of a website.
    """

    try:
        response = requests.get(url)

        print("\nWebsite Status Check")
        print("-----------------------------")

        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Status: Website is reachable.")
        elif response.status_code == 404:
            print("Status: Page not found.")
        elif response.status_code == 500:
            print("Status: Server error.")
        else:
            print("Status: Received response from server.")

        print("-----------------------------\n")

    except requests.exceptions.RequestException as error:
        print("Error while connecting to the website.")
        print(error)


if __name__ == "__main__":

    print("\nHTTP Status Checker")
    print("-----------------------------")

    website = input("Enter website URL (e.g. https://example.com): ")

    check_website_status(website)
