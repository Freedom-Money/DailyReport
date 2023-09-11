import enums

class UserInfo:
    def __init__(self, username: str, nickname: str, platform: enums.PlatformType, date, followCount, fansCount, likeCount, videoCount) -> None:
        self.username = username
        self.nickname = nickname
        self.platform = platform
        self.date = date,
        self.followCount = followCount
        self.fansCount = fansCount
        self.likeCount = likeCount
        self.videoCount = videoCount
        pass

    def toString(self):
        result = """账号：{0}
关注数量：{1}
粉丝数量：{2}
点赞数量：{3}
视频数量：{4}

""".format(self.nickname, self.followCount, self.fansCount, self.likeCount, self.videoCount)
        return result
