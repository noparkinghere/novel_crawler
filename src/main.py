# 爬取 wuxiaworld 的代码

from crawler import WXSJ_download

reqUrl_base = 'https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-'
file_name = "../download/against-the-gods.txt"
reqUrl_sp = {1043:'https://www.wuxiaworld.com/novel/against-the-gods/chapter-', 1044:'https://www.wuxiaworld.com/novel/against-the-gods/chapter-'}
WXSJ_download(reqUrl_base=reqUrl_base, file_name=file_name, start=1, len=1600, reqUrl_sp=reqUrl_sp)
