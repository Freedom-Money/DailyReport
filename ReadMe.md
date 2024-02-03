
# 功能

1. 监控TikTok账号数据，每日20:20以后开始获取，结果发送到微信。



# 使用方法

## 1. Fork本项目到个人账号下

## 2. 【选填】设置WxPusher UID

1. 微信中点击  https://wxpusher.zjiecode.com/wxuser/?type=1&id=51499#/follow  关注公众号。
2. 公众号右下角【我的】获取uid。
3. 【Settings】-【Security】-【Secrets and variables】-【Actions】-【Variables】处，添加变量。名称为【WECHAT_UID】,内容为上步骤获取的uid。

## 3. 【选填】设置接受信息邮箱

1. 添加环境变量，名称为【RECEIVE_EMAIL】，其中设置接收日报的邮箱，如果需要设置多个，中间以英文逗号间隔。

## 3. 设置被监控账号列表

1. 创建语雀公开文档，在其中添加表格，设置四列，内容分别为序号、操作员姓名、账号uid、备注四项内容。参考：https://www.yuque.com/1dao/ym0va6/ogsadgl75tn5ma7f
2. 添加环境变量，名称为【YUQUE_DOC_UID】，内容为语雀文档的uid（在上面的案例中为【ogsadgl75tn5ma7f】）

## 4. 设置发送邮箱账号密码

1. 添加环境变量，名称为【SEND_EMAIL】，设置发送邮件的邮箱账号（outlook邮箱）。
2. 添加环境变量，名称为【SEND_EMAIL_PASSWORD】，设置发送邮件的邮箱密码。
3. 邮箱账号密码：https://www.yuque.com/1dao/ym0va6/enlgqkwn0rg1suqd

## 5. 设置Github Token

1. 用户中心选择"Settings"、"Developer settings"，然后选择 "Personal access tokens"、"Tokens(classic)"。点击 "Generate new token"，选择需要的权限（通常需要 repo 权限，如果不确定就全选）。
2. 复制生成的token。
3. GitHub 仓库中，点击右上角的 "Settings"。在左侧导航栏中选择 "Secrets"，然后点击 "New repository secret"。给 secret 一个名称（GH_TOKEN），将之前生成的 Personal Access Token 复制粘贴到 "Value" 字段中。保存