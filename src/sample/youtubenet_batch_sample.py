# coding: utf8
"""
youtubenet样本
"""
import torch


class YoutubeNetBatchSample:
    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, userId):
        if isinstance(userId, list):
            self._userId = torch.LongTensor(userId)
        elif isinstance(userId, torch.LongTensor):
            self._userId = userId
        else:
            raise ValueError("userIds Type Error")

    @property
    def cmsSegId(self):
        return self._cmsSegId

    @cmsSegId.setter
    def cmsSegId(self, cmsSegId):
        if isinstance(cmsSegId, list):
            self._cmsSegId = torch.LongTensor(cmsSegId)
        elif isinstance(cmsSegId, torch.LongTensor):
            self._cmsSegId = cmsSegId
        else:
            raise ValueError("userIds Type Error")

    @property
    def cmsGroupId(self):
        return self._cmsGroupId

    @cmsGroupId.setter
    def cmsGroupId(self, cmsGroupId):
        if isinstance(cmsGroupId, list):
            self._cmsGroupId = torch.LongTensor(cmsGroupId)
        elif isinstance(cmsGroupId, torch.LongTensor):
            self._cmsGroupId = cmsGroupId
        else:
            raise ValueError("userIds Type Error")

    @property
    def finalGenderCode(self):
        return self._finalGenderCode

    @finalGenderCode.setter
    def finalGenderCode(self, finalGenderCode):
        if isinstance(finalGenderCode, list):
            self._finalGenderCode = torch.LongTensor(finalGenderCode)
        elif isinstance(finalGenderCode, torch.LongTensor):
            self._finalGenderCode = finalGenderCode
        else:
            raise ValueError("userIds Type Error")

    @property
    def ageLevel(self):
        return self._ageLevel

    @ageLevel.setter
    def ageLevel(self, ageLevel):
        if isinstance(ageLevel, list):
            self._ageLevel = torch.LongTensor(ageLevel)
        elif isinstance(ageLevel, torch.LongTensor):
            self._ageLevel = ageLevel
        else:
            raise ValueError("userIds Type Error")

    @property
    def pvalueLevel(self):
        return self._pvalueLevel

    @pvalueLevel.setter
    def pvalueLevel(self, pvalueLevel):
        if isinstance(pvalueLevel, list):
            self._pvalueLevel = torch.LongTensor(pvalueLevel)
        elif isinstance(pvalueLevel, torch.LongTensor):
            self._pvalueLevel = pvalueLevel
        else:
            raise ValueError("userIds Type Error")

    @property
    def shoppingLevel(self):
        return self._shoppingLevel

    @shoppingLevel.setter
    def shoppingLevel(self, shoppingLevel):
        if isinstance(shoppingLevel, list):
            self._shoppingLevel = torch.LongTensor(shoppingLevel)
        elif isinstance(shoppingLevel, torch.LongTensor):
            self._shoppingLevel = shoppingLevel
        else:
            raise ValueError("userIds Type Error")

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        if isinstance(occupation, list):
            self._occupation = torch.LongTensor(occupation)
        elif isinstance(occupation, torch.LongTensor):
            self._occupation = occupation
        else:
            raise ValueError("userIds Type Error")

    @property
    def newUserClassLevel(self):
        return self._newUserClassLevel

    @newUserClassLevel.setter
    def newUserClassLevel(self, newUserClassLevel):
        if isinstance(newUserClassLevel, list):
            self._newUserClassLevel = torch.LongTensor(newUserClassLevel)
        elif isinstance(newUserClassLevel, torch.LongTensor):
            self._newUserClassLevel = newUserClassLevel
        else:
            raise ValueError("userIds Type Error")

    @property
    def adGroupId(self):
        return self._adGroupId

    @adGroupId.setter
    def adGroupId(self, adGroupId):
        if isinstance(adGroupId, list):
            self._adGroupId = torch.LongTensor(adGroupId)
        elif isinstance(adGroupId, torch.LongTensor):
            self._adGroupId = adGroupId
        else:
            raise ValueError("adGroupIds Type Error")

    @property
    def cateId(self):
        return self._cateId

    @cateId.setter
    def cateId(self, cateId):
        if isinstance(cateId, list):
            self._cateId = torch.LongTensor(cateId)
        elif isinstance(cateId, torch.LongTensor):
            self._cateId = cateId
        else:
            raise ValueError("userIds Type Error")

    @property
    def campaignId(self):
        return self._campaignId

    @campaignId.setter
    def campaignId(self, campaignId):
        if isinstance(campaignId, list):
            self._campaignId = torch.LongTensor(campaignId)
        elif isinstance(campaignId, torch.LongTensor):
            self._campaignId = campaignId
        else:
            raise ValueError("userIds Type Error")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, list):
            self._customer = torch.LongTensor(customer)
        elif isinstance(customer, torch.LongTensor):
            self._customer = customer
        else:
            raise ValueError("userIds Type Error")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, list):
            self._brand = torch.LongTensor(brand)
        elif isinstance(brand, torch.LongTensor):
            self._brand = brand
        else:
            raise ValueError("userIds Type Error")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, list):
            self._price = torch.FloatTensor([[p] for p in price])
        elif isinstance(price, torch.FloatTensor):
            self._price = price
        else:
            raise ValueError("userIds Type Error")

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, labels):
        if isinstance(labels, list):
            self._labels = torch.FloatTensor(labels)
        elif isinstance(labels, torch.FloatTensor):
            self._labels = labels
        else:
            raise ValueError("labels Type Error")