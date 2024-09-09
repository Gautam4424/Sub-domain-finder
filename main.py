import requests

def check_domain(domain):
    # print("domain : " , domain) 
    try:
        # Try to make a request to the domain
        response = requests.get(f'https://{domain}', timeout=20)
        # print(response)
        # If the status code is successful (200 OK), return True
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_domain_components(domain):
    parts = domain.split('.')
    successful_domains = []

    # Start from the full subdomain and progressively remove the leftmost component
    for i in range(len(parts)-1):
        current_domain = '.'.join(parts[i:])
        # print(current_domain)
        if check_domain(current_domain):
            successful_domains.append(current_domain)

    return successful_domains


def sub_finder(domains):
    print(domains)
    try : 
        if (len(domains)==1):
            print("Domain : " , domains[0])
        else: 
            print("Sub domain  : ",  domains[0].split(".")[0])
    except : 
        print("Domain Not found")
        


# Example 
# domain
domain = "dash.whoisdatacenter.co.in"

# Get the successful domains
successful_domains = get_domain_components(domain)

sub_finder(successful_domains)

