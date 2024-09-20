import requests

with open("tokens.txt", "r") as file:
    tokens = file.readlines()

print("Select the format type:")
print("1. Email:Pass:Token to Email:Pass")
print("2. Email:Pass:Token to Email:Token")
print("3. Email:Pass:Token to Token")
print("4. Token to Email:Token")
format_type = input("Enter the format type (1, 2, 3, or 4): ")

use_proxy = False
proxies = []

if format_type == "4":
    use_proxy_input = input("Do you want to run the script with proxy? (yes/no): ").strip().lower()
    if use_proxy_input == "yes":
        use_proxy = True
        with open("proxies.txt", "r") as proxy_file:
            proxies = proxy_file.readlines()
        if not proxies:
            print("proxies.txt is empty | Make sure to put your proxies.")
            exit()

with open("formatted_tokens.txt", "w") as output_file:
    for token in tokens:
        token = token.strip()
        
        if format_type == "1":
            parts = token.split(":")
            if len(parts) == 3:
                email, password, token_value = parts
                formatted_token = f"{email}:{password}"
            else:
                print(f"Invalid Format | Make sure it is Email:Pass:Token: {token}")
                continue
        elif format_type == "2":
            parts = token.split(":")
            if len(parts) == 3:
                email, password, token_value = parts
                formatted_token = f"{email}:{token_value}"
            else:
                print(f"Invalid Format | Make sure it is Email:Pass:Token: {token}")
                continue
        elif format_type == "3":
            parts = token.split(":")
            if len(parts) == 3:
                email, password, token_value = parts
                formatted_token = f"{token_value}"
            else:
                print(f"Invalid Format | Make sure it is Email:Pass:Token: {token}")
                continue
        elif format_type == "4":
            if ":" in token:
                print(f"Invalid Format | Make sure it is just the token: {token}")
                continue
            
            url = "https://discord.com/api/v9/users/@me"
            headers = {
                "Authorization": f"{token}"
            }
            
            if use_proxy and proxies:
                proxy = proxies.pop(0).strip()
                proxy_dict = {
                    "http": f"http://{proxy}",
                    "https": f"https://{proxy}"
                }
                response = requests.get(url, headers=headers, proxies=proxy_dict)
            else:
                response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                user_data = response.json()
                email = user_data.get("email")
                if email:
                    formatted_token = f"{email}:{token}"
                else:
                    print(f"Email not found for token: {token}")
                    continue
            else:
                print(f"Error fetching user information for token: {token} - Status code: {response.status_code}")
                print(f"Error message: {response.json().get('message')}")
                continue
        else:
            print("Invalid format type selected.")
            break
        
        output_file.write(formatted_token + "\n")
        
        if format_type == "4":
            token_preview = f"{token[:10]}...{token[-4:]}"
            print(f"Email -> {email} Token -> {token_preview}")

print("Tokens formatted successfully.")
