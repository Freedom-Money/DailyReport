class AccountConfig:
    def __init__(self,  number: int, operater: str, uid: str, deviceId: str, remarks: str) -> None:
        """账号配置

        Args:
            uid (str): tiktok uid/账号名
            operater (str): 操作员名字
            number (int): 序号
            deviceId (str): 机号/设备号
            remarks (str): 备注
        """
        self.uid = uid.strip()
        self.operater = operater
        self.number = number
        self.remarks = remarks
        self.deviceId = deviceId
