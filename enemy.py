import random

class enemy:
    Skill_List = ["응애","때리기"]
    Skill_damage = [10,1]
    
    attack = 1
    magic_power = 1
    amor = 1
    magic_amor = 1
    enemy_hp=300

    # def __init__(self):
    #     self.charector_number = num
    #     self.set_stat(self.stats_list[num][0], self.stats_list[num][1], self.stats_list[num][2], self.stats_list[num][3], self.stats_list[num][4], self.stats_list[num][5])

    # def set_stat(self,attack,magic_power,amor,magic_amor,player_HP):
    #     self.attack = attack
    #     self.magic_power = magic_power
    #     self.amor = amor
    #     self.magic_amor = magic_amor
    #     self.player_HP = player_HP
    
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


    def get_skills(self):
        return self.Skill_List 

    def get_skill_name(self,skill_num):
        return self.Skill_List[skill_num]
    

    def get_skill_damage(self,skill_num):
        return self.Skill_damage[skill_num]
    
    def get_random_skill(self):
        skill_num = random.randint(0,len(self.Skill_List)-1)
        # E_use=random.choice(Enumy_Skill_list)
        # if E_use == "응애":
        #     print("적:응애")
        return skill_num
    
    # def get_skill_script(self):
        