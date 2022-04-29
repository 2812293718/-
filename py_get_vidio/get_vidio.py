import requests
import re
import os
import json
from tqdm import tqdm

'''
好看网小品视频爬取练习

'''
def get_page_data(url,headers):
    # 伪装反反爬

    page_text = requests.get(url=url, headers=headers).text
    # 传值page_text到parse_page_data函数
    return page_text

def parse_page_data(page_text,headers):

    json_page_text = json.loads(page_text)
    data_list = json_page_text['data']['list']
    # print(data_list)
    for vid in data_list:
        t = 0
        t += 1
        vid['title']
        vid_url = 'https://haokan.baidu.com/v?vid=' +  vid['vid'] +"&_format=json"
        json_vid_text = json.loads(get_page_data(vid_url,headers))
        vid_down_load = json_vid_text["data"]["apiData"]["curVideoMeta"]["playurl"]
        # vid_data = requests.get(url=vid_down_load, headers=headers).content
        vid_Path = 'vidio/' + vid['title'] + ".mp4"
        total_size = int(int(requests.get(url=vid_down_load,stream=True).headers["Content-Length"]) / 1024 + 0.5)
        with open(vid_Path, 'wb') as f:
            desc = "正在下载"+vid['title']
            #实时进度条的实现
            for vid_data in tqdm(iterable=requests.get(url=vid_down_load,stream=True).iter_content(1024),total=total_size,unit='k',desc=desc):
                f.write(vid_data)
            f.close()
        print(vid['title'] + '下载成功！')
    print('成功下载了' + str(t) + '个视频!')


if __name__ == '__main__':
    if not os.path.exists('vidio'):
        os.mkdir('vidio')
    # 指定url
    url =  'https://haokan.baidu.com/web/search/api?pn=2&rn=10&type=video&query=%E5%B0%8F%E5%93%81'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/67.0.396.99 Safari/537.36',
        'Cookie': 'BIDUPSID=502200AFB81FE7181B1A8833BA3AA17B; PSTM=1648018908; BAIDUID=502200AFB81FE718C397DD42E9B34BD9:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31254_36005_35909_36165_34584_36120_36232_26350_36300_36315_36061; BA_HECTOR=0k01208lag0g0124mg1h6hj490r; delPer=0; PSINO=1; BAIDU_WISE_UID=wapp_1651035318851_663; BAIDUID_BFESS=897EE5B4436C0007AC03A853F722680C:FG=1; BCLID=10457401896746647562; BDSFRCVID=260OJexroG01VTjDeXVJMWG1yEJ4OdoTDYrEOwXPsp3LGJLVg1mDEG0PtHM7R2DbY6ONogKKW2OTHT8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbPO_C-yJID3fn74bKTahjoLjmT22jna-tj9aJ5nJDoAjtoG3jJUbqvyWtcU05o85R6ahDJlQpP-eCOKhpLBQ5KzDUKHK4vHJ2bnKl0MLnjWbb0xyTOY36FiXfnMBMnUteOnaU-y3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4j58WDT3LDHRf-b-X-Kb0QnT8MJnhHJrd5tQ_q4tHePjNtURZ5mAqoD375UJ8jlbNWhJEXq-1DqrpWUrg3K7naIQqahbKhl3EhpnkW4DUQM6HWt743bRTWbLy5KJvfJoE3pQhhP-UyntHWh37QnblMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD_-MK_xD58MePDyqx5Ka43tHD7yWCvKWpQcOR59K4nnD5_Z3M6RKlvgbejUKKjX3lFM8nbv3MOZKxLg5n7Tbb8eBgvZ2UQjtR6Usq0x0bO1Xj-wD4OaX659BDOMahv6tq7xOM-9QlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXjG8HJT8JJn3y0JQVKbK_qbbIq4b_eUAOMPnZKRvHa2kjoxQm2qbqoM8lXqJnDJFkyGO9KPRn3N5HKC5V3C5x84c1-t5M34bLhtO405OTbgbu_M_-3noZMl78hPJvypbXXnO7LTvlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_KJI_2hK-meP55q4D_MfOtetJyaR0H_DJvWJ5WqR7jD5Q43-IvbJ7pBfrU3b68KlF2BbboShbXKxoc5pkrKp0eWUbZBNcMoR6g3l02V-bSXjJCDx0VWHj9WtRMW23Uoq7mWU-WsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKDHAHJjJP; BCLID_BFESS=10457401896746647562; BDSFRCVID_BFESS=260OJexroG01VTjDeXVJMWG1yEJ4OdoTDYrEOwXPsp3LGJLVg1mDEG0PtHM7R2DbY6ONogKKW2OTHT8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbPO_C-yJID3fn74bKTahjoLjmT22jna-tj9aJ5nJDoAjtoG3jJUbqvyWtcU05o85R6ahDJlQpP-eCOKhpLBQ5KzDUKHK4vHJ2bnKl0MLnjWbb0xyTOY36FiXfnMBMnUteOnaU-y3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4j58WDT3LDHRf-b-X-Kb0QnT8MJnhHJrd5tQ_q4tHePjNtURZ5mAqoD375UJ8jlbNWhJEXq-1DqrpWUrg3K7naIQqahbKhl3EhpnkW4DUQM6HWt743bRTWbLy5KJvfJoE3pQhhP-UyntHWh37QnblMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafD_-MK_xD58MePDyqx5Ka43tHD7yWCvKWpQcOR59K4nnD5_Z3M6RKlvgbejUKKjX3lFM8nbv3MOZKxLg5n7Tbb8eBgvZ2UQjtR6Usq0x0bO1Xj-wD4OaX659BDOMahv6tq7xOM-9QlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXjG8HJT8JJn3y0JQVKbK_qbbIq4b_eUAOMPnZKRvHa2kjoxQm2qbqoM8lXqJnDJFkyGO9KPRn3N5HKC5V3C5x84c1-t5M34bLhtO405OTbgbu_M_-3noZMl78hPJvypbXXnO7LTvlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVD_KJI_2hK-meP55q4D_MfOtetJyaR0H_DJvWJ5WqR7jD5Q43-IvbJ7pBfrU3b68KlF2BbboShbXKxoc5pkrKp0eWUbZBNcMoR6g3l02V-bSXjJCDx0VWHj9WtRMW23Uoq7mWU-WsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKDHAHJjJP; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1651056973; hkpcSearch=%u5C0F%u54C1; av1_switch_v3=0; PC_TAB_LOG=video_details_page; COMMON_LID=d95acc0d964aadb22746d1be2db1d76e; ab_sr=1.0.1_M2M3MDU3YTllNjgyN2I2ODhlMzg1NWNhMDcyNWY4NGNlMDZlOGRmNGUxYjU4NzBkNTM1NGE0MjhlZWQyMDU2Mzk4Yzc1ZDk5YzQ5Y2E0YjViNzU2MDhkMmNiZmViYzliNWUzNmQ3ZGZmZTI3ZThhNWQ2NmZmYTg4YTAxNWM3ZTExM2U1NjQxYjVkYTcwNzNjZmE2N2MwNzU0ZTY0YjA3Ng==; reptileData=%7B%22data%22%3A%22d6c9cda39b2af4ed4c6d81ebc2c13c0d3228503c5218bfdc699e05a251439274085a3a6b1dea3f610e8e1368853dc70f9a2704811e037a7ada52d9a9febbf9f5c80914fdf16b96a4907b8da1172f2fe0de72bfa65f6d0ff87d77b5503c7429ec%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%229cebdc98%22%7D; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1651058134; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=lyfi30665ga&ss=l2hgozt4&sl=5&tt=3gpp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=pmjl"'
    }
    page_text = get_page_data(url,headers)
    parse_page_data(page_text,headers)
