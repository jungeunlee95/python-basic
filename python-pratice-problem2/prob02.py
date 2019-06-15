# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

# --- 1 : 직접 거르기 if, else
result = ''
idx = 0
while True:
    if idx >= len(s): break
    if s[idx] == '<':
        while s[idx] != '>':
            result += ''
            idx += 1
    else:
        result += s[idx]
    idx += 1

print(result)

print('------------------------------------------------------------------------------')

# --- 2 find() 사용
while True:
    start = s.find('<')
    end = s.find('>')
    if start == -1 or end == -1:
        break
    s = s[:start] + s[end+1:]
print(s)

# 실험
# a = "1123434311"
# while True :
#     c = a.find('1')
#     if c == -1 : break
#     a = a[:c] + a[c+1:]
#     print(a)


print('------------------------------------------------------------------------------')

# --- 3 : re 모듈 - 파이썬 정규 표현식 사용
import re
def remove_tag(content):
   cleanr = re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext
print(remove_tag(s))

