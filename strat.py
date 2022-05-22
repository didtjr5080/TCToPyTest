import random
import time
import os

Charector_List =["드로즈2세","댐","드라지"]
charactor=[]
Skill_List=["검의 신판","강력한 의지","근력강화","분노의 일격"]
Drows_Damage_List = [100,0,0,150]
stats=[1,1,1,1,1000] #공격력, 주문력,방어력, 마법저항력, 체력

# Player_HP=stats[len(stats)-1]
# Enemy_HP=1000

Enumy_Skill_list=["응애","때리기"]
Enumy_Skill_Damage=[0,1]


E_use=""
use_skill=""

def Pick_To_Type():
    for i in Charector_List:
        print(str(Charector_List.index(i)+1)+"."+i)
    global star_type
    star_type = input("원하시는 캐릭터 고르세요:")
    os.system("cls")
    print(Charector_List[(int(star_type))-1],"을 선택하셨습니다","\n","이대로 플레이 하시겠습니까?[y/n]")
    p_a = input("")
    charactor.append(Charector_List[(int(star_type))-1])
    if p_a == "y":
        if charactor[0] == "드로즈2세":
            drows()
    else:
        Pick_To_Type()

def drows():
    global stats
    stats = [1,2,3,4,1000]
    print(stats)

def drows_Skill():
    for i in Skill_List:
        print(str(Skill_List.index(i)+1)+"."+i)
    global use_skill
    use_skill=input("")

def Enemy_Skill():
    global E_use
    E_use=random.choice(Enumy_Skill_list)
    if E_use == "응애":
        print("적:응애")

def fight():
    global Player_HP, Enemy_HP
    if charactor[0] == "드로즈2세":
        drows_Skill()
        print(Skill_List[int(use_skill)-1],"사용!")
        Enemy_HP -= Drows_Damage_List[int(use_skill)-1]
    Enemy_Skill()
    time.sleep(0.5)
    Player_HP -= Enumy_Skill_Damage[Enumy_Skill_list.index(random.choice(Enumy_Skill_list))]
    print("적이",Enumy_Skill_list[int(Enumy_Skill_list.index(E_use)) - 1], "사용!")
    time.sleep(0.5)
    print("플레이어 hp:",Player_HP)
    print("적 hp:", Enemy_HP)
    time.sleep(1)

    

Pick_To_Type()
 
while Player_HP >= 0 or Enemy_HP<=0:
    os.system("cls")
    print("플레이어 hp:",Player_HP)
    print("적 hp:", Enemy_HP)
    fight()
