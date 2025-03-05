#write a program fro generating regular expression for regular grammar

#1} re for searching words
import re
s="this is winter season"
match=re.search(r'winter',s)
print('start index:',match.start())
print('end index:',match.end())

#2}re for number search
import re
string="""hello my number is 1234567890 and my friend's number is 1234566789"""
regex=r'\d+'
match=re.findall(regex,string)
print(match)

#3}re for searching characters
import re
p=re.compile('[a-z]')
print(p.findall("stark industries"))

#4}re for searching character by length
import re
p=re.compile(r"\b\w{2}\b")
print(p.findall("Mr.stark"))

#5}re for searching number with length
import re
str1 = "Emma's lucky number is 786"
pattern = r"\b\d+\b"  
regex_pattern = re.compile(pattern)
result = regex_pattern.findall(str1)
print(result)

#6}re for printing number from string & splitting it by character & grp of character
import re
p=re.compile('\d')
print(p.findall("i went to him at 11am on 4th july 1999"))
p=re.compile('\d+')
print(p.findall("i went to him at 11am on 4th july 1999"))

#7}re for printing combination of given ip
import re
p=re.compile('ab*')
print(p.findall("ababbaabbb"))





