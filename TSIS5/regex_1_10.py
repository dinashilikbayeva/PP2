"""#1
import re
s = str(input())
r = re.findall("ab*", s)
print(r)

#2
import re
s = str(input())
r = re.findall('ab{2,3}', s)
print(r)

#3
import re
s = str(input())
r = re.findall("[a-z]_[a-z]{1}", s)
print(r)

#4
import re
s = str(input())
r = re.findall("[A-Z][a-z]+", s)
print(r)

#5
import re
s = str(input())
r = re.findall('a[^ b]*b', s)
print(r)

#6
import re
s = str(input())
r = re.sub("[ ,.]", ":",s)
print(r)
"""
#7
import re
s = str(input())
temp = s.split('_')
print(temp[0] + ''.join(ele.capitalize() for ele in temp[1:]))
"""
#8
import re
s = str(input())
r = re.findall('[A-Z][^A-Z]*', s)
print(r)

#9
import re
s = str(input())
r = re.findall('[A-Z][^A-Z]*', s)
for i in r:
    print(i +" ", end='')

#10
import re

s = str(input())
snake_case = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
print(snake_case)
"""