from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup


url = 'http://www.culture.go.kr/openapi/rest/cultureartspaces/performingplace'
params ={'serviceKey' : '4GznD2rYw2DOOMXTM1pKa8Xy5uEWZuyzeGSMc03hYAIInVy3CS03t5GlkZDtdR%2BDA4AEFwnOCUHvitP9o99vmg%3D%3D', 'gpsxfrom' : '129.101', 'gpsyfrom' : '35.142', 'gpsxto' : '129.101', 'gpsyto' : '35.142', 'cPage' : '1', 'rows' : '10', 'ComMsgHeader' : '', 'RequestTime' : '20100810:23003422', 'CallBackURI' : '', 'MsgBody' : '', 'keyword' : '' }

response = requests.get(url, params=params)
print(response.content)