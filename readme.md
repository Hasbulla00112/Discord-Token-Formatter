# Token Formatter 

This Python script processes tokens from a file named tokens.txt and formats them based on the user's selection. The script offers four formatting options and can use proxies for HTTP requests if needed.

## Description

The script reads tokens from the tokens.txt file and provides the following formatting options:

1. **Email:Pass:Token to Email:Pass**
2. **Email:Pass:Token to Email:Token**
3. **Email:Pass:Token to Token**
4. **Token to Email:Token**

## Installation

Download - [Token-Formatter](https://github.com/Hasbulla00112/Token-Formatter/releases/download/v1.0.2/Token.Formatter.zip)
Extract the archive and run the script.

### Features

- **Option 1:** Converts `Email:Pass:Token` to `Email:Pass`.
- **Option 2:** Converts `Email:Pass:Token` to `Email:Token`.
- **Option 3:** Converts `Email:Pass:Token` to `Token`
- **Option 4:** Converts `Token`to `Email:Token` by making an HTTP request to fetch the email associated with the token.

### Proxy Support

For option 4, the script can use proxies for HTTP requests. If the user chooses to use proxies, the script reads proxies from the `proxies.txt` file. The proxies should be in the format `user:pass@ip:port`. If the `proxies.txt` file is empty, the script will stop and display an error message.

### Usage
  1. **Prepare the `tokens.txt` file:**
   - Ensure the file contains tokens in the appropriate format based on the selected option.
  2. **Run the script:**
   - The script will prompt you to select a formatting option.
   - For option 4, the script will ask if you want to use proxies.
  3. **Output:**
   - The formatted tokens will be saved in the `formatted_tokens.txt` file.
   - A success message will be displayed once the formatting is complete.

### Notes

- Ensure the `tokens.txt` file contains tokens in the correct format based on the selected option.
- If using proxies, ensure the `proxies.txt` file contains valid proxies in the format `user:pass@ip:port`.
