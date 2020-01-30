# coding: utf8
"""
youtubeNet
"""

import torch.nn as nn
import torch

class YoutubeNet(nn.Module):
    def __init__(self, config):
        super(YoutubeNet, self).__init__()

        self.userEmbedding = nn.Embedding(config.numUser,
                                          config.dimEmb)

        self.cmsSegEmbedding = nn.Embedding(config.numCmsSeg,
                                            config.dimEmb)

        self.cmsGroupEmbedding = nn.Embedding(config.numCmsGroup,
                                            config.dimEmb)

        self.finalGenderCodeEmbedding = nn.Embedding(config.numFinalGenderCode,
                                            config.dimEmb)

        self.ageLevelEmbedding = nn.Embedding(config.numAgeLevel,
                                            config.dimEmb)

        self.pvalueLevelEmbedding = nn.Embedding(config.numPvalueLevel,
                                            config.dimEmb)

        self.shoppingLevelEmbedding = nn.Embedding(config.numShoppingLevel,
                                            config.dimEmb)

        self.occupationEmbedding = nn.Embedding(config.numOccupation,
                                            config.dimEmb)

        self.newUserClassLevelEmbedding = nn.Embedding(config.numNewUserClassLevel,
                                            config.dimEmb)
        
        self.adGroupEmbedding = nn.Embedding(config.numAdGroup,
                                             config.dimEmb)

        self.cateIdEmbedding = nn.Embedding(config.numCateId,
                                            config.dimEmb)

        self.campaignIdEmbedding = nn.Embedding(config.numCampaignId,
                                            config.dimEmb)

        self.customerEmbedding = nn.Embedding(config.numCustomer,
                                            config.dimEmb)

        self.brandEmbedding = nn.Embedding(config.numBrand,
                                            config.dimEmb)

        self.fc1 = nn.Linear(config.dimEmb * 14 + 1, config.dimFc1)
        self.fcOutput = nn.Linear(config.dimFc1, 1)

        self.criterion = nn.BCELoss()

    def forward(self, batchSample):
        userEmb = torch.squeeze(self.userEmbedding(batchSample.userId.cuda()), 1)
        cmsSegEmb = torch.squeeze(self.cmsSegEmbedding(batchSample.cmsSegId.cuda()), 1)
        cmsGroupEmb = torch.squeeze(self.cmsGroupEmbedding(batchSample.cmsGroupId.cuda()), 1)
        finalGenderCodeEmb = torch.squeeze(self.finalGenderCodeEmbedding(batchSample.finalGenderCode.cuda()), 1)
        ageLevelEmb = torch.squeeze(self.ageLevelEmbedding(batchSample.ageLevel.cuda()), 1)
        pvalueLevelEmb = torch.squeeze(self.pvalueLevelEmbedding(batchSample.pvalueLevel.cuda()), 1)
        shoppingLevelEmb = torch.squeeze(self.shoppingLevelEmbedding(batchSample.shoppingLevel.cuda()), 1)
        occupationEmb = torch.squeeze(self.occupationEmbedding(batchSample.occupation.cuda()), 1)
        newUserClassLevelEmb = torch.squeeze(self.newUserClassLevelEmbedding(batchSample.newUserClassLevel.cuda()), 1)

        adGroupEmb = torch.squeeze(self.adGroupEmbedding(batchSample.adGroupId.cuda()), 1)
        cateEmb = torch.squeeze(self.cateIdEmbedding(batchSample.cateId.cuda()), 1)
        campaignEmb = torch.squeeze(self.campaignIdEmbedding(batchSample.campaignId.cuda()), 1)
        customerEmb = torch.squeeze(self.customerEmbedding(batchSample.customer.cuda()), 1)
        brandEmb = torch.squeeze(self.brandEmbedding(batchSample.brand.cuda()), 1)

        concatEmb = torch.cat([userEmb,
                               adGroupEmb,
                               cmsSegEmb,
                               cmsGroupEmb,
                               finalGenderCodeEmb,
                               ageLevelEmb,
                               pvalueLevelEmb,
                               shoppingLevelEmb,
                               occupationEmb,
                               newUserClassLevelEmb,
                               cateEmb,
                               campaignEmb,
                               customerEmb,
                               brandEmb,
                               batchSample.price.cuda()], 1)

        fc1 = nn.functional.relu(self.fc1(concatEmb))
        return nn.functional.sigmoid(self.fcOutput(fc1))


if __name__ == "__main__":
    from src.config.youtubenet_config import YoutubeNetConfig
    from src.sample.youtubenet_batch_sample import YoutubeNetBatchSample

    net = YoutubeNet(YoutubeNetConfig())
    net.cuda()
    batchSample = YoutubeNetBatchSample()
    batchSample.userId = [[0], [0]]
    batchSample.adGroupId = [[0], [0]]
    batchSample.labels = [1, 1]

    preds = net(batchSample)

    print(preds)

