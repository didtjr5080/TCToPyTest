import random
import player_list

class enemy:
    attack = 5
    magic_power = 1
    amor = 10
    magic_amor = 10
    enemy_hp=1000
    Skill_basic_damage = [0, 100] #스킬 공격력 데미지 리스트
    Skill_basic_magic_damage = [100, 0] #스킬 주문력 데미지 리스트
    Skill_damage_per = [0, 0.2] #스킬 공격력 데미지 리스트 퍼센트
    Skill_magic_damage_per = [0.5, 0] #스킬 주문력 데미지 리스트 퍼센트

    Skill_List = ["응애", "때리기"]
    
    
    # def __init__(self):
    #     self.charector_number = num
    #     self.set_stat(self.stats_list[num][0], self.stats_list[num][1], self.stats_list[num][2], self.stats_list[num][3], self.stats_list[num][4], self.stats_list[num][5])

    # def set_stat(self,attack,magic_power,amor,magic_amor,enemy_hp):
    #     self.attack = attack
    #     self.magic_power = magic_power
    #     self.amor = amor
    #     self.magic_amor = magic_amor
    #     self.enemy_hp = enemy_hp
    
    def get_HP(self):
        return self.enemy_hp
    
    def set_HP(self,hp):
        self.enemy_hp=hp
        return self.enemy_hp
    
    def sub_HP(self,hp):
        self.enemy_hp-=hp
        return self.enemy_hp
    
    def add_HP(self,hp):
        self.enemy_hp+=hp
        return self.enemy_hp

    def take_damage(self, damege, amor_per, magic_damage, magic_amor_per): # 모든 형태의 인자에 따라 데미지를 받게하는 함수 (데미지, 아머퍼, 매직데이지, 매직아머퍼)
        self.add_damage(damege, amor_per)
        self.add_magic_damage(magic_damage, magic_amor_per)
        return self.enemy_hp

    def add_damage(self, damage, amor_per):
        self.enemy_hp -= damage - self.amor*amor_per
        return self.enemy_hp

    def add_magic_damage(self, magic_damage, magic_amor_per):
        self.enemy_hp -= magic_damage - self.magic_amor*magic_amor_per
        return self.enemy_hp

    def add_damege(self, damege, amor_per):
        self.enemy_hp -= damege - self.amor*amor_per
        return self.enemy_hp

    def add_magic_damege(self, magic_damege, magic_amor_per):
        self.enemy_hp -= magic_damege - self.magic_amor*magic_amor_per
        return self.enemy_hp


    def get_skills(self):
        return self.Skill_List 

    def get_skill_name(self,skill_num):
        return self.Skill_List[skill_num]
    

    # def get_skill_damage(self,skill_num):
    #     return self.Skill_damage[skill_num]

    def get_skill_damage_array(self, skill_num): #스킬 번호에 해당하는 스킬 데미지를 배열 형태로 출력하는 함수 (데미지, 아머퍼, 매직데이지, 매직아머퍼)
        just_damage = self.Skill_basic_damage[skill_num] + self.attack*self.Skill_damage_per[skill_num]
        magic_damage = self.Skill_basic_magic_damage[skill_num] + self.magic_power*self.Skill_magic_damage_per[skill_num]

        damage_per = self.Skill_damage_per[skill_num]
        magic_per = self.Skill_magic_damage_per[skill_num]

        data = [just_damage, damage_per, magic_damage, magic_per]
        return data
    
    def get_random_skill(self):
        skill_num = random.randint(0,len(self.Skill_List)-1)
        # E_use=random.choice(Enumy_Skill_list)
        # if E_use == "응애":
        #     print("적:응애")
        return skill_num
    
    # def get_skill_script(self):
        