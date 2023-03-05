import json, sys, requests
def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        numBit = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rJson = r.json()
        amount = numBit * rJson["bpi"]["USD"]["rate_float"]
        print(f"${amount:,.4f}")
    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()