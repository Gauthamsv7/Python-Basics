'''

	Regular Expression:
•	.	 -> Any character Except new line
•	\d	-> Digit (0-9)
•	\D	-> Non Digit (0-9)
•	\w	-> Word Character (a-z,A-Z,0-9, _ )
•	\W	-> Not a word character
•	\s	-> Whitespace ( space,tab,new line)
•	\S	-> Not Whitespace (space,tab,new line)
•	\b	-> Word Boundary eg: Ha HaHa
•	\B	-> Not a Word Boundary eg: Ha HaHa
•	^	-> Beginning of a string
•	$	-> End of a string
•	[]	-> Matches characters in a brackets
•	[^ ]	-> Matches characters Not in a bracket
•	|	-> Either or
•	()	-> Group
•	*	-> 0 or More
•	+	-> 1 or More
•	?	-> 0 or One
•	{3}	-> Exact Number
•	{3,4}	-> Range of Numbers(Min,Max)


'''


import re

text = ''' abcdefghijklmnopqrstuvwxyz
 ACDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha Haha
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
sv.gautham7@gmail.com
sv.gautham@gmail.com
sv.gautham@gmail.com

batman.com
0891-2143289

Mr.Bruce Wayne
Mr.BruceWayne
Mrs.catwoman'''

sentence = "Start a new sentence"
# pattern = re.compile(r'\d\d\d\d-\d') #Compiling is done here (Backslash '\' is provided to meta characters such that they are avoided
# #matches = pattern.finditer(text) #finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches
# with open('data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


''' For Word boundaries -> pattern = re.compile(r'\bHa') <- '''
''' For digit pattern -> pattern = re.compile(r'pattern = re.compile(r'\d\d\d\d-\d')') <- '''


#---- Search pattern with text files ----------
# pattern = re.compile(r'\d\d\d\d-\d')
# with open('data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

#---------- Search pattern for email-----------

# pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.com') #Compiling is done here (Backslash '\' is provided to meta characters such that they are avoided
# matches = pattern.finditer(text) #finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches
# for match in matches:
#     print(match)

# url = '''
# http://www.google.com
# www.facebook.in
# http://youtube.net
# '''
# pattern = re.compile(r'http?://(www\.)?(\w+)(\.\w+)') #Compiling is done here (Backslash '\' is provided to meta characters such that they are avoided
# matches = pattern.finditer(url) #finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches
# for match in matches:
#     print(match.group(1)) #Group(0)(1)(2)(3) where 0=full link 1=www 2=website name 3=com/net
#
# url = '''
# http://www.google.com
# www.facebook.in
# http://youtube.net
# '''
# pattern = re.compile(r'http?://(www\.)?(\w+)(\.\w+)') #Compiling is done here (Backslash '\' is provided to meta characters such that they are avoided
# matches = pattern.finditer(url) #finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches
# subbed_urls = pattern.sub(r"\2\3",url) #sub(0)(1)(2)(3) where 0=full lin
# print(subbed_urls)
#
#

# #Using match sting
# line = "hello how are you ?"
# pattern = re.compile(r"hello")
# matches = pattern.match("hello")
# print(matches)

# #Using Flags
# line = "hello how are you ?"
# pattern = re.compile(r"hello",re.IGNORECASE)
# matches = pattern.match("Hello")
# print(matches)


'''Methods
Finditer = show the matches 
Findall = shows the list of strings which matches(tuples)
match = will only match the first string in the beginning of the sting if not it will throw and error
search = It is same as match
Flags are used as additional operation ( Lets explore more )

'''

