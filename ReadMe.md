
# 功能

1. 监控TikTok账号数据，每日20:20以后开始获取，结果发送到微信。



# 使用方法

## 1. Fork本项目到个人账号下

## 2. 设置变量被监控账号列表

### 2.1. 获取WxPusher UID
1. 微信中点击  https://wxpusher.zjiecode.com/wxuser/?type=1&id=51499#/follow  关注公众号。
2. 公众号右下角【我的】获取uid。
### 2.2. 设置被监控账号列表
1. 创建语雀公开文档，在其中添加表格，设置四列，内容分别为序号、操作员姓名、账号uid、备注四项内容。参考：https://www.yuque.com/1dao/ym0va6/ogsadgl75tn5ma7f
### 2.3. 设置Actions环境变量
1. 在github【Settings】-【Security】-【Secrets and variables】-【Actions】-【Variables】处，新增变量，名称为SETTINGS，内容设置如下：
```
[
    {
        "name":"name1",
        "settings_url":"https://www.yuque.com/*****",
        "receive_email":[
            "email1@163.com",
            "email2@163.com"
        ],
        "wechat_uid":"UID_*****"
    },
    {
        "name":"name2",
        "settings_url":"xxxx",
        "receive_email":[
            "email1",
            "email2"
        ]
    }
]
```
以上列表中，每项代表一组：
* name与yml名称完全匹配，代表由哪个yml触发。
* settings_url设置为语雀表格配置链接。
* receive_email设置为接收信息邮箱，可以设置多个。
* wechat_uid设置为WxPusher的uid，不设置则不发送。
### 2.4. 配置定时yml
1. 进入.github/workflows文件夹下，默认包含两个文件（report_demo.yml/report_demo#手动触发.yml），其中第一个为自动触发，触发后会保存记录，第二个为手动触发，触发后不会保存记录。
2.  复制report_demo.yml文件，并重命名为环境变量中的{name}.yml（**一定要完全匹配**），代表此yml文件触发报告的是哪个分组的配置。
3. 设置时间，修改yml文件中的时间。注意如果有多个分组配置，时间最好间隔开。
4. 设置手动触发配置。复制“report_demo#手动触发.yml”文件，并且将#号前的名称改为与环境变量中配置的name相同，即触发对应name的配置（一定要以#分隔且完全匹配名称）。


## 3. 设置Github Token

1. 用户中心选择"Settings"、"Developer settings"，然后选择 "Personal access tokens"、"Tokens(classic)"。点击 "Generate new token"，选择需要的权限（通常需要 repo 权限，如果不确定就全选）。
2. 复制生成的token。
3. GitHub 仓库中，点击右上角的 "Settings"。在左侧导航栏中选择 "Secrets"，然后点击 "New repository secret"。给 secret 一个名称（GH_TOKEN），将之前生成的 Personal Access Token 复制粘贴到 "Value" 字段中。保存。

## 4. 设置发送邮箱账号密码

1. 添加环境变量，名称为【SEND_EMAIL】，设置发送邮件的邮箱账号（outlook邮箱）。
2. 添加环境变量(**不是Variables，是Secrets**)，名称为【SEND_EMAIL_PASSWORD】，设置发送邮件的邮箱密码。
3. 邮箱账号密码：https://www.yuque.com/1dao/ym0va6/enlgqkwn0rg1suqd