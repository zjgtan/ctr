# coding: utf8
"""
训练数据
"""

class RawSampleService:
    def __init__(self, rawSampleManager):
        self.rawSampleManager = rawSampleManager

    def nextBatch(self, isTrain, batchSize):
        for batchSample in self.rawSampleManager.nextBatch(isTrain, batchSize):
            yield batchSample