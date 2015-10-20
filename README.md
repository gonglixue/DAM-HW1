# DAM-HW1
Homework 1 of DAM course in 2015 autumn term. It is a music resource website.

这是2015年秋学期数字媒体资源管理课程作业一。这是一个音乐资源网站项目，本网站提供了一些音乐资源的试听以及对它们的简短介绍。在本网站的Leave A Message页面实现留言功能，点击发送可将留言发送到我的邮箱，但这需要在index.py中自行填写mail_host,mail_user,mail_pass，程序以mail_user为发件箱使用smtplib自动发送邮件。

以新浪邮箱为例，新浪邮箱的smtp服务器地址为smtp.sina.com。那么，mail_host填写smtp.sina.com，mail_user填写邮箱地址，mail_pass填写邮箱密码。

运行index.py需要使用的包有flask, flask.ext.script, os, smtplib, email.mime.text, wtforms, wtforms.validators
