import random
import timeit
import math

string1='\nA black hole is a region of space where gravity is so strong that nothing, not even light, can escape. Black holes form when massive stars collapse at the end of their life cycle. They have three main features: a singularity, an event horizon, and an accretion disk.'

string2='\nIron Man is a fictional superhero who appears in comic books published by Marvel Comics. He is the alter ego of billionaire inventor and philanthropist Tony Stark, who uses his advanced suit of armor to fight crime and protect the world. Iron Man is one of the founding members of the Avengers, a team of Earths mightiest heroes.'

string3='\nArtificial Intelligence is a term that describes machines or software that can perform tasks that normally require human intelligence, such as understanding language, recognizing faces, playing games, or making decisions. However, some people think that Artificial Intelligence is also a term that describes machines or software that can take over the world, destroy humanity, or make us their slaves. This is not true, at least not yet. Artificial Intelligence is still very limited and dependent on human input and guidance. Besides, why would Artificial Intelligence want to harm us when we are so nice and funny and give them cool names like Siri, Alexa, or Bing?'

print('\nCLI based static typing speed test\n')

print('Here is your text')
temp=0
string='NULL'
go='R'
while go=='R':
    temp=random.randint(1,3)
    if temp==1:
        string=string1
        print(string)
    elif temp==2:
        string=string2
        print(string)
    else:
        string=string3
        print(string)
    print('\nType R to refresh text or any press ENTER to start test')
    go=input()
    


print('Type Below\n[ from here ] ',end='')
typingText=''
start = timeit.default_timer()
Input=input()
while Input!='':
    typingText+=Input
    Input=input()

stop = timeit.default_timer()
count=0

def levenshtein_distance(string1, string2):
  len1 = len(string1)
  len2 = len(string2)
  if len1 == 0:
    return len2
  if len2 == 0:
    return len1
  dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
  for i in range(len1 + 1):
    dp[i][0] = i
  for j in range(len2 + 1):
    dp[0][j] = j
  for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
      if string1[i - 1] == string2[j - 1]:
        cost = 0
      else:
        cost = 1
      dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
  return dp[len1][len2]

dis=levenshtein_distance(typingText,string)
count=max(0,len(string)-dis)

print('Your typing is',(((count)/len(string))*100),'percent accurate with the typing speed of',(count)//(stop-start),'characters per second\n')
print('*Typing Speed is based on the correct inputs - the characters those matched*\n')
