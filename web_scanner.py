import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url)

    print("\nStatus Code:", response.status_code)

    headers = response.headers

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security"
    ]

    print("\nChecking Security Headers...\n")

    for header in security_headers:
        if header in headers:
            print(f"{header} FOUND")
        else:
            print(f"{header} MISSING")

except Exception as e:
    print("Error:", e)