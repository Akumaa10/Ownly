property_value = {"pink":{0:250,1:300,2:360,3:576,4:691},
                  "orange":{0:1250,1:1350,2:1500,3:1800,4:2160},
                  "red":{0:2500,1:3000,2:3600,3:4320,4:5180},
                  "yellow":{0:3750,1:4500,2:5400,3:6480,4:7780},
                  "green":{0:12500,1:15000,2:18000,3:21600,4:25900},
                  "blue":{0:25000,1:30000,2:36000,3:43200,4:51800},
                  "brown":{0:125000,1:150000,2:180000,3:216000,4:259000},
                  "cyan":{0:250000,1:300000,2:360000,3:432000,4:5180000}}
boosts_multipler = {"roll":{1:10,2:30,3:90,4:270,5:810},"go":{1:1.1,2:1.25,3:1.5,4:1.75,5:2}}

class Player:
    def __init__(self):
        self.money = 100000000
        self.base_roll = boosts_multipler["roll"][1]
        self.base_go = 200
        self.properties = {} #{'color_number':owned_state,...}  color_number = pink_1, owned_state = 0 (owned), 1 (1 classroom), etc up to 4 classrooms
        self.buffs = [] #double dice, prop_disc, 
        self.position = 32
        self.boosts = {"roll":1,"go":1} 
        pass

    def update_property(self,property:str): #property = str "pink_1"
        if self.properties.get(property):
            self.properties[property] += 1
        else:
            self.properties[property] = 0
    
    def pass_go(self): #user has passed go
        prop_total = 0
        for color in self.properties:
            prop_total += property_value[color.split("_")[0]][self.properties[color]]
        
        self.money += (self.base_go + prop_total) * boosts_multipler["go"][self.boosts["go"]]

    def roll(self,dice_total:int): #user has rolled
        self.money += boosts_multipler["roll"][self.boosts["roll"]] * dice_total

    def upgrade(self,upg_type:str): #upg_type = "roll"/"go"
        if(upg_type == "roll"):
            self.base_roll *= 2
        else:
            self.base_go *= 1.5
    
    def update_buffs(self,buff:str,price:int): #buff = "hertz","hunt","blanton"
        if buff not in self.buffs and self.money >= price:
            self.buffs.append(buff)
            self.money -= price

    def update_boosts(self,boost:str,price:int): #boost = "roll"/"go"
        print(self.boosts[boost] < 5 and self.money >= price)
        if self.boosts[boost] < 5 and self.money >= price:
            self.boosts[boost] += 1
            self.money -= price
        
