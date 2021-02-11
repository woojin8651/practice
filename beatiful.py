import requests
from bs4 import BeautifulSoup

with requests.Session() as req:
    URL_college = 'http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?'
    URL_Search ='http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/listSearch.action?'
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    
#asdfasdf
    }
    params1 = {'search_open_yr_trm':'20211'}
    params2 = {
        'search_cont_gubun':'2',
        'search_cont':'골프',
        'search_yr_trm':'99992'
    }
    major_code = input('major_code(학과)를 입력하세요')
    college_code = input('단대 코드를 입력하세요')
    search_parameter = {
        'search_open_crse_cde': major_code,
        'sub':college_code,
        'search_open_yr_trm':'20211'
    }
    response = req.get(URL_college,headers = headers,params = search_parameter)
    response.status_code
    soup = BeautifulSoup(response.text,'html.parser')

    response.text
    print(soup.find_all("tr"))