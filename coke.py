def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        if coin in accepted_coins:
            amount_due -= coin

    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
