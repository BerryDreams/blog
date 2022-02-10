import requests        #导入requests包
import json
def get_translate_date():
    url = 'https://leetcode-cn.com/problems/maximum-good-people-based-on-statements'
    #请求表单数据
    cookies_str = '__auc=8712db5117e22498016e05ed386; gr_user_id=13b7b412-c5d1-4d98-b3c8-ff1fa6494d2f; _ga=GA1.2.1948093967.1641252752; _bl_uid=4zk2zxawzg0bj1ijUgzhrR5f9s36; a2873925c34ecbd2_gr_last_sent_cs1=berrydream; _gid=GA1.2.206292084.1641778457; csrftoken=8IPjYkCg3276HUpB2Ol4mgQrLyIFpC1Ry5f1RWlBNyqrKOpjDcTfumBz76ioc07g; __atuvc=3%7C4; aliyungf_tc=5230c75403008c87885595017a851d4f17116f29bcd1f7da722198982b0bbf04; NEW_PROBLEMLIST_PAGE=1; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1642814824,1642848549,1642904714,1642912990; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTU5Mjg0NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImF1dGhlbnRpY2F0aW9uLmF1dGhfYmFja2VuZHMuUGhvbmVBdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNzkwOGI1YzcwZTVmZjVmOTJhNTAzY2M2MGMyZWM1NGNjMmU0ZTc5MmRjODY0NzMwODg2OTE2OWJlYjIyMTIwIiwiaWQiOjE1OTI4NDUsImVtYWlsIjoiY3pnXzIwMDBAMTYzLmNvbSIsInVzZXJuYW1lIjoiYmVycnlkcmVhbSIsInVzZXJfc2x1ZyI6ImJlcnJ5ZHJlYW0iLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9taXN4cmVzcy04L2F2YXRhcl8xNTk0NTM3OTY0LnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjQyODUwNTU4LjczNzY2MjgsImV4cGlyZWRfdGltZV8iOjE2NDUzODM2MDAsInZlcnNpb25fa2V5XyI6MCwibGF0ZXN0X3RpbWVzdGFtcF8iOjE2NDI5MTU0Nzd9.OEHKzaucnIxOcJ8EtagIJ78I-W0YKbn8Yoly5lJT6mc; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1642936293; a2873925c34ecbd2_gr_session_id=fc00f4a0-fb78-48cc-ac7d-3c271515efde; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=fc00f4a0-fb78-48cc-ac7d-3c271515efde; a2873925c34ecbd2_gr_cs1=berrydream; a2873925c34ecbd2_gr_session_id_fc00f4a0-fb78-48cc-ac7d-3c271515efde=true'
    cookies = {}
    for line in cookies_str.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    response = requests.get(url, cookies=cookies)
    #将Json格式字符串转字典
    print(response.text)
    #打印翻译后的数据
    #print(content['translateResult'][0][0]['tgt'])
if __name__=='__main__':
    get_translate_date()