import requests
import re

content_rep_str = '</p>'
NextLineSignal = "\n"  # 添加换行符
titleEndSig = r'<'
contentEndSig = r'<a href="/novel/'
dumpSig = r'(<[^>]+>|&nbsp;)'

def WXSJ_download_test(reqUrl_base, file_name, i):
  payloadHeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

  if i == 1043 or i == 1044:
    reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/chapter-'

  try:
    reqUrl = reqUrl_base+str(i)
    r = requests.get(reqUrl, headers=payloadHeader)

    pattern = re.compile('>Chapter '+str(i)+' [–|-]')
    src_list = re.split(pattern, r.text) # 超出需要内容的起点

    content = src_list[-1]
    print(content)
    nov_title = 'Chapter '+str(i)+content[0:re.search(titleEndSig, content).start()]
    print('*'*10)
    nov_content = content[re.search(titleEndSig, content).start():re.search(contentEndSig, content).start()]
    nov_content = nov_content.replace(content_rep_str, NextLineSignal+NextLineSignal)
    nov_content = re.sub(dumpSig, '', nov_content)
    print(nov_title)
    print(nov_content)

    with open(file_name, 'w+', encoding='utf-8') as test:
      test.write(nov_title)
      test.write(nov_content)

  except:
    print('error:' + str(i))



def WXSJ_download(reqUrl_base, file_name, start, num):
  payloadHeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
  reqUrl_tmp = reqUrl_base

  for i in range(num):
    # 网址发生变更的特殊情况
    if i+start == 1043 or i+start == 1044:
      reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/chapter-'
    else:
      reqUrl_base = reqUrl_tmp

    try:
      reqUrl = reqUrl_base + str(i+start)
      r = requests.get(reqUrl, headers=payloadHeader)

      pattern = re.compile('>Chapter ' + str(i+start) + ' [–|-]')
      src_list = re.split(pattern, r.text)  # 超出需要内容的起点

      content = src_list[-1]
      nov_title = 'Chapter ' + str(i+start) + content[0:re.search(titleEndSig, content).start()]
      nov_content = content[re.search(titleEndSig, content).start():re.search(contentEndSig, content).start()]
      nov_content = nov_content.replace(content_rep_str, NextLineSignal + NextLineSignal)
      nov_content = re.sub(dumpSig, '', nov_content)

      with open(file_name, 'a+', encoding='utf-8') as test:
        test.write(nov_title)
        test.write(nov_content)

      with open(file_name[:-3] + 'log', 'a+') as f:
        log = 'Chapter ' + str(i + start) + ' is successful' + '\n'
        print(log)
        f.write(log)

    except:
      print('error:'+'Chapter-'+str(i))
      break



if __name__ == '__main__':
  reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-'
  file_name = "../download/against-the-gods.txt"
  WXSJ_download(reqUrl_base, file_name, 1, 1600)

  # WXSJ_download_test(reqUrl_base, file_name, 1600)

