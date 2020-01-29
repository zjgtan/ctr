# coding: utf8
import torch.nn as nn
import torch

class BasicNet(nn.Module):
    def __init__(self, config):
        super(BasicNet, self).__init__()

        self.userEmbedding = nn.Embedding(config.numUser,
                                          config.dimUserEmb)
        self.adGroupEmbedding = nn.Embedding(config.numAdGroup,
                                             config.dimAdGroupEmb)
        self.fc1 = nn.Linear(config.dimAdGroupEmb + config.dimUserEmb, config.dimFc1)
        self.fc2 = nn.Linear(config.dimFc1, 1)

        self.criterion = nn.BCELoss()

    def forward(self, batchSample):
        userEmb = torch.squeeze(self.userEmbedding(batchSample.userIds.cuda()), 1)
        adGroupEmb = torch.squeeze(self.adGroupEmbedding(batchSample.adGroupIds.cuda()), 1)
        concatEmb = torch.cat([userEmb, adGroupEmb], 1)
        fc1 = nn.functional.relu(self.fc1(concatEmb))
        return nn.functional.sigmoid(self.fc2(fc1))


if __name__ == "__main__":
    from src.config.basicnet_config import BasicNetConfig
    from src.service.basic_batch_sample_service import BasicBatchSample
    net = BasicNet(BasicNetConfig())
    net.cuda()
    batchSample = BasicBatchSample()
    batchSample.userIds = [[0], [0]]
    batchSample.adGroupIds = [[0], [0]]
    batchSample.labels = [1, 1]

    preds = net(batchSample)

    print(preds)


