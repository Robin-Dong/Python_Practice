# Python_Practice
python学习和实践内容，包含以下

## 01 python_basis
python基础练习，题目为主

## python_script
用python写的两个小脚本
- 01.clean_helper.py  
    背景：前公司的实验数据每天几百个，手工选中删除费时间，而且实验电脑比较渣，动不动选中大量文件时就卡住  
    作用：指定清理相应文件夹定日期，快速且高效，打包成应用后，一键运行
- 02.book_meeting_room.py  
    背景：前公司所在部门经常周一早上有周会，一层楼就一个大会议室，因为系统限制的限制，只能提前周末早上8:00抢订会议室，累呀  
    构成：模拟登入公司ERP系统，在跳转会议预定页面，拿到会议室ID，加入预定信息，POST预定。再放到服务器上，定时运行，周末可以睡个懒觉了

## web_server_practice
手写一个web_server练习

## login_system
用Django写的登入注册系统，包含完整登入注册流程，如验证码，邮件认证，用户信息加密等功能