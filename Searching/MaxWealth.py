# https://leetcode.com/problems/richest-customer-wealth/description/
def richestPerson(accounts):
    wealthRichest = 0
    for person in range(len(accounts)):
        totalMoney = 0
        for account in range(len(accounts[person])):
            totalMoney = totalMoney + accounts[person][account]
        if totalMoney > wealthRichest:
            wealthRichest = totalMoney

    return wealthRichest


if __name__ == "__main__":
    accounts = [[1, 2, 3], [3, 2, 2]]
    print(richestPerson(accounts))
