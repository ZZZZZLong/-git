#基础属性（文本框需要填入的）
class attributes:
    class ally:
        def __init__(self,ATK:float,ATK_Inc_Mult:float=0,Fin_ATK_Add:float=0,ATK_Mult:float=0,Dmg_Inc:float=0,Vul:float=0,Dec_DEF:int=0,Prec_Dec_DEF:float=0):
            self.ATK = ATK                      #基础攻击力
            self.ATK_Inc_Mult = ATK_Inc_Mult    #攻击力增加倍率
            self.Fin_ATK_Add = Fin_ATK_Add      #最终加算攻击力
            self.ATK_Mult = ATK_Mult            #攻击力增幅
            self.Dmg_Inc = Dmg_Inc              #增伤
            self.Vul = Vul                      #易伤
            self.Dec_DEF = Dec_DEF              #固定减防
            self.Prec_Dec_DEF = Prec_Dec_DEF    #百分比减防
            print("当前输入我方属性 基础攻击力：{} 攻击力增加倍率：{} 最终加算攻击力：{} 增伤：{} 易伤：{} 固定减防:{} 百分比减防:{}"
                  .format(self.ATK,self.ATK_Inc_Mult,self.Fin_ATK_Add,self.ATK_Mult,self.Dmg_Inc,self.Vul,self.Dec_DEF,self.Prec_Dec_DEF))

        def __iter__(self):
            self._index = 0
            self._attributes = [self.ATK, self.ATK_Inc_Mult, self.Fin_ATK_Add, self.ATK_Mult, self.Dmg_Inc,self.Vul, self.Dec_DEF, self.Prec_Dec_DEF]
            return self

        def __next__(self):
            if self._index >= len(self._attributes):
                raise StopIteration
            value = self._attributes[self._index]
            self._index += 1
            return value
        
    class enemy:
        def __init__(self,Emy_HP:int=500,Emy_DEF:float=0,Emy_DEF_Add:float=0,Emy_DEF_Inc_Mult:float=0,Emy_Spell_RES:int=0,Emy_Spell_RES_Add:int=0,Emy_Spell_RES_Inc_Mult:float=0,Emy_Perc_Dmg_Red:float=0):
            self.Emy_HP=Emy_HP                                          #敌方基础生命值
            self.Emy_DEF=Emy_DEF                                        #敌方基础防御力
            self.Emy_DEF_Add=Emy_DEF_Add                                #敌方防御力增加
            self.Emy_DEF_Inc_Mult=Emy_DEF_Inc_Mult                      #敌方防御力增加倍率
            self.Emy_Spell_RES = Emy_Spell_RES                          #敌方基础法抗
            self.Emy_Spell_RES_Add = Emy_Spell_RES_Add                  #敌方法抗增加
            self.Emy_Spell_RES_Inc_Mult = Emy_Spell_RES_Inc_Mult        #敌方法抗增加倍率
            self.Emy_Perc_Dmg_Red=Emy_Perc_Dmg_Red                      #敌方减伤
            print("当前输入敌方属性")
            print("基础生命值：{} 基础防御力：{} 防御力增加：{} 防御力增加倍率：{} 基础法抗：{} 法抗增加：{} 法抗增加倍率：{} 减伤：{}"
                  .format(Emy_HP,Emy_DEF,Emy_DEF_Add,Emy_DEF_Inc_Mult,Emy_Spell_RES,Emy_Spell_RES_Add,Emy_Spell_RES_Inc_Mult,Emy_Perc_Dmg_Red))

        def __iter__(self):
            self._index = 0
            self._attributes = [self.Emy_DEF,self.Emy_DEF_Add,self.Emy_DEF_Inc_Mult,self.Emy_Perc_Dmg_Red]
            return self
        
        def __next__(self):
            if self._index >= len(self._attributes):
                raise StopIteration
            value = self._attributes[self._index]
            self._index += 1
            return value
    
    def basicFinallData(allay,enemy):
        dic = {}
        ally_attr = vars(allay)
        enemy_attr = vars(enemy)

        print("="*20+"添加敌人前"+"="*20)

        for attr,val in ally_attr.items():
            dic[attr] = val
        print(dic)
        print("="*20+"添加敌人后"+"="*20)
        for attr,val in enemy_attr.items():
            dic[attr] = val
        print(dic)
        return dic
        
        
    


