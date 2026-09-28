"""given price on n days buy price and sell on later day
find max profit, can only make one transaction"""

def main():
    prices = [5, 2, 9, 1, 6, 8]
    cp = 0
    min_price = 999999
    prof_sold_today = 0
    best = 0
    for price in prices:
        cp = price
        if cp < min_price:
            min_price = cp
        prof_sold_today = cp - min_price
        if prof_sold_today > best:
            best = prof_sold_today


    print(f"Best price: {best}")

    












if __name__ == "__main__":
    main()