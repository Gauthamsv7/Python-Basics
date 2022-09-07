import re

text = ''' abcdefghijklmnopqrstuvwxyz
 ACDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha Haha
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

batman.com
0891-2143289

Mr.Bruce Wayne
Mr.BruceWayne
Mrs.catwoman'''

sentence = "Start a new sentence"
pattern = re.compile(r'\d\d\d\d-\d') #Compiling is done here (Backslash '\' is provided to meta characters such that they are avoided
#matches = pattern.finditer(text) #finditer() function matches a pattern in a string and returns an iterator that yields the Match objects of all non-overlapping matches
with open('data.txt','r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)


''' For Word boundaries -> pattern = re.compile(r'\bHa') <- '''
''' For digit pattern -> pattern = re.compile(r'pattern = re.compile(r'\d\d\d\d-\d')') <- '''


#---- Search pattern with text files ----------
# pattern = re.compile(r'\d\d\d\d-\d')
# with open('data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)