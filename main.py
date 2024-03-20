import ssl
import urllib.request as urllib

def main(url):
    print("Checking connectivity...")

    context = ssl._create_unverified_context() # SSL context that bypasses certificate verification

    try:
        response = urllib.urlopen(url, context=context)
        print(f"Connection to '{url}' established successfully.")
        print(f"HTTP Response Code: {response.getcode()}")
        print("")
    except urllib.error.URLError as e:
        print(f"Failed to establish a connection to '{url}'.")
        print(f"Error: {e.reason}")
        print("")

print("")
print("Site Connectivity Checker")
print("--------------------------")
print("")
input_url = input("Enter the URL to check connectivity: ")
main(input_url)