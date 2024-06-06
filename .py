import random

an2=random.randint(4,6)
an3=random.randint(4,6)
an4=random.randint(4,6)
an5=random.randint(4,6)
an1=25-an5-an2-an3-an4

if an1 > 6 or an1 < 4:
    while an1 > 6 or an1 < 4:
        an2=random.randint(4,6)
        an3=random.randint(4,6)
        an4=random.randint(4,6)
        an5=random.randint(4,6)
        an1=25-an5-an2-an3-an4
        if 4<= an1 <=6:
            break    

number=1
answerlist=[]
a = {}

while number < 26:
    answer=random.randint(1,5)
    answerlist.extend([answer])
    a[number] = answer
    number=number+1
    if answerlist.count(1) == an1+1 and answer == 1:
        answerlist.pop()
        number=number-1
    else:
        pass
    if answerlist.count(2) == an2+1 and answer == 2:
        answerlist.pop()
        number=number-1
    else:
        pass
    if answerlist.count(3) == an3+1 and answer == 3:
        answerlist.pop()
        number=number-1
    else:
        pass
    if answerlist.count(4) == an4+1 and answer == 4:
        answerlist.pop()
        number=number-1
    else:
        pass
    if answerlist.count(5) == an5+1 and answer == 5:
        answerlist.pop()
        number=number-1
    else:
        continue
        
    


하나로_찍었을때_점수=random.randint(1,5)
score=answerlist.count(하나로_찍었을때_점수)*4
score2=0

ans2=random.randint(4,6)
ans3=random.randint(4,6)
ans4=random.randint(4,6)
ans5=random.randint(4,6)
ans1=25-an5-an2-an3-an4

if ans1 > 6 or ans1 < 4:
    while ans1 > 6 or ans1 < 4:
        ans2=random.randint(4,6)
        ans3=random.randint(4,6)
        ans4=random.randint(4,6)
        ans5=random.randint(4,6)
        ans1=25-ans5-ans2-ans3-ans4
        if 4<= ans1 <=6:
            break    

number2=1
answerlist2=[]
a2 = {}

while number2 < 26:
    answer2=random.randint(1,5)
    answerlist2.extend([answer2])
    a2[number2] = answer2
    number2=number2+1
    if answerlist2.count(1) == ans1+1 and answer2 == 1:
        answerlist2.pop()
        number2=number2-1
    else:
        pass
    if answerlist2.count(2) == ans2+1 and answer2 == 2:
        answerlist2.pop()
        number2=number2-1
    else:
        pass
    if answerlist2.count(3) == ans3+1 and answer2 == 3:
        answerlist2.pop()
        number2=number2-1
    else:
        pass
    if answerlist2.count(4) == ans4+1 and answer2 == 4:
        answerlist2.pop()
        number2=number2-1
    else:
        pass
    if answerlist2.count(5) == ans5+1 and answer2 == 5:
        answerlist2.pop()
        number2=number2-1
    else:
        continue

s=0
while s<=24:
    if answerlist[s] == answerlist2[s]:
        score2=score2+4
        s=s+1
        
    else:
        s=s+1
        continue

print('일자로 찍은 번호 :', 하나로_찍었을때_점수)
print('시험지 답지 :', a)
print('여러 번호로 찍은 시험지 :', a2)
print('한 번호로 찍었을때 점수 :', score)
print('여러 번호로 찍었을때 점수 :', score2)
if score > score2:
    print('한 번호로 찍었을때 여러 번호로 찍었을때보다 점수가 높습니다.')
elif score == score2:
    print('한 번호로 찍었을때의 점수와 여러 번호로 찍었을때의 점수가 같습니다.')
else:
    print('여러 번호로 찍었을때 한 번호로 찍었을때보다 점수가 높습니다.')