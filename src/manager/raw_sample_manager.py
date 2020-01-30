# coding: utf8
import csv
import os
import random

from src.utils.async_csv_reader import AsyncCsvReader


class RawSample:
    def __init__(self):
        self.userId = 0
        self.adGroupId = 0
        self.label = 0


class RawSampleManager:
    def __init__(self, dataPath):
        self.trainSampleReader = None
        self.testSampleReader = None
        self.dataPath = dataPath

        self.init()

    def parseRawSample(self, rawSample):
        '''

        '''
        record = [int(rawSample["user"]), int(rawSample["adgroup_id"]), int(rawSample["clk"])]
        return record

    def parseRecord(self, record):
        rawSample = RawSample()

        rawSample.userId = int(record["user"])
        rawSample.adGroupId = int(record["adgroup_id"])
        rawSample.label = int(record["label"])

        return rawSample

    def loadRawSamples(self):
        trainSamples = []
        testSamples = []

        with open(os.path.join(self.dataPath, "raw_sample.csv")) as rawSampleFile:
            rawSampleReader = csv.DictReader(rawSampleFile)

            for rawSample in rawSampleReader:
                record = self.parseRawSample(rawSample)
                if int(rawSample["time_stamp"]) >= 1494604800:
                    testSamples.append(record)
                else:
                    trainSamples.append(record)

        random.shuffle(trainSamples)

        return trainSamples, testSamples

    def init(self):

        if os.path.exists(os.path.join(self.dataPath, "raw_sample_train.csv")) != True or \
                os.path.exists(os.path.join(self.dataPath, "raw_sample_test.csv")) != True:
            trainRawSamples, testRawSamples = self.loadRawSamples()

            trainCsvFile = open(os.path.join(self.dataPath, "raw_sample_train.csv"), "w")
            trainCsvWriter = csv.writer(trainCsvFile)
            trainCsvWriter.writerow(["user", "adgroup_id", "label"])

            testCsvFile = open(os.path.join(self.dataPath, "raw_sample_test.csv"), "w")
            testCsvWriter = csv.writer(testCsvFile)
            testCsvWriter.writerow(["user", "adgroup_id", "label"])

            for record in trainRawSamples:
                trainCsvWriter.writerow(record)
            for record in testRawSamples:
                testCsvWriter.writerow(record)

            trainCsvFile.close()
            testCsvFile.close()

            del trainRawSamples
            del testRawSamples

        self.trainSampleReader = AsyncCsvReader(os.path.join(self.dataPath, "raw_sample_train.csv"))
        self.testSampleReader = AsyncCsvReader(os.path.join(self.dataPath, "raw_sample_test.csv"))

    def nextBatch(self, isTrain, batchSize):
        sampleReader = self.trainSampleReader if isTrain else self.testSampleReader

        batch = []
        for sample in sampleReader.next():
            if len(batch) >= batchSize:
                yield batch
                batch = []
            batch.append(self.parseRecord(sample))
