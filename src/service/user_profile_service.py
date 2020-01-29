# coding: utf8

class UserProfileService:
    def __init__(self, userProfileManager):
        self.userProfileManager = userProfileManager

    def getUserProfile(self, userId):
        return self.userProfileManager.getUserProfile(userId)