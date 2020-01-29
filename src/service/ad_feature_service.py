# coding: utf8

class AdFeatureService:
    def __init__(self, adFeatureManager):
        self.adFeatureManager = adFeatureManager

    def getAdFeature(self, adGroupId):
        return self.adFeatureManager.getAdFeature(adGroupId)