import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Argument must be a number")

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=274e89e78a634e72cf6d9ca780866d0f5a28ac36fe76337749226a2ab75f22ed"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data["data"]["priceUsd"]
    except requests.RequestException:
        sys.exit("Network Error")
    except (ValueError, TypeError, KeyError):
        sys.exit("API Error")

    try:
        total = amount*float(price)
    except (ValueError, TypeError):
        sys.exit("Wrong type")

    print(f"total: {total:,.4f}")

if __name__ == "__main__":
    main()