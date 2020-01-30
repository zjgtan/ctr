# coding: utf8
import os
import csv

class AdFeature:
    def __init__(self):
        self.cateId = 0
        self.campaignId = 0
        self.customer = 0
        self.brand = 0
        self.price = 0.


class AdFeatureManager:
    def __init__(self, dataPath):
        self.adFeatureDict = {}
        self.dataPath = dataPath

        self.init()

    def init(self):
        with open(os.path.join(self.dataPath, "ad_feature.csv")) as adFeatureFile:
            adFeatureReader = csv.DictReader(adFeatureFile)
            for record in adFeatureReader:
                adFeature = self.parseRecord(record)
                self.adFeatureDict[int(record["adgroup_id"])] = adFeature

    def parseRecord(self, record):
        adFeature = AdFeature()
        adFeature.cateId = int(record["cate_id"])
        adFeature.campaignId = int(record["campaign_id"])
        adFeature.customer = int(record["customer"])
        adFeature.brand = int(record["brand"]) if record["brand"] != "NULL" else 0
        adFeature.price = float(record["price"])

        return adFeature

    def getAdFeature(self, adGroupId):
        return self.adFeatureDict[adGroupId]