__author__ = 'twig'

import json

JSON_PATH = '../data/data.json'

class Filter(object):

    def findMax(self):
        json = self._readJSON()
        currentValue = float(json[0]['price_btc'])
        maxValueObject = json[0]

        for entry in json:
            if currentValue < float(entry['price_btc']):
                maxValueObject = entry

        return maxValueObject

    def _readJSON(self):
        return json.load(open(JSON_PATH, mode='r'))
