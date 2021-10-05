#Regular experssion module:
"""
Meta Char:
[] :Set of char
. : any char
^ : starts with
$ : Ends with(to be applied at end)
* : zero or more occerance
+ :one or more occurence
{x} : exctly  x no of occurence
| : Either/or
() : capture and grp


#Special char
\A: return match if string starts with
\b : return matches where words starts(applied at start) or ends(applied at end) with
\B : return matches where words contains expression but dont starts(applied at start) or ends(applied at end) with it
\d : returns matches if string contains any digits: 0-9
\D : returns matches if doesnot contains digits
\w : contains word char(all alpha,digits,underscores)
\W : doesnot contains char(all symbols and spaces)
\Z : end of string
"""
import re
mystr='''the quantities, characters, or symbols 25
on which operations are performed by a computer 6025,
which may be stored and transmitted 32b5 
in the form of electrical %signals and recorded on 
magnetic, optical, or mechanical recording media.'''

p=re.compile(r'the') #Normal
#p=re.compile(r'.the') #.==any char
#p=re.compile(r'^the') #  string starts with
#p=re.compile(r'the$') # Ends with
#p=re.compile(r'th*') # t and 0 or more h
#p=re.compile(r'th+') # t and 1 or more h
#p=re.compile(r'th{2}')# t and exactly 2 h
#p=re.compile(r'(the)*') # returns 0 or more 'the' together
#p=re.compile(r'th{2} | a') # gives 'a' and 'thth' places



#special seq

#p=re.compile(r'\Athe') #String starts with "the"
#p=re.compile(r'\bthe') #mathces where words starts with "the"
#p=re.compile(r'he\b') #mathces where words ends with "he"
#p=re.compile(r'he\b') #mathces where words ends with "he"
#p=re.compile(r'\Bthe') #mathces where words contains with "the" but dont start with it
#p=re.compile(r'the\B') #mathces where words contains with "the" but dont ends with it
#p=re.compile(r'3\db') #mathces where we have digits,Note itc can e applied anywhere
#p=re.compile(r'\Db') #mathces where we dont have digits,Note itc can e applied anywhere
#p=re.compile(r'\sb') #mathces where we  have spaces,Note itc can e applied anywhere
#p=re.compile(r'\Sb') #mathces where we have dont have spaces,Note itc can e applied anywhere
#p=re.compile(r'\wb') #mathces where we  have any word char,Note itc can e applied anywhere
#p=re.compile(r'\W') #mathces where we  dont have any word char,Note itc can e applied anywhere
#p=re.compile(r'ia\Z')#String ends with "ia"





mat=p.finditer(mystr)
for m in mat:
    print(m)