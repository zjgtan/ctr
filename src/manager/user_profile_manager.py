# coding: utf8
import os
import csv

class UserProfile:
    def __init__(self):
        self.cmsSegId = 0
        self.cmsGroupId = 0
        self.finalGenderCode = 0
        self.ageLevel = 0
        self.pvalueLevel = 0
        self.shoppingLevel = 0
        self.occupation = 0
        self.newUserClassLevel = 0

class UserProfileManager:
    def __init__(self, dataPath):
        self.userProfileDict = {}
        self.dataPath = dataPath

        self.init()

    def init(self):
        with open(os.path.join(self.dataPath, "user_profile.csv")) as userProfileFile:
            userProfileReader = csv.DictReader(userProfileFile)
            for record in userProfileReader:
                userProfile = self.parseRecord(record)
                self.userProfileDict[int(record["userid"])] = userProfile

    def parseRecord(self, record):
        userProfile = UserProfile()
        userProfile.cmsSegId = int(record["cms_segid"])
        userProfile.cmsGroupId = int(record["cms_group_id"])
        userProfile.finalGenderCode = int(record["final_gender_code"])
        userProfile.ageLevel = int(record["age_level"])
        userProfile.pvalueLevel = int(record["pvalue_level"]) if record["pvalue_level"] != "" else 0
        userProfile.shoppingLevel = int(record["shopping_level"])
        userProfile.occupation = int(record["occupation"])
        userProfile.newUserClassLevel = int(record["new_user_class_level "]) if record["new_user_class_level "] != "" else 0

        return userProfile

    def getUserProfile(self, userId):
        try:
            return self.userProfileDict[userId]
        except:
            return UserProfile()