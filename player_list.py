class PlayerCharector:
    attack = 10 #공격력
    magic_power = 1 #주문력
    amor = 5 # 방어력
    magic_amor = 50 #마법저항력
    player_HP = 1000 #기본 캐릭터 체력
    charector_number=0 #캐릭터 번호

    Charector_List = ["드로즈2세","댐","드라지"] #캐릭터 리스트
    Skill_List = [["검의 신판","강력한 의지","근력강화","분노의 일격"]] #캐릭터 스킬 리스트 이중 리스트
    Skill_basic_damage = [[0,0,0,150]] #스킬 공격력 데미지 리스트 이중 리스트
    Skill_basic_magic_damage = [[100,0,0,0]] #스킬 주문력 데미지 리스트 이중 리스트
    Skill_damage_per = [[0.2,0,0,0]] #스킬 공격력 데미지 리스트 퍼센트 이중 리스트
    Skill_magic_damage_per = [[0,0,0,0.5]] #스킬 주문력 데미지 리스트 퍼센트 이중 리스트
    stats_list = [[10,0,100,100,1000]] #캐릭터 스텟 리스트 이중 변수

    

    def __init__(self, num):
        self.charector_number = num
        self.set_stat(self.stats_list[num][0], self.stats_list[num][1], self.stats_list[num][2], self.stats_list[num][3], self.stats_list[num][4])

    def set_stat(self, attack, magic_power, amor,magic_amor, player_HP):
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
    
    def set_HP(self, hp):
        self.player_HP=hp
        return self.player_HP
    
    def sub_HP(self, hp):
        self.player_HP-=hp
        return self.player_HP
    
    def add_HP(self, hp):
        self.player_HP+=hp
        return self.player_HP

    def take_damage(self, damege, amor_per, magic_damage, magic_amor_per): # 모든 형태의 인자에 따라 데미지를 받게하는 함수 (데미지, 아머퍼, 매직데이지, 매직아머퍼)
        self.add_damage(damege, amor_per)
        self.add_magic_damage(magic_damage, magic_amor_per)
        return self.player_HP

    def add_damage(self, damage, amor_per):
        self.player_HP -= damage - self.amor*amor_per
        return self.player_HP

    def add_magic_damage(self, magic_damage, magic_amor_per):
        self.player_HP -= magic_damage - self.magic_amor*magic_amor_per
        return self.player_HP


    def get_skills(self):
        return self.Skill_List[self.charector_number] 

    def get_skill_name(self, skill_num):
        return self.Skill_List[self.charector_number][skill_num]

    # def get_skill_damage(self,skill_num):
    #     return self.Skill_basic_damage[self.charector_number][skill_num] #과거에 썼던 함수

    def get_skill_damage_array(self, skill_num): #스킬 번호에 해당하는 스킬 데미지를 배열 형태로 출력하는 함수 (데미지, 아머퍼, 매직데이지, 매직아머퍼)
        just_damage = self.Skill_basic_damage[self.charector_number][skill_num] + self.attack*self.Skill_damage_per[self.charector_number][skill_num]
        magic_damage = self.Skill_basic_magic_damage[self.charector_number][skill_num] + self.magic_power*self.Skill_magic_damage_per[self.charector_number][skill_num]

        damage_per = self.Skill_damage_per[self.charector_number][skill_num]
        magic_per = self.Skill_magic_damage_per[self.charector_number][skill_num]

        data = [just_damage, damage_per, magic_damage, magic_per]
        return data

    

    # def drows():
    #     global stats
    #     stats = [1,2,3,4,1000]
    #     print(stats)

    # def drows_Skill():
    #     for i in Skill_List:
    #         print(str(Skill_List.index(i)+1)+"."+i)
    #     global use_skill
    #     use_skill=input("")


