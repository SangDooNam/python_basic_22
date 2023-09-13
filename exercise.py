import re 

"""Task 1. 
Write a Python program to check for a number at the end of a string."""

# text = input('Enter any text: ')

# pattern = r'\w+\d+$'  # r'd+$'

# match = re.search(pattern, text)
# every = re.findall(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequence : {every}')
# else:
#     print('There is no match.')

"""Task 2.
Write a Python program to search for numbers (0-9) of length between 1 and 3 in the given string.

Exercises number 1, 12, 13, and 345 are important"""

# text = ('Exercises number 1, 12, 13, and 345 are important')

# pattern = r'[0-9]{1,3}' # \d{1,3}

# # pattern = r'(34[0-5]|3[0-3][0-9]|[012]?[0-9][0-9]?)'

# match = re.search(pattern, text)
# every = re.findall(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group()}')
#     print(f'All matched sequence : {every}')
# else:
#     print('There is no match.')

"""Task 3.
Write a Python program to search for literal strings within a string.
Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'
"""

# text = 'The quick brown fox jumps over the lazy dog.'

# pattern = r'(fox)|(dog)|(horse)'

# match = re.search(pattern, text)
# every = re.findall(pattern, text)

# if match:
#     print(f'First matched sequence : {match.group(1,2,3)}')
#     print(f'All matched sequence : {every}')
# else:
#     print('There is no match.')


"""Task 4.
Write a Python program to search for a literal string in a string 
and also find the location within the original string where the pattern occurs.
Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox'
"""

# text = 'The quick brown fox jumps over the lazy dog.'

# pattern = r'fox'

# match = re.search(pattern, text)

# print(match) # print(match.span()) # print(match.start(), match.end())


"""Task 5. 
Write a Python program to find the substrings within a string.
Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.

"""

# text = 'Python exercises, PHP exercises, C# exercises'

# pattern = 'exercises'

# match = re.findall(pattern, text)

# sub = re.subn(pattern, 'here it is', text)

# print(match)

# print(sub)

"""Task 6.
Write a Python program to find the occurrence and position of substrings within a string."""

# text = input('Enter a text to find a matching word and its position.: ')

# search = input('Enter the word or string you want to search for in the previously entered text.: ')

# match = re.findall(search, text)

# if match:
#     for i in re.finditer(search, text):
        
#         print(f"'{i.group()}' is matched at the porint {i.start()} to {i.end()}")

# print(match)




"""Task 7.
Write a Python program to replace whitespaces with an underscore and vice versa."""

# text = input('Enter any text to replace whitespaces with an underscore and vice versa.: ')

# pattern = r'\s' 

# underscore = r'_'

# match_s = re.findall(pattern, text)

# match_ = re.findall(underscore, text)

# if match_s:
#     replace= re.sub(pattern, underscore, text)
    
#     print(replace)
    
# elif match_:
#     replace_ = re.sub(underscore, ' ', text)
    
#     print(replace_)


"""Task 8.
Write a Python program to extract year, month and date from an URL."""

# text = input('Enter URL or any text to extract year, month and date: ')

# text = 'https://www.example.com/2023/08/17/article-titlehttps://www.example.com/08/17/2023/article-titlehttps://www.example.com/17/08/2023/article-title'


# pattern1 = r'([0-9]{4})/(1[0-2]|0?[1-9])/(3[0-1]|[0-2]?[0-9])'

# pattern2 = r'(1[0-2]|0?[1-9]).(3[0-1]|[0-2]?[0-9]).([0-9]{4})'

# pattern3 = r'(3[0-1]|[0-2]?[0-9]).(1[0-2]|0?[1-9]).([0-9]{4})'


# pattern = r'([0-9]{4})/(1[0-2]|0?[1-9])/(3[0-1]|[0-2]?[0-9])|(1[0-2]|0?[1-9]).(3[0-1]|[0-2]?[0-9]).([0-9]{4})|(3[0-1]|[0-2]?[0-9]).(1[0-2]|0?[1-9]).([0-9]{4})'

# match = re.findall(pattern, text)
# # match2 = re.findall(pattern2, text)
# # match3 = re.findall(pattern3, text)
# print(match)

# match = re.finditer(pattern, text)


# for i in match:
    
#     print(f'{i.group()}  {i.start()} {i.end()}')


"""Task 9.
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format."""

# text = '2023-08-17'

# pattern = r'([0-9]{4})-(1[0-2]|0?[1-9])-(3[0-1]|[0-2]?[0-9])'

# match = re.search(pattern, text)

# if match:
    
#     replace = re.sub(pattern, r'\3-\2-\1',text)
#     print(replace)
    
    
"""Task 10.
Write a Python program to match if two words from a list of words start with the letter 'P'."""


# words = ["Python", "Pear", "Apple", "Peach", "Grape", "Pineapple"]

# p_words = []

# pattern = r'^P'

# for i in words:
#     if re.match(r'^P', i):
        
#         p_words.append(i)
        
# if len(p_words) >= 2:
#     print(f'There are 2 or more words starting with P : {p_words}')
# else:
#     print(f'Less than 2 words starting with P : {p_words}')
    

"""Task 11.
Write a Python program to separate and print the numbers in a given string."""

# text = 'Sunsets over the horizon bring calmness to my heart.'

# pattern = r'\s'

# # task = re.subn(pattern, r'-', text)

# # print(task)

# task = re.split(pattern, text)

# indexing = []
# listing = []
# result = []

# for index, element in enumerate(task):
    
#     indexing.append(index)
#     listing.append(element)
    
#     adding = str(index)+ '.' + element
    
#     result.append(adding)

# # print(indexing, listing)
# print(result)

# print(f'{task}')

"""Task 12.
Write a Python program to find all words starting with 'a' or 'e' in a given string."""

# text = 'Astonishingly, every apple in the basket was eaten. But, contrary to expectations, the dragonfruit remained untouched.'

# pattern = r'\b\w+\b'

# aORe = []

# listing = re.findall(pattern, text)

# for i in listing:
    
#     if re.match(r'^a|^e', i):
        
#         aORe.append(i)
        

# print(aORe)

# print(f'{ len(aORe)} words are matched in the given number.') 

#------------------------------------------------------------------------------------------------

# pattern = r'\b[ae]\w*\b' 

# match = re.findall(pattern, text)

# print(match)

"""Task 13.
Write a Python program to separate and print the numbers and their position in a given string.
"""

# text = 'The marathon had 26.2 miles, and by mile 18, I felt the weight of every step.'

# pattern = r'\d+'

# sepa = re.split(pattern, text)

# match = re.findall(pattern, text)

# print(f'The numbers are separated like : {sepa}')

# if match:
#     for i in re.finditer(pattern, text):
        
#         print(f'The separated numbers are :{i.group()} and the position was at {i.start()} to {i.end()} ')
        

"""Task 14.
Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""

# def abbreviate():
    
#     # text = 'On our family trip, we took the Old Forest Road, which led us through some enchanting landscapes.'
#     # text = 'During our cross-country drive, we traversed the Pacific Coast Road, the Rocky Road, and finally the famous Route 66 Road'
    
#     text = input("Enter any text containing the word 'Road' to convert as Rd: ")
    
#     pattern = r'Road'
    
#     match = re.findall(pattern, text)
#     results = []
#     if match:
#         pattern2 = r'Rd.'
#         replace = re.sub(pattern, pattern2, text )
        
#         for i in re.finditer(pattern2, replace):
            
        
#             result = f'The word "Road" is abbreviated as "{i.group()}".\nthe position of the modified word is at {i.start()} to {i.end()}'
#             results.append(result)
        
#         return replace, "\n\n".join(results)
            
#     else :
#         return 'There is not match.'
    
# modified_text, abbreviations = abbreviate()

# print('-'* 40)
# print(f'The modified_text : {modified_text}')
# print('-'* 40)
# print(abbreviations)

# """Task 15.
# Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# """
# def replacer():
    
#     text = input('Enter any text to replace space, comma, or dot with a colon: ')
    
#     pattern = r'[\s,\.]'
    
#     replace = re.sub(pattern, r':', text)
    
#     return replace

# print(replacer())

"""Task 16.
Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon."""

# def replacer():
    
#     text = input('Enter any text to replace space, comma, or dot with a colon: ')
    
#     pattern = r'[\s,\.]{2}'
    
#     replace = re.sub(pattern, r':', text)
    
#     return replace

# print(replacer())

def max_two ():
    
    text = input('Enter any text to replace space, comma, or dot with a colon:')
    
    pattern = r'[\s,\.]'
    
    replace = re.subn(pattern, r':', text, count= 2)
    
    return replace

print(max_two())