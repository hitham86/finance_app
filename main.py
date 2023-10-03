"""
sign in
create account
add a stock
delete a stock
add a bond
delete a bond
visualize ----> most profitable
keep logs
"""
import os
import sqlite3
import time
import finance_db
from getpass import getpass
import general_funcs
from visualize import StockDf

ACTIVE_ACCOUNT = {}
SAVED_TICKER = []


def sign_in():
    user_name: str = input("Enter your user name\n>>>: ")
    print("\U0001F510")
    password = getpass(f" Enter your user password\n>>>: ")
    id, un, pw = finance_db.read_user(user_name, password)
    ACTIVE_ACCOUNT["id"], ACTIVE_ACCOUNT["un"],  ACTIVE_ACCOUNT["pw"] = id, un, pw
    ACTIVE_ACCOUNT["stocks"] = finance_db.read_stock(id)



def create_account():
    user_name: str = input("choose a user name\n>>>: ")
    password = general_funcs.validate_password(getpass(f"\U0001F510 choose a password\n>>>: "))
    finance_db.write_user(user_name, password)
    print("user added successfully")


def update(origin=None) -> None:
    """

    :param origin:
    :return:
    """
    options_map = {
        "1": ("Enter new ticker: ", "symbol"),
        "2": ("Enter new price: ", "purchase_price"),
        "3": ("Enter new date: ", "purchase_date"),
        "4": ("Enter new quantity: ", "quantity")
    }
    new_stock_attributes = {}
    if origin:
        os.system("cls")
        print(f"UPDATE: {SAVED_TICKER[0]}")
        ticker_info = [j for j in [i for i in ACTIVE_ACCOUNT["stocks"] if i[1] == SAVED_TICKER[0]][0]]
        print(f"Stock Purchase Price: ${ticker_info[2]}")
        print(f"Stock Purchase Date: {ticker_info[3]}")
        print(f"Stock Purchase Quantity: {ticker_info[4]}")
        print("="*20)
        user_selections = set(general_funcs.option_validation(input("Can select multiple>>> example(123 or 3 or 1234)\nwould you like to\n[1].UPDATE "
                                "TICKER\n[2].UPDATE PRICE\n[3].UPDATE DATE\n[4].UPDATE QUANTITY\n>>>: ")))
        for i in sorted(user_selections):
            update_input = input(f"{options_map[i][0]}")
            new_stock_attributes[options_map[i][1]] = update_input
        finance_db.update_stock(new_stock_attributes, ACTIVE_ACCOUNT["id"], SAVED_TICKER[1])
    return None


def delete_stock(origin=False):
    if origin:
        finance_db.delete_stock(SAVED_TICKER[1], ACTIVE_ACCOUNT["id"])


def show_stocks():
    df_obj = StockDf(ACTIVE_ACCOUNT["id"])
    print(df_obj.load())


def add_stock():
    def stock_exist():
        user_options = {"1": update, "2": quit, "3": add_stock, "4": menu}
        selection = input(f"{symbol} already exists... would you like to\n[1].UPDATE\n[2].DELETE\n[3].RETRY\n["
                          f"4].RETURN\n>>>: ")
        if selection == "1" or selection == "2":
            SAVED_TICKER.extend([symbol, ACTIVE_ACCOUNT["stocks"][existing_symbols.index(symbol)][0]])
            return user_options[selection](origin=True)
        user_options[selection]()
    try:
        user_id = ACTIVE_ACCOUNT["id"]
        existing_symbols = [i[1] for i in ACTIVE_ACCOUNT["stocks"]]
        symbol = input("Enter the ticker\n>>>: ")
        if symbol not in existing_symbols:
            purchase_price = input("Enter the purchase price\n>>>: ")
            purchase_date = input("enter the date (mm/dd/yyyy)\n>>>: ")
            quantity = input("enter the quantity\n>>>: ")
            finance_db.write_stock(symbol, purchase_price, purchase_date, quantity, investor_id=user_id)
            print("stock added successfully")
        else:
            stock_exist()
    except sqlite3.IntegrityError as e:
        stock_exist()


def menu():
    while True:
        selection = input(
            "would you like to\n[1].ADD STOCK\n[2].SHOW ACCOUNT\n>>>: ")
        if selection == "1":
            add_stock()
        elif selection == "2":
            show_stocks()


def main():
    while True:
        selection = input(
            "would you like to\n[1].SIGN IN\n[2].CREATE ACCOUNT\n>>>: ")
        if selection == "1":
            sign_in()
        if ACTIVE_ACCOUNT:
            print("login success...")
            time.sleep(2)
            os.system("cls")
            menu()


if __name__ == '__main__':
    main()