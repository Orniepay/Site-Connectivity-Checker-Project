import ssl
import urllib.request as urllib

def main(url):
    """
    Checks the connectivity to a specified URL.

    This function attempts to establish a connection to the given URL to check 
    its accessibility over the internet. It bypasses SSL certificate verification 
    for HTTPS connections, which is useful for testing purposes but not 
    recommended for secure or production environments. The function reports 
    back the HTTP response code if the connection is successful, or the error 
    if it fails to connect.

    Parameters:
    url (str): The URL to be checked for connectivity.

    Returns:
    None: The function prints the result of the connectivity check to the console
    and does not return a value.
    """
    
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