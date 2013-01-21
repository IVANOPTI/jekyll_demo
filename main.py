#-*- coding:utf-8 -*- 
import re
def main_process():
    s = '''211.210.209.108
    gan ffad1.210.2.108
    d ffad1.210.2.109afa''' 
    com=re.compile(p)
    lst_m=com.finditer(s)
    for m in lst_m:
        print m.group()
p = r'(([12][0-9][0-9]|[1-9][0-9]|[1-9])\.){3,3}([12][0-9][0-9]|[1-9][0-9]|[1-9])' 
match_group(p)
def group():
    '''若存在多个匹配，可以用finditer来获取到多个组''' 
def match(p): 
    s = 'Isaac Newton, physicist, huang zhijun'
    mo = re.compile(p)
    m = mo.search(s) 
    if not m: 
        print 'no match' 
    else:
	print mo.findall(s)

