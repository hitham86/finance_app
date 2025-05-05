💰 Finance Tracker CLI
A command-line application to manage your personal stock and bond investments, visualize profitability, and keep a log of your financial activities. Built with Python and SQLite for fast, secure, and offline tracking.

📦 Features
🔐 Sign in / Create account

📈 Add / Delete Stocks and Bonds

🧮 Real-time stock profitability tracking

📊 Visualize most profitable investments

📝 Keep logs of transactions and errors

🧠 Smart update flow for existing assets

🛠 Requirements
Python	Supported
3.8	✅
3.9	✅
3.10	✅
3.11	✅

Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
⚙️ Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/finance-tracker-cli.git
cd finance-tracker-cli
Set up environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Create a .env file

env
Copy
Edit
# .env
DATABASE_URL=finance.db
🧪 Usage
bash
Copy
Edit
python main.py
Main Menu
csharp
Copy
Edit
[1] SIGN IN
[2] CREATE ACCOUNT
Account Menu
csharp
Copy
Edit
[1] ADD STOCK
[2] SHOW ACCOUNT
You can:

Add/update stock with ticker, price, date, and quantity

Delete stock entries

View profitability via visualize.py

Track errors in error.log

🧠 Example Workflow
text
Copy
Edit
> SIGN IN
✔ Enter username
🔒 Enter password
✅ Login success...

> ADD STOCK
✔ Ticker: AAPL
✔ Price: 187.23
✔ Date: 05/01/2025
✔ Quantity: 10

> SHOW ACCOUNT
+--------+------------+-----------+----------+
| Ticker | Buy Price  | Date      | Quantity |
+--------+------------+-----------+----------+
| AAPL   | $187.23    | 05/01/25  | 10       |
+--------+------------+-----------+----------+
📈 Visualization
This project supports stock profitability visualization using pandas and matplotlib. Run:

python
Copy
Edit
from visualize import StockDf

df = StockDf(user_id).load()
print(df)
🧾 Logging
Errors and exceptions are automatically logged to error.log:

text
Copy
Edit
Unhandled error in on_message: (<error details>)
🧤 Credits
Created by Hitham Hauter.
