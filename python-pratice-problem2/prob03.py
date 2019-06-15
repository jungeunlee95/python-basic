# 문제3.
s = """
    We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors group is available 
    to help guide new contributors through the process.
    """

# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.

print("---------------[1 - 1 : 직접 거르기]-----------------")
a = [',', '.', '\n', ' ']
result = []
str = ''
for i in range(len(s)):
    if s[i] not in a:
        str += s[i].upper()
    else:
        if str != '':
            result.append(str)
            str = ''
print("\n".join([i for i in sorted(list(set(result)))] ))


print("---------------[1 - 2 : 직접 거르기]-----------------")
# 2)각 단어의 빈도수도 함께 출력해 보세요
def check_cnt(str):
    wordAll = s.split(' ')
    result = 0
    for i in wordAll:
        if str in i.upper():
            result += 1
    return result

for i in sorted(list(set(result))):
    print(i, ":", check_cnt(i))


print("---------------[2 - 1 : 내장함수 사용]-----------------")
s = s.replace('.', '').replace(',', '').replace('\n', '').upper()
word_list = s.split(' ')
word_list = list(set(word_list))
word_list.sort()
print(' \n'.join(word_list[1:]))

print("---------------[2 - 2 : 내장함수 사용]-----------------")
for i in range(1, len(word_list)):
    print(f"{word_list[i]} : {s.upper().count(word_list[i])}")