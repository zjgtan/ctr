# coding: utf8
"""
基线模型样本
"""
import torch

class BasicBatchSample:
    @property
    def userIds(self):
        return self._userIds

    @userIds.setter
    def userIds(self, userIds):
        if isinstance(userIds, list):
            self._userIds = torch.LongTensor(userIds)
        elif isinstance(userIds, torch.LongTensor):
            self._userIds = userIds
        else:
            raise ValueError("userIds Type Error")

    @property
    def adGroupIds(self):
        return self._adGroupIds

    @adGroupIds.setter
    def adGroupIds(self, adGroupIds):
        if isinstance(adGroupIds, list):
            self._adGroupIds = torch.LongTensor(adGroupIds)
        elif isinstance(adGroupIds, torch.LongTensor):
            self._adGroupIds = adGroupIds
        else:
            raise ValueError("adGroupIds Type Error")

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