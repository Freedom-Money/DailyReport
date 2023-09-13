
# 功能

1. 监控TikTok账号数据，每日20:20以后开始获取，结果发送到微信。



# 使用方法

## 1. Fork本项目到个人账号下

## 2. 设置WxPusher UID

1. 微信点击https://wxpusher.zjiecode.com/wxuser/?type=1&id=51499#/follow。关注公众号。
2. 公众号右下角【我的】获取uid。
3. 【Settings】-【Security】-【Secrets and variables】-【Actions】-【Variables】处，添加变量。名称为【WECHAT_UID】,内容为上步骤获取的uid。

## 3. 设置被监控账号列表

1. 添加变量，名称为【TIKTOK_ACCOUNTS】，内容为用户id列表（以英文逗号间隔），如“yuandao5,yuandd39,yuanaab,yuanyuan4096”。