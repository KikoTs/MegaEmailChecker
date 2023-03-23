# 📧 MegaEmailChecker 🕵️‍♀️

MegaEmailChecker is a simple Python script that verifies if an email from a list has a registration on mega.nz. 

## 🚀 Getting Started

To use this script, follow these simple steps:

1. Clone the repository or download the script.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Create a file named `emails.txt` in the same directory as the script.
4. Add the emails you want to check, each on a new line.
5. Run the script using `python MegaEmailChecker.py`.

## 🛠️ How to Use

The script will check each email from the `emails.txt` file and print the status. 

The status can be one of the following:

- `[-11]`, `[-9]`, or `[-2]`: Invalid email.
- `[{"val":1,"2fa":0}]`: Might be working.
- Anything else: Not Worky Duuno the code.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are always welcome! Please feel free to open an issue or a pull request.

## 📬 Contact

If you have any questions or comments, please feel free to contact me at kiriltsanov12@gmail.com.
