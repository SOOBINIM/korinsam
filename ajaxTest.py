import requests
import json
from bs4 import BeautifulSoup


# id = id id_email_2
# pw = id id_password_3
# submit = class btn_g btn_confirm submit




LOGIN_INFO = {
    'userID' : '743490@naver.com',
    'userPassword' : 'skWkd92!'
}

with requests.Session() as s:
    req_login = s.post('https://accounts.kakao.com/login?continue=https%3A%2F%2Faccounts.kakao.com%2Fweblogin%2Faccount', data=LOGIN_INFO)
    print(req_login.status_code)

    # custom_header = {
    #     "referer" : 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fcomm-auth-web.kakao.com%2Flogin%2Fcheck?hash=pb2b13tCS3gfvWojP3pf1T_KvKO3U-UbUs2v_cz60ns',
    #     "user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    # }
    url = "https://comm-auth-web.kakao.com/seller/gate?groupId=237405"
    req_index = requests.get(url)
    # req_index = requests.get(url, header= custom_header)

    dom = BeautifulSoup(req_index.content, "html.parser")
    print(dom)


    # req = s.post('https://sell.kakao.com/dashboard/index')

    


# def kakao_login(id_email_2,id_password_3):
#     custom_header = {
#         "referer" : 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fcomm-auth-web.kakao.com%2Flogin%2Fcheck?hash=pb2b13tCS3gfvWojP3pf1T_KvKO3U-UbUs2v_cz60ns',
#         "user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
#     }
#     url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Faccounts.kakao.com%2Fweblogin%2Faccount"
#     req = requests.get(url, headers = custom_header)

#     # response = requests.get(link, headers = headers)
#     # dom = BeautifulSoup(response.content, "html.parser")
#     # # text = dom.findAll("span", {"strong":re.complie("희망가격")})
#     # return dom

#     if req.status_code == 200:
#         print("접속 성공")
#         stock_data = json.loads(req.text)
#         print(stock_data)

#     else:
#         print("접속 실패")

# if __name__ == "__main__": 
#     kakao_login('743490@naver.com','skWkd92!')
    # s = kakao_session('743490', 'skWkd7434!@')     




# import re 
# import uuid 
# import requests
# import rsa
# import lzstring 
# from urllib3.util.retry import Retry 
# from requests.adapters import HTTPAdapter
# from bs4 import BeautifulSoup
# import konlpy


# def encrypt(key_str, uid, upw):
#     def naver_style_join(l):
#         return ''.join([chr(len(s)) + s for s in l])

#     sessionkey, keyname, e_str, n_str = key_str.split(',')
#     e, n = int(e_str, 16), int(n_str, 16)

#     message = naver_style_join([sessionkey, uid, upw]).encode()

#     pubkey = rsa.PublicKey(e, n)
#     encrypted = rsa.encrypt(message, pubkey)
    
#     return keyname, encrypted.hex()

# def encrypt_account(uid, upw):
#     key_str = requests.get('https://nid.naver.com/login/ext/keys.nhn').content.decode("utf-8") 
#     return encrypt(key_str, uid, upw)

# def naver_session(nid, npw):
#     encnm, encpw = encrypt_account(nid, npw) 

#     s = requests.Session() 
#     retries = Retry( 
#         total=5, 
#         backoff_factor=0.1, 
#         status_forcelist=[500, 502, 503, 504] 
#     ) 
#     s.mount('https://', HTTPAdapter(max_retries=retries)) 
#     request_headers = { 
#         'User-agent': 'Mozilla/5.0' 
#     } 
    
#     bvsd_uuid = uuid.uuid4() 
#     encData = '{"a":"%s-4","b":"1.3.4","d":[{"i":"id","b":{"a":["0,%s"]},"d":"%s","e":false,"f":false},{"i":"%s","e":true,"f":false}],"h":"1f","i":{"a":"Mozilla/5.0"}}' % (bvsd_uuid, nid, nid, npw) 
#     bvsd = '{"uuid":"%s","encData":"%s"}' % (bvsd_uuid, lzstring.LZString.compressToEncodedURIComponent(encData)) 
#     resp = s.post('https://nid.naver.com/nidlogin.login', data={ 
#         'svctype': '0', 
#         'enctp': '1', 
#         'encnm': encnm, 
#         'enc_url': 'http0X0.0000000000001P-10220.0000000.000000www.naver.com', 
#         'url': 'www.naver.com', 
#         'smart_level': '1', 
#         'encpw': encpw, 
#         'bvsd': bvsd 
#     }, headers=request_headers) 
    
#     finalize_url = re.search(r'location\.replace\("([^"]+)"\)', resp.content.decode("utf-8")).group(1) 
#     s.get(finalize_url) 
    
#     return s

# def get_total(keyword):
#     url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%" + keyword +  \
# 	"&search.menuid=424&search.searchBy=0&search.sortBy=date&search.clubid=10625158&search.option=0&search.defaultValue=&search.page="
#     response = requests.get(url)
#     dom = BeautifulSoup(response.content, "html.parser")
#     return dom.select_one("#ct > div.search_contents > div.search_sort > div.sort_l > span").text

# def get_list(keyword, page):
#     url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%" + keyword +  \
# 	"&search.menuid=424&search.searchBy=0&search.sortBy=date&search.clubid=10625158&search.option=0&search.defaultValue=&search.page=" + str(page)
#     res = requests.get(url)
#     dom = BeautifulSoup(res.content, "html.parser")
#     result = dom.findAll("a", {"href":re.compile("ArticleRead.nhn?")})
#     get_link(result)
#     return result
    
# def get_link(result):
#     # ls = []
#     for i in range(0, len(result)):
#         link = result[i].get('href')
#         link = "http://m.cafe.naver.com"+link
#         print(link, sep='\n')
#         print( sep='\n')
#         # ls.append(link)
    
    
#     # print(ls, sep='\t')
#     # return ls

# def get_text(link):
#     headers = {
#         "Referer" : "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EB%B0%98%EB%8B%A4%EB%82%98&search.menuid=0&search.searchBy=0&search.sortBy=date&search.clubid=10625158&search.option=0&search.defaultValue=1",
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
#     }

#     response = requests.get(link, headers = headers)
#     dom = BeautifulSoup(response.content, "html.parser")
#     # text = dom.findAll("span", {"strong":re.complie("희망가격")})
#     return dom

# def get_all_texts(keyword):
#     total = get_total(keyword)
#     pages = int(total)
#     # text_sets = []

#     for page in range(1, 2):
#         text = get_list(keyword, page)
#         link_ls = get_link(text)
#         for link in link_ls:
#             all_text = get_text(link)
#             # text_sets.extend(all_text)

#     print(all_text)

# if __name__ == "__main__": 
#     s = naver_session('743490', 'skWkd7434!@') 
#     get_list("반다나",1)
#     # get_all_texts("반다나")    

