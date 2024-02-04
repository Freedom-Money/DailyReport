class AccountConfig:
    def __init__(self, uid: str, operater: str, number: int, remarks: str, deviceId: str) -> None:
        """账号配置

        Args:
            uid (str): tiktok uid/账号名
            operater (str): 操作员名字
            number (int): 序号
            deviceId (str): 机号/设备号
            remarks (str): 备注
        """
        self.uid = uid
        self.operater = operater
        self.number = number
        self.remarks = remarks
        self.deviceId = deviceId
