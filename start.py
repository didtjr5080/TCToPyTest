#ver.Y2022M05D26h19m27

import random
import time
import os
import player_list
import enemy

# Charector_List =["드로즈2세","댐","드라지"]
# charactor=[]
# Skill_List=["검의 신판","강력한 의지","근력강화","분노의 일격"]
# Drows_Damage_List = [100,0,0,150]
# stats=[1,1,1,1,1000] #공격력, 주문력,방어력, 마법저항력, 체력

# Player_HP=stats[len(stats)-1]
# Enemy_HP=1000
test_enemy = enemy.enemy()

# Enumy_Skill_list=["응애","때리기"]
# Enumy_Skill_Damage=[0,1]

player_c= None

E_use=""
use_skill=""

def screen_clear(): #환경에 따라 화면 클리어 명령어
    os.system("cls")  
    try:
        os.system("cls")
    except:
        os.system("clear")



def Pick_To_Type():
    screen_clear()
    global player_c
    Charector_List = player_list.PlayerCharector.get_charetor_list()
    
    for i in Charector_List:
        print(str(Charector_List.index(i)+1)+"."+i)
    star_type = input("원하시는 캐릭터 고르세요:")
    check_to_type = star_type.isdigit() #int인지 확인하는 함수 int면 true값 출력됨
    #########################################오류 방지를 위한 입력값 검사코드#########################################
    if check_to_type:
        star_type= int(star_type)
        if star_type > len(player_list.PlayerCharector.Charector_List):
            screen_clear()
            Pick_To_Type()
        elif star_type <= 0:
            screen_clear()
            Pick_To_Type()
        else:
            screen_clear()
            print(Charector_List[(int(star_type))-1],"을 선택하셨습니다","\n","이대로 플레이 하시겠습니까?[y/n]")
            p_a = input("")
        
            if p_a == "y":
                # charactor.append(Charector_List[(int(star_type))-1])
                # if charactor[0] == "드로즈2세":
                #     drows()
                player_c = player_list.PlayerCharector((int(star_type))-1)
            else:
                Pick_To_Type()
    else:
        screen_clear()
        Pick_To_Type()
####################################################################################################################
# def drows():
#     global stats
#     stats = [1,2,3,4,1000]
#     print(stats)

def select_Skill():
    global player_c
    Skill_List = player_c.get_skills()
    for i in Skill_List:
        print(str(Skill_List.index(i)+1)+"."+i)
    # global use_skill
    use_skill=input("")
    return int(use_skill) - 1

# def Enemy_Skill():
#     global E_use
#     E_use=random.choice(Enumy_Skill_list)
#     if E_use == "응애":
#         print("적:응애")

def fight():
    global test_enemy, player_c
    Enemy_HP = test_enemy.get_HP()
    Player_HP = player_c.get_HP()
    # if charactor[0] == "드로즈2세":
    #     drows_Skill()
    #     print(Skill_List[int(use_skill)-1],"사용!")
    #     Enemy_HP -= Drows_Damage_List[int(use_skill)-1]
    used_skill = select_Skill()
    print(player_c.get_skill_name(used_skill),"사용!")
    # Enemy_HP = test_enemy.sub_HP(player_c.get_skill_damage(used_skill))
    this_damage = player_c.get_skill_damage_array(used_skill)
    Enemy_HP = test_enemy.take_damage(this_damage[0], this_damage[1], this_damage[2], this_damage[3])
    # Enemy_HP -= player_c.get_skill_damage(used_skill)
    
    time.sleep(0.5)
    
    enemy_used_skill = test_enemy.get_random_skill()
    this_damage = test_enemy.get_skill_damage_array(enemy_used_skill)
    Player_HP = player_c.take_damage(this_damage[0], this_damage[1], this_damage[2], this_damage[3])
    # Player_HP = player_c.sub_HP(test_enemy.get_skill_damage(enemy_used_skill))
    # Player_HP -= test_enemy.get_skill_damage(enemy_used_skill)
    print("적이",test_enemy.get_skill_name(enemy_used_skill) , "사용!")
    time.sleep(0.5)
    print("플레이어 hp:",Player_HP)
    print("적 hp:", Enemy_HP)
    # time.sleep(0.5)
    # if player_c.get_HP() < 0:
    #         print("Player win")
    #         Enemy_HP = test_enemy.get_HP()
    #         Player_HP = player_c.get_HP()
    # elif test_enemy.get_HP() < 0:
    #     print("Player Lose")
    #     Enemy_HP = test_enemy.get_HP()
    #     Player_HP = player_c.get_HP()

    

Pick_To_Type()
print("0. 게임 종료")
print("1. 전투")
plyer_command_input = input("")
check_to_command = plyer_command_input.isdigit()#plyer_command_input값이 숫자 값인지 검사
print(check_to_command)

while plyer_command_input != 0:#입력값이 0이면 루프 끝남
    if check_to_command:#plyer_command_input값이 숫자값이면 int로 변환
        plyer_command_input = int(plyer_command_input)
    else:
        while not check_to_command:
            screen_clear()
            time.sleep(1)
            screen_clear
            print("원하는 행동을 선택해주세요")
            print("0. 게임 종료")
            print("1. 전투")
            plyer_command_input = input("")
            check_to_command = plyer_command_input.isdigit()
            print(check_to_command) 
            
    
    if plyer_command_input == 1:
        plyer_command_input = -1
        while player_c.get_HP() > 0 and test_enemy.get_HP() > 0:
            screen_clear()
            print("플레이어 hp:",player_c.get_HP())
            print("적 hp:", test_enemy.get_HP())
            fight()
            #####전투 후 hp초기화#####
            if player_c.get_HP() >= 0:
                print("Player win")
                Enemy_HP = test_enemy.get_HP()
                Player_HP = player_c.get_HP()
                continue
            elif test_enemy.get_HP() >= 0:
                print("Player Lose")
                Enemy_HP = test_enemy.get_HP()
                Player_HP = player_c.get_HP()
                continue
            ########################
    else: #지정된 값이 아니면 다시 인풋값 받음
        screen_clear()
        # time.sleep(0.5)
        screen_clear
        print("원하는 행동을 선택해주세요")
        print("0. 게임 종료")
        print("1. 전투")
        plyer_command_input = input("")
        check_to_command = plyer_command_input.isdigit()
        print(check_to_command) 
        

screen_clear()
print("End Game")

