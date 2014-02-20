__author__ = 'twig'

from lib.CryptoCoinChartsApi.CryptoCoinChartsApi import API

api = API()


coins = api.listcoins()

print(coins)


