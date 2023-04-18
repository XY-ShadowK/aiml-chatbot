import aiml
import os

question_path='../chatbot/corpus'
os.chdir(question_path)

question=aiml.Kernel()
question.learn("question.aiml")

print("问卷测试!")

i=1
score=0
never=0
often=0

while i<=14 :
    print(question.respond("QUESTION "+str(i)))
    tempStr=input()
    if tempStr=="A" :
        never+=1
    if tempStr=="B" :
        score+=1
    if tempStr=="C" :
        often+=1
        score+=2

if score>=14 and never<3 and often>=6 :
    print("您的孩子得分为"+str(score)+",可能为自闭症，分数越高可能性越大")
else :
    print("您的孩子得分为"+str(score)+",不太可能是自闭症")
