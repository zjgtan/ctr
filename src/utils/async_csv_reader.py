# coding: utf8
import multiprocessing
import csv
import os


class AsyncCsvReader:
    def __init__(self, csvFile):
        self.csvFile = csvFile

        self.queue = multiprocessing.SimpleQueue()

    def readCsvFile(self):
        with open(self.csvFile) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for record in csvReader:
                self.queue.put(record)
        self.queue.put(None)

    def next(self):
        reader = multiprocessing.Process(target=self.readCsvFile)
        reader.start()

        while True:
            record = self.queue.get()
            if record is None:
                break
            yield record


if __name__ == "__main__":
    acyncCsvReader = AsyncCsvReader("./data/test.csv", 1)
    for record in acyncCsvReader.next():
        print(record)