# coding: utf8

import argparse
import sys

import torch

from src.service.basic_batch_sample_service import BasicBatchSampleService
from src.service.youtubenet_batch_sample_service import YoutubeBatchSampleService
from src.controller.trainer import Trainer
from src.network.basicnet import BasicNet
from src.network.youtubenet import YoutubeNet
from src.config.basicnet_config import BasicNetConfig
from src.config.youtubenet_config import YoutubeNetConfig

from src.manager.ad_feature_manager import AdFeatureManager
from src.manager.raw_sample_manager import RawSampleManager
from src.manager.user_profile_manager import UserProfileManager

from src.service.user_profile_service import UserProfileService
from src.service.ad_feature_service import AdFeatureService
from src.service.raw_sample_service import RawSampleService
from src.service.trace_service import TraceService

class Ctr:
    def __init__(self):
        self.args = self.initArgParser()

    def initArgParser(self):
        argParser = argparse.ArgumentParser()
        argParser.add_argument("--network", type=str, required=True)
        argParser.add_argument("--epoch", type=int, required=True)
        argParser.add_argument("--batch_size", type=int, required=True)
        argParser.add_argument("--lr", type=float, required=True)
        argParser.add_argument("--data_path", type=str, required=True)
        argParser.add_argument("--trace_path", type=str, required=True)

        return argParser.parse_args()

    def initAdFeatureService(self):
        return AdFeatureService(AdFeatureManager(self.args.data_path))

    def initRawSampleService(self):
        return RawSampleService(RawSampleManager(self.args.data_path))

    def initUserProfileService(self):
        return UserProfileService(UserProfileManager(self.args.data_path))

    def init(self):
        sys.stderr.write("init ad feature service\n")
        adFeatureService = self.initAdFeatureService()
        sys.stderr.write("init raw sample service\n")
        rawSampleService = self.initRawSampleService()
        sys.stderr.write("init user profile service\n")
        userProfileService = self.initUserProfileService()

        traceService = TraceService(self.args.trace_path)

        sys.stderr.write("init network\n")
        if self.args.network == "basic":
            batchSampleService = BasicBatchSampleService(rawSampleService, userProfileService, adFeatureService)
            network = BasicNet(BasicNetConfig())
            network = network.cuda()
        elif self.args.network == "youtubenet":
            batchSampleService = YoutubeBatchSampleService(rawSampleService, userProfileService, adFeatureService)
            network = YoutubeNet(YoutubeNetConfig())
        else:
            raise ValueError("network error")

        optimizer = torch.optim.Adam(network.parameters(), lr=self.args.lr)
        self.trainer = Trainer(batchSampleService, network, optimizer, traceService, self.args.epoch, self.args.batch_size)

    def start(self):
        self.trainer.train()


if __name__ == "__main__":
    app = Ctr()
    app.init()
    app.start()
