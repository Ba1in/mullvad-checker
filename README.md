# Mullvad Checker

This Python script allows you to check the status and expiration date of Mullvad VPN accounts by providing a list of account numbers. It makes API requests to the Mullvad API and retrieves the account details for each account number.

## Prerequisites

- Python 3.x
- `requests` library
- `colorama` library
- `rich` library

You can install the required libraries by running the following command:

```shell
pip install requests colorama rich
````

## Usage

1. Clone or download the script file `mullvad_checker.py` to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

```shell
python mullvad_checker.py
```

4. The script will prompt you to enter the delay in seconds between each API request. The default value is 10 seconds. You can press Enter to use the default value or enter your desired delay.

5. The script will load the account numbers from the `acc_numbers.txt` file and start checking their status and expiration date.

6. The script will display the status and expiration date of each account number. Active accounts will be marked with a checkmark (✓), and expired accounts will be marked with a cross (✗).

7. The script will also write the details of active accounts to the `active_acc_numbers.txt` file.

8. Once the script finishes checking all the account numbers, it will display a message indicating completion.

9. Press Enter to exit the script.

## Customization

- Account numbers: Create a text file named `acc_numbers.txt` in the same directory as the script. Each line in the file should contain a single account number.

- Output file: The script will write the details of active accounts to the `active_acc_numbers.txt` file. If the file doesn't exist, it will be created. You can customize the output file name by modifying the script.

- Styling: The script uses the `colorama` and `rich` libraries to add colors and styles to the console output. You can modify the styling code in the script to suit your preferences.

## Acknowledgements

This script was created by @ba1in. chatGPT helped too🤭
