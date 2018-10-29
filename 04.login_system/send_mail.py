import os
#from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_site.settings'

if __name__ == '__main__':   
    '''
    send_mail(
        '来自www.robindongblog.com的测试邮件',
        '欢迎访问www.robindongblog.com，这里是wo的博客和教程站点，本站专注于Python和Django技术的分享！',
        '1361623944@qq.com',
        ['1505955202@qq.com'],
    )
    '''
    #send HTML email
    subject, from_email, to = '来自www.robindongblog.com的测试邮件','1361623944@qq.com','1505955202@qq.com'
    text_content = '欢迎访问www.robindongblog.com，这里是wo的博客和教程站点，本站专注于Python和Django技术的分享！'
    html_content ='<p>欢迎访问<a href="http://www.robin-dong.github.io" target=blank>www.robin-dong.github.io</a>，这里是wo的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('done')