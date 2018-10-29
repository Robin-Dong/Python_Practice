import requests


def log_in():
    """
    登入系统
    """
    url='http://ekp.sunwoda.com/ekp/j_acegi_security_check'
    data ={
        'j_redirectto':'http://ekp.sunwoda.com/ekp/index.jsp',
        'j_username':'******',
        'j_password':'******',
        'j_lang':'zh-CN',  
    }
    session = requests.session()
    r =session.post(url,data = data)
    if r.status_code == 200:
        print("登入成功")
        return session
    else:
        print("登入失败")


def get_meeting_page(log_session,book_dict):
    """
    进入会议预定界面，获取指定会议室id和会议id
    """
    url = 'http://ekp.sunwoda.com/ekp/km/imeeting/km_imeeting_calendar/kmImeetingCalendar.do'
    data = {
        'method':'rescalendar',
        'fdStart':'2018-08-20 00:00',
        'fdEnd':'2018-08-27 00:00',
    }
    result = log_session.post(url,data=data)
    all_meeting_info = result.json()
    for room in meeting_info['main']:
        if meeting_info['main'][room]['name'] == '综合楼7楼1号会议室':
            room_info = meeting_info['main'][i]['list'][3]
            #获取会议室id和会议id
            book_dict['fdId'] = room_info['fdId']
            book_dict['fdPlaceId'] = room_info['fdPlaceId']
            break
        else：
            continue
    return book_dict

def book_meeting(sessions,book_dict,):
    """
    申请预定
    """
    book_url ='http://ekp.sunwoda.com/ekp/km/imeeting/km_imeeting_book/kmImeetingBook.do?method=book&s_ajax=true
    headers = {
        'Host': 'ekp.sunwoda.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer':'http://ekp.sunwoda.com/ekp/km/imeeting/index.jsp',
    }
    result = logged.post(book_url,headers=headers,data=book_dict)
    if result.status_code == 200:
        return result['titile']
    else:
        return result.text

def main():
    log_session = log_in()
    book_dict = {}
    get_meeting_page(log_session,book_dict)
    # 构造请求信息
    book_dict['fdName'] = '部门周会' # 会议主题
    book_dict['fdMeetingNums'] = '19' # 人数
    book_dict['start'] = '2018-08-20 08:00' # 开始时间
    book_dict['end'] = '2019-08-20 09:00' # 结束时间
    book_result = book_meeting(sessions, book_dict)
    print(book_result)

if __main__ == __name__:
    main()


