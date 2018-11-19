import re
import os

f = open('everything.txt','r',errors='ignore').read()
q = open('temp.txt','w+')
pattern = r'\[.*?\]+\(.*?\)'
s = re.sub(pattern, '', f)
pattern2 = r'\n\n'
l = re.sub(pattern2, '', s)
l = re.sub(r'![a-zA-Z0-9]', '', l)

q.write(l)
q.close()
os.remove('everything.txt')
os.rename('temp.txt','output.txt')