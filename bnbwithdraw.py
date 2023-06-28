from binance.client import Client

api_key = ''
api_secret = ''

client = Client(api_key, api_secret)

# получаем информацию о балансе аккаунта
account = client.get_account()

def withdraw(adress, network, amount):

    withdraw_result = client.withdraw(
        coin='ETH',
        address=adress,
        amount=amount,
        network=network,
        name='Withdraw')

    print(f"Вывели {withdraw_result['amount']} {withdraw_result['asset']} на адрес {withdraw_result['address']}")

def main():


    # выводим баланс для каждой криптовалюты в портфеле
    for asset in account['balances']:
        if float(asset['free']) > 0 or float(asset['locked']) > 0:
            print(f"{asset['asset']}: free - {asset['free']}, locked - {asset['locked']}")

    info = client.get_all_coins_info()
    for coin in info:
        if coin["coin"] == "ETH":
            print(coin)

    amount = 0.03
    network = 'ARBITRUM'
    adress = ''

    #withdraw(adress,network,amount)

if __name__ == "__main__":
    main()
