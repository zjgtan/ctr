# coding: utf8
"""
指标监控类
"""

from torch.utils.tensorboard import SummaryWriter

class TraceService:
    def __init__(self, tracePath):
        self.writer = SummaryWriter(tracePath)
        self.globalEpoch = 0
        self.globalStep = 0
        self.initScalar()

    def initScalar(self):
        self.trainLoss = []
        self.testLoss = 0.
        self.testAuc = 0.


    def traceTrainLoss(self, loss):
        self.trainLoss.append(loss)

        if len(self.trainLoss) % 100 == 0:
            self.writer.add_scalar("Loss/training", self.trainLoss[-1], self.globalStep)

        self.globalStep += 1

    def traceTestLoss(self, loss):
        self.testLoss = loss

    def traceTestAuc(self, auc):
        self.testAuc = auc

    def updateEpoch(self):
        trainLoss = sum(self.trainLoss) / len(self.trainLoss)

        self.writer.add_scalar("Loss/train", trainLoss, self.globalEpoch)
        self.writer.add_scalar("Loss/test", self.testLoss, self.globalEpoch)
        self.writer.add_scalar("Auc/test", self.testAuc, self.globalEpoch)

        self.globalEpoch += 1

        self.initScalar()


if __name__ == "__main__":
    traceService = TraceService("./run/test")

    for _ in range(10):
        traceService.traceTrainLoss(0.1)
        traceService.traceTestLoss(0.3)
        traceService.traceTestAuc(0.65)
        traceService.updateEpoch()