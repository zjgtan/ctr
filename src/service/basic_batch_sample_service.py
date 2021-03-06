# coding: utf8
import torch

from src.sample.basic_batch_sample import BasicBatchSample

class BasicBatchSampleService:
    def __init__(self, rawSampleService, userProfileService, adFeatureService):
        self.rawSampleService = rawSampleService
        self.userProfileService = userProfileService
        self.adFeatureService = adFeatureService

    def nextBatch(self, isTrain, batchSize):
        for rawBatchSample in self.rawSampleService.nextBatch(isTrain, batchSize):
            batchSample = self.getSample(rawBatchSample)
            yield batchSample

    def getSample(self, rawBatchSample):
        basicBatchSample = BasicBatchSample()
        '''
        basicBatchSample.userIds = [sample.userId for sample in rawBatchSample]
        basicBatchSample.adGroupIds = [sample.adGroupId for sample in rawBatchSample]
        basicBatchSample.labels = [sample.label for sample in rawBatchSample]
        '''
        basicBatchSample.userIds = [sample.userId for sample in rawBatchSample]
        basicBatchSample.adGroupIds = [sample.adGroupId for sample in rawBatchSample]
        basicBatchSample.labels = [sample.label for sample in rawBatchSample]
        return basicBatchSample
