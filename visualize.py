import numpy
import pandas as pd
import requests
import finance_db
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API")


class StockDf:
    def __init__(self, investor_id):
        self.investor_id: int = investor_id

    def load(self):
        df: pd.DataFrame = pd.read_sql(f"select * from Stock where investor_id={self.investor_id}", finance_db.cnxn)
        df.drop(["stock_id", "investor_id"], inplace=True, axis=1)

        df["current_price"] = numpy.NAN

        for ticker in df["symbol"].tolist():
            end_point = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={API_KEY}"
            response: dict = requests.get(end_point).json()
            if "error" not in response.values():
                df.loc[df["symbol"] == ticker, "current_price"] = numpy.float64(response.get('price'))

        df["profit/loss"] = (df["quantity"] * df["current_price"]) - (df["quantity"] * df["purchase_price"])
        return df


