# coding: utf8
import csv
import os
import random


class RawSampleManager:
    def __init__(self, dataPath):
        self.trainSamples = []
        self.testSamples = []
        self.dataPath = dataPath

        self.init()

    def parseRecord(self, record):
        record["user"] = int(record["user"])
        record["time_stamp"] = int(record["time_stamp"])
        record["adgroup_id"] = int(record["adgroup_id"])
        record["label"] = 0 if record["nonclk"] == "1" else 1

        return [record["user"], record["adgroup_id"], record["label"]]

    def init(self):
        count = 0
        with open(os.path.join(self.dataPath, "raw_sample.csv")) as rawSampleFile:
            rawSampleReader = csv.DictReader(rawSampleFile)
            for record in rawSampleReader:
                count += 1
                if count == 1000:
                    break
                sample = self.parseRecord(record)
                if int(record["time_stamp"]) >= 1494604800:
                    self.testSamples.append(sample)
                else:
                    self.trainSamples.append(sample)

        random.shuffle(self.trainSamples)

    def nextBatch(self, isTrain, batchSize):
        samples = self.trainSamples if isTrain else self.testSamples

        batch = []
        for sample in samples:
            if len(batch) >= batchSize:
                yield batch
                batch = []
            batch.append(sample)
