property_multiplier = {"pink": 1.1, "orange":1.2, "red":1.3, "yellow":1.4, "green":1.5, "dark_blue":1.6, "brown":1.7, "light_blue":1.8}


class Player:
    def __init__(self):
        self.money = 0
        self.base_roll = 10
        self.base_go = 200
        self.properties = {} #{'color_number':owned_state,...}  color_number = pink_1, owned_state = 0 (owned), 1 (1 classroom), etc up to 4 classrooms
        self.buffs = [] #double dice, prop_disc, 
        pass

    def update_property(self,property:str): #property = str "pink_1"
        if self.properties.get(property):
            self.properties[property] += 1
        else:
            self.properties[property] = 0
    
    def pass_go(self): #user has passed go
        total_multiplier = 0
        for color in self.properties:
            total *= property_multiplier[color.split('_')[0]]
        
        self.money += self.base_go * total_multiplier

    def roll(self,dice_total:int): #user has rolled
        self.money += self.base_roll * dice_total

    def upgrade(self,upg_type:str): #upg_type = "roll"/"go"
        if(upg_type == "roll"):
            self.base_roll *= 2
        else:
            self.base_go *= 1.5
    
    def update_buffs(self,buff:str): #buff = "double_dice","prop_disc"
        if buff not in self.buffs:
            self.buffs.append(buff)

