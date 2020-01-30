# coding: utf8
"""
训练类
"""
from sklearn.metrics import roc_auc_score

class Trainer:
    def __init__(self, batchSampleService, network, optimizer, traceService, numEpoch, batchSize):
        self.batchSampleService = batchSampleService
        self.network = network
        self.optimizer = optimizer

        self.numEpoch = numEpoch
        self.batchSize = batchSize

        self.traceService = traceService

    def train(self):
        for epoch in range(self.numEpoch):
            self.trainLoop()
            self.evaluate()
            self.traceService.updateEpoch()

    def trainLoop(self):
        self.network.train()

        for stepId, batchSample in enumerate(self.batchSampleService.nextBatch(True, self.batchSize)):
            self.optimizer.zero_grad()
            preds = self.network(batchSample)
            loss = self.network.criterion(preds, batchSample.labels.cuda())
            loss.backward()
            self.optimizer.step()

            self.traceService.traceTrainLoss(loss.item())

            if stepId % 1000 == 0:
                print("Batch: %d, Loss: %f" % (stepId, loss.item()))

    def evaluate(self):
        self.network.eval()

        testLoss = []
        testPreds = []
        testLabels = []
        for stepId, batchSample in enumerate(self.batchSampleService.nextBatch(False, 10000)):
            preds = self.network(batchSample)
            loss = self.network.criterion(preds, batchSample.labels.cuda())
            testLoss.append(loss.item())
            for pred in preds.cpu().tolist():
                testPreds.append(pred[0])

            for label in batchSample.labels.tolist():
                testLabels.append(label)

        testAuc = roc_auc_score(testLabels, testPreds)
        self.traceService.traceTestLoss(sum(testLoss) / len(testLoss))
        self.traceService.traceTestAuc(testAuc)






