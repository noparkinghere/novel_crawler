# 无法写出比较通用的程序，wuxiaworld 页面每个几个更换一种排版格式，标题、符号、个数经常变动。
# 这边仅仅提供一个勉强可以用的程序，不能使用的地方仍然需要手动更改程序。

import requests
import re

content_rep_str = '</p>'
NextLineSignal = "\n"  # 添加换行符
titleEndSig = r'<'
contentEndSig = r'<a href="/novel/'
dumpSig = r'(<[^>]+>|&nbsp;)'

def WXSJ_download_test(reqUrl_base, file_name, num):
  payloadHeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

  try:
    reqUrl = reqUrl_base+str(num)
    r = requests.get(reqUrl, headers=payloadHeader)
    pattern = re.compile('>Chapter '+str(num)+'(?: [–|-]|\: )')

    src_list = re.split(pattern, r.text) # 超出需要内容的起点
    # print(reqUrl_base)
    # print(src_list)
    if len(src_list) > 1:
      content = src_list[-1]
    else:
      print("cannot split error"+str(num))

    nov_title = 'Chapter '+str(num)+content[0:re.search(titleEndSig, content).start()]
    nov_content = content[re.search(titleEndSig, content).start():re.search(contentEndSig, content).start()]
    nov_content = nov_content.replace(content_rep_str, NextLineSignal+NextLineSignal)
    nov_content = re.sub(dumpSig, '', nov_content)
    # print('*'*10)
    nov_content += '\n'+'*'*10+'\n'
    # print(nov_title)
    # print(nov_content)

    with open(file_name, 'a+', encoding='utf-8') as test:
      test.write(nov_title)
      test.write(nov_content)

    with open(file_name[:-3] + 'log', 'a+') as f:
      log = 'Chapter ' + str(num) + ' is successful' + '\n'
      f.write(log)
      print(log)

  except:
    exit('error:' + str(num))



def WXSJ_download(reqUrl_base, file_name, start, len, reqUrl_sp={}):
  payloadHeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
  reqUrl_tmp = reqUrl_base
  keySp = [i for i in reqUrl_sp.keys()]

  # 循环逐一爬取整个内容
  for i in range(len):
    reqUrl_base = reqUrl_tmp

    for j in keySp:    # 个别网页网址发生变更的特殊情况
      if i+start == j:
        reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/chapter-'
        break

    WXSJ_download_test(reqUrl_base, file_name, i+start)

if __name__ == '__main__':
  reqUrl_base = 'https://www.wuxiaworld.com/novel/rmji/rmji-chapter-'
  file_name = "../download/test.txt"
  reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-'
  file_name = "../download/against-the-gods.txt"
  reqUrl_sp = {1043: 'https://www.wuxiaworld.com/novel/against-the-gods/chapter-',
               1044: 'https://www.wuxiaworld.com/novel/against-the-gods/chapter-'}
  WXSJ_download(reqUrl_base, file_name, 1043, 3, reqUrl_sp)
  # 测试代码
  # WXSJ_download_test(reqUrl_base, file_name, 1043, reqUrl_sp)

