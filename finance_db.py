import sqlite3

cnxn = sqlite3.connect("finance.db")
cursor = cnxn.cursor()


def write_user(user_name, password):
    cursor.execute("insert into Investor (user_name, password) values (?,?)", (user_name, password))
    cnxn.commit()


def read_user(user_name, password):
    result = cursor.execute("select * from Investor where user_name = ? and password = ?", (user_name, password)).fetchone()
    return result


def read_stock(user_id):
    result = cursor.execute("select * from Stock where investor_id = ?",
                            (user_id,)).fetchall()
    return result


def write_stock(symbol, purchase_price, purchase_date, quantity, investor_id):
    cursor.execute("insert into Stock (symbol, purchase_price, purchase_date, quantity, investor_id) values (?, ?, ?, ?, ?)",
                   (symbol, purchase_price, purchase_date, quantity, investor_id))
    cnxn.commit()


def update_stock(updated_stock: dict, investor_id, stock_id):
    query = "update Stock set "
    last_index = len(updated_stock.keys()) - 1
    for index, attribute in enumerate(updated_stock.keys()):
        if index != last_index:
            query += f"{attribute} = ?, "
        else:
            query += f"{attribute} = ? "
    query += f"where investor_id = {investor_id} and stock_id = {stock_id}"
    cursor.execute(query, tuple(updated_stock.values()))
    cnxn.commit()


def delete_stock(stock_id, investor_id):
    cursor.execute(f"delete from Stock where stock_id ={stock_id} and investor_id = {investor_id}")
    cnxn.commit()