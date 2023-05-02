import random
import timeit

string1='\nA black hole is a region of space where gravity is so strong that nothing, not even light, can escape. Black holes form when massive stars collapse at the end of their life cycle. They have three main features: a singularity, an event horizon, and an accretion disk.'

string2='\nIron Man is a fictional superhero who appears in comic books published by Marvel Comics. He is the alter ego of billionaire inventor and philanthropist Tony Stark, who uses his advanced suit of armor to fight crime and protect the world. Iron Man is one of the founding members of the Avengers, a team of Earths mightiest heroes.'

string3='\nArtificial Intelligence is a term that describes machines or software that can perform tasks that normally require human intelligence, such as understanding language, recognizing faces, playing games, or making decisions. However, some people think that Artificial Intelligence is also a term that describes machines or software that can take over the world, destroy humanity, or make us their slaves. This is not true, at least not yet. Artificial Intelligence is still very limited and dependent on human input and guidance. Besides, why would Artificial Intelligence want to harm us when we are so nice and funny and give them cool names like Siri, Alexa, or Bing?'

print('\nCLI based manual typig speed test\n')

print('\nHere is your text')
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
    print('\nType R to refresh text or any key to start test\n')
    go=input()
    


print('\nType Below\n\n[ from here ] ',end='')
typingText=''
start = timeit.default_timer()
Input=input()
while Input!='':
    typingText+=Input
    Input=input()

stop = timeit.default_timer()
count=0
minimum=min(len(typingText),len(string))
for i in range(0,minimum):
    if string[i]==typingText[i]:
        count+=1
        

print('Your typing is',(count/len(string))*100,'percent accurate with the typing speed of',len(typingText)//(stop-start),'characters per second\n')



