import requests # 导入 requests 库，用于发送 HTTP 请求
from JsReverse import get_js # 导入自定义模块 JsReverse 中的 get_js 函数

# 传入 wyyJs.js 里的参数
data = '{"rid":"R_SO_4_2054300084","threadId":"R_SO_4_2054300084","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
# 调用 get_js 函数，将文件路径、函数名和数据作为参数，获取返回的字典
data_dict = get_js('wyyJs.js', 'd', data)
# 打印获取的字典
print(data_dict)

# 创建一个空字典
dic = {}
# 传入网站的参数
dic['params'] = data_dict['encText']
dic['encSecKey'] = data_dict['encSecKey']
# 目标 url
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
# 请求头
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# 发送 POST 请求，传递参数 dic 和 headers，并获取响应对象
res = requests.post(url, data=dic, headers=head)
# 打印响应对象的文本内容
print(res.text)
