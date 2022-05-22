from re import M


class PlayerCharector:
    Charector_List = ["드로즈2세","댐","드라지"]
    Skill_List = [["검의 신판","강력한 의지","근력강화","분노의 일격"]]
    Skill_damage = [[100,0,0,150]]
    stats_list = [[10,0,100,100,1000]]

    attack = 1
    magic_power = 1
    amor = 1
    magic_amor = 1
    player_HP = 1000
    charector_number=0

    def __init__(self, num):
        self.charector_number = num
        self.set_stat(self.stats_list[num][0], self.stats_list[num][1], self.stats_list[num][2], self.stats_list[num][3], self.stats_list[num][4])

    def set_stat(self,attack,magic_power,amor,magic_amor,player_HP):
        self.attack = attack
        self.magic_power = magic_power
        self.amor = amor
        self.magic_amor = magic_amor
        self.player_HP = player_HP
    
    @staticmethod
    def get_charetor_list():
        return PlayerCharector.Charector_List 
    
    def get_HP(self):
        return self.player_HP
    
    def set_HP(self,hp):
        self.player_HP=hp
        return self.player_HP
    
    def sub_HP(self,hp):
        self.player_HP-=hp
        return self.player_HP
    
    def add_HP(self,hp):
        self.player_HP+=hp
        return self.player_HP

    def get_skills(self):
        return self.Skill_List[self.charector_number] 

    def get_skill_name(self,skill_num):
        return self.Skill_List[self.charector_number][skill_num]

    def get_skill_damage(self,skill_num):
        
        return self.Skill_damage[self.charector_number][skill_num]

    # def drows():
    #     global stats
    #     stats = [1,2,3,4,1000]
    #     print(stats)

    # def drows_Skill():
    #     for i in Skill_List:
    #         print(str(Skill_List.index(i)+1)+"."+i)
    #     global use_skill
    #     use_skill=input("")

    