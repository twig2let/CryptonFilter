__author__ = 'twig'

import json

from lib.CryptoCoinChartsApi.CryptoCoinChartsApi import API

class cryptonFilterMain(object):

    api = API()

    # fetch latest coin information
    api.listcoins()

    # clone the json for use later, NOTE: API limit is 60 hits per hour
    with open('../data/data.json', 'w') as f:
        json.dump(api.getjson(), f, ensure_ascii=False)