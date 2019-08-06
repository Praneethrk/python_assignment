import csv

class Stock:
    def __init__(self, name, symbol, exchange, price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price

    def __str__(self):
        return (f"{self.name}, {self.symbol}, {self.exchange}, {self.price}")

def load_data():
    try:
        with open("stock.csv") as f:
            data = csv.reader(f, delimiter=",")
            stock_list =[]
            line = 0
            for d in data:
                if line == 0:
                    line += 1
                    continue
                stock_list.append(Stock(*d))
        return stock_list
    except Exception as e:
        print(f"{e}")

def clean_data(data):
    clean_stocks = list()
    for stock in data:
        if "K" in stock.price:
            stock.price = float(stock.price.replace("K","")) * 1000
        else:
            stock.price = float(stock.price.replace("K", ""))
        clean_stocks.append(stock)
    return clean_stocks

data = load_data()
stocks = clean_data(data)
for stock in stocks:
    print(stock)