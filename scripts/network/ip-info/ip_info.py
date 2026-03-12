import requests

ip = input("Enter an IP address: ")

url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)
data = response.json()

print("\nIP Information\n")

print(f"IP: {data.get('query')}")
print(f"Country: {data.get('country')}")
print(f"Region: {data.get('regionName')}")
print(f"City: {data.get('city')}")
print(f"ISP: {data.get('isp')}")
print(f"Organization: {data.get('org')}")
