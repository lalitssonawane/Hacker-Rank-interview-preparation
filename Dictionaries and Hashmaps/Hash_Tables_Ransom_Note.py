#Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

#Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

from collections import Counter

def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    return "Yes" if ( a & b ) == b else "No"

m,n = map(int,input().split())
magazine = input().split()
note = input().split()
print(checkMagazine(magazine, note))