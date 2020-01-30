# coding: utf8
import torch
from src.sample.youtubenet_batch_sample import YoutubeNetBatchSample
from src.service.basic_batch_sample_service import BasicBatchSampleService


class YoutubeBatchSampleService(BasicBatchSampleService):
    def __init__(self, rawSampleService, userProfileService, adFeatureService):
        super(YoutubeBatchSampleService, self).__init__(rawSampleService, userProfileService, adFeatureService)

    def getSample(self, rawBatchSample):
        batchSample = YoutubeNetBatchSample()
        batchSample.userId = [sample.userId for sample in rawBatchSample]
        batchSample.cmsSegId = [self.userProfileService.getUserProfile(sample.userId).cmsSegId for sample in rawBatchSample]
        batchSample.cmsGroupId = [self.userProfileService.getUserProfile(sample.userId).cmsGroupId for sample in
                                rawBatchSample]
        batchSample.finalGenderCode = [self.userProfileService.getUserProfile(sample.userId).finalGenderCode for sample in
                                rawBatchSample]
        batchSample.ageLevel = [self.userProfileService.getUserProfile(sample.userId).ageLevel for sample in
                                rawBatchSample]
        batchSample.pvalueLevel = [self.userProfileService.getUserProfile(sample.userId).pvalueLevel for sample in
                                rawBatchSample]
        batchSample.shoppingLevel = [self.userProfileService.getUserProfile(sample.userId).shoppingLevel for sample in
                                rawBatchSample]
        batchSample.occupation = [self.userProfileService.getUserProfile(sample.userId).occupation for sample in
                                rawBatchSample]
        batchSample.newUserClassLevel = [self.userProfileService.getUserProfile(sample.userId).newUserClassLevel for sample in
                                rawBatchSample]

        batchSample.adGroupId = [sample.adGroupId for sample in rawBatchSample]

        batchSample.cateId = [self.adFeatureService.getAdFeature(sample.adGroupId).cateId for sample in rawBatchSample]
        batchSample.campaignId = [self.adFeatureService.getAdFeature(sample.adGroupId).campaignId for sample in rawBatchSample]
        batchSample.customer = [self.adFeatureService.getAdFeature(sample.adGroupId).customer for sample in rawBatchSample]
        batchSample.brand = [self.adFeatureService.getAdFeature(sample.adGroupId).brand for sample in rawBatchSample]
        batchSample.price = [self.adFeatureService.getAdFeature(sample.adGroupId).price for sample in rawBatchSample]

        batchSample.label = [sample.label for sample in rawBatchSample]

        return batchSample
        
