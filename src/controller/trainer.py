# coding: utf8
"""
训练类
"""

class Trainer:
    def __init__(self, batchSampleService, network, optimizer, numEpoch, batchSize):
        self.batchSampleService = batchSampleService
        self.network = network
        self.optimizer = optimizer

        self.numEpoch = numEpoch
        self.batchSize = batchSize

    def train(self):
        for epoch in range(self.numEpoch):
            self.trainLoop()
            self.evaluate()

    def trainLoop(self):
        for stepId, batchSample in enumerate(self.batchSampleService.nextBatch(True, self.batchSize)):
            self.optimizer.zero_grad()
            preds = self.network(batchSample)
            loss = self.network.criterion(preds, batchSample.labels)
            loss.backward()
            self.optimizer.step()

            if stepId % 100 == 0:
                print("batch: %d, loss: %f" % (stepId, loss.item()))

    def evaluate(self):
        pass


