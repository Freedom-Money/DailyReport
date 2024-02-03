from .AccountConfig import AccountConfig


class AccountInfo:
    def __init__(self, account: AccountConfig, nick_name: str,  follow_count, fans_count, like_count, video_count) -> None:
        self.account = account
        if account != None:
            self.uid = account.uid
            self.number = account.number
            self.operater = account.operater
            self.remarks = account.remarks
        self.nick_name = nick_name
        self.follow_count = follow_count
        self.fans_count = fans_count
        self.like_count = like_count
        self.video_count = video_count
        self.have_yesterday_data = False

    def set_yesterday(self, yesterday_follow: int, yesterday_fans: int, yesterday_like: int, yesterday_video: int):
        self.follow_change = self.follow_count - yesterday_follow
        self.fans_change = self.fans_count - yesterday_fans
        self.like_change = self.like_change - yesterday_like
        self.video_change = self.video_count - yesterday_video
        self.have_yesterday_data = True

    def toString(self):
        result = """
账号：{0}
关注数量：{1}
粉丝数量：{2}
获赞数量：{3}
视频数量：{4}
""".format(self.nick_name, self.follow_count, self.fans_count, self.like_count, self.video_count)

        if self.have_yesterday_data:
            result += f'关注数量变化：{self.follow_change}\n'
            result += f'粉丝数量变化：{self.fans_change}\n'
            result += f'获赞数量变化：{self.like_change}\n'
            result += f'视频数量变化：{self.video_change}\n'

        return result
