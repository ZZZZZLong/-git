class calculate:
    """
        物理伤害计算公式     
    def phyDmg(self,ATK=0,ATK_Mod=1,ATK_Add=0,ATK_Inc_Mult=0,Fin_ATK_Add=0,ATK_Mult=0,Skill_Dmg_Mult=1,Vul=0,Dmg_Inc=0,Dec_DEF=0,Prec_Dec_DEF=0,Ign_DEF=0,Ign_Mul_DEF=0,Emy_DEF=0,Emy_DEF_Add=0,Emy_DEF_Inc_Mult=0,Emy_Perc_Dmg_Red=0):
    
        DPH = max(0.05*((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*(1+Vul)*(1+Dmg_Inc)*(1-Emy_Perc_Dmg_Red),
                (((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult-((Emy_DEF+Emy_DEF_Add-Dec_DEF)*(1+Emy_DEF_Inc_Mult)*(1-Prec_Dec_DEF)-Ign_DEF)*(1-Ign_Mul_DEF))*(1+Vul)*(1+Phy_Vul)*(1+Dmg_Inc)*(1+Phy_Dmg_Inc)(1-Emy_Perc_Dmg_Red))
        return round(DPH,3)
    """

    @staticmethod
    def phyDmg(dic):
        #我方属性
        ATK = dic.get('ATK', 0)
        ATK_Mod = dic.get('ATK_Mod', 1)
        ATK_Add = dic.get('ATK_Add', 0)
        ATK_Inc_Mult = dic.get('ATK_Inc_Mult', 0)
        Fin_ATK_Add = dic.get('Fin_ATK_Add', 0)
        ATK_Mult = dic.get('ATK_Mult', 0)
        Skill_Dmg_Mult = dic.get('Skill_Dmg_Mult', 1)
        Vul = dic.get('Vul', 0)
        Phy_Vul = dic.get('Phy_Vul', 0)
        Dmg_Inc = dic.get('Dmg_Inc', 0)
        Phy_Dmg_Inc = dic.get('Phy_Dmg_Inc', 0)
        Dec_DEF = dic.get('Dec_DEF', 0)
        Prec_Dec_DEF = dic.get('Prec_Dec_DEF', 0)
        Ign_DEF = dic.get('Ign_DEF', 0)
        Ign_Mul_DEF = dic.get('Ign_Mul_DEF', 0)
        #敌方属性
        Emy_DEF = dic.get('Emy_DEF', 0)
        Emy_DEF_Add = dic.get('Emy_DEF_Add', 0)
        Emy_DEF_Inc_Mult = dic.get('Emy_DEF_Inc_Mult', 0)
        Emy_Perc_Dmg_Red = dic.get('Emy_Perc_Dmg_Red', 0)

        DPH = max(((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*(1+Vul)*(1+Dmg_Inc)*(1-Emy_Perc_Dmg_Red)*0.05,
                (((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult-max(0,((Emy_DEF+Emy_DEF_Add-Dec_DEF)*(1+Emy_DEF_Inc_Mult)*(1-Prec_Dec_DEF)-Ign_DEF)*(1-Ign_Mul_DEF)))*(1+Vul)*(1+Phy_Vul)*(1+Dmg_Inc)*(1+Phy_Dmg_Inc)*(1-Emy_Perc_Dmg_Red))
        return round(DPH,3)
    """
        法术伤害计算公式    
        def magDmg(self,ATK=0,ATK_Mod=1,ATK_Add=0,ATK_Inc_Mult=0,Fin_ATK_Add=0,ATK_Mult=0,Skill_Dmg_Mult=1,Vul=0,Dmg_Inc=0,Dec_Spell_RES=0,Prec_Dec_Spell_RES=0,Ign_Spell_RES=0,Emy_Spell_RES=0,Emy_Spell_RES_Add=0,Emy_Spell_RES_Inc_Mult=0,Emy_Perc_Dmg_Red=0):
        
        DPH = max(((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*0.05*(1+Vul)*(1+Dmg_Inc)*(1-Emy_Perc_Dmg_Red),
                  ((ATK*ATK_Add+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*0.01*(100-max(0,min(100,((Emy_Spell_RES+Emy_Spell_RES_Add-Dec_Spell_RES)*(1+Emy_Spell_RES_Inc_Mult)*(1-Prec_Dec_Spell_RES)-Ign_Spell_RES))))*(1+Vul)*(1+Spell_Vul)*(1+Dmg_Inc)*(1+Spell_Dmg_Inc)*(1-Emy_Perc_Dmg_Red))
        return round(DPH,3)
    """
    @staticmethod
    def speDmg(dic):
        #我方属性
        ATK = dic.get('ATK', 0)
        ATK_Mod = dic.get('ATK_Mod', 1)
        ATK_Add = dic.get('ATK_Add', 0)
        ATK_Inc_Mult = dic.get('ATK_Inc_Mult', 0)
        Fin_ATK_Add = dic.get('Fin_ATK_Add', 0)
        ATK_Mult = dic.get('ATK_Mult', 0)
        Skill_Dmg_Mult = dic.get('Skill_Dmg_Mult', 1)
        Vul = dic.get('Vul', 0)
        Spell_Vul = dic.get('Spell_Vul', 0)
        Dmg_Inc = dic.get('Dmg_Inc', 0)
        Spell_Dmg_Inc = dic.get('Spell_Dmg_Inc', 0)
        Dec_Spell_RES = dic.get('Dec_Spell_RES', 0)
        Prec_Dec_Spell_RES = dic.get('Prec_Dec_Spell_RES', 0)
        Ign_Spell_RES = dic.get('Ign_Spell_RES', 0)
        #敌方属性
        Emy_Spell_RES = dic.get('Emy_Spell_RES', 0)
        Emy_Spell_RES_Add = dic.get('Emy_Spell_RES_Add', 0)
        Emy_Spell_RES_Inc_Mult = dic.get('Emy_Spell_RES_Inc_Mult', 0)
        Emy_Perc_Dmg_Red = dic.get('Emy_Perc_Dmg_Red', 0)
        print(Spell_Vul)
        
        DPH = max(((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*0.05*(1+Vul)*(1+Dmg_Inc)*(1-Emy_Perc_Dmg_Red),
                  ((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*0.01*(100-max(0,min(100,((Emy_Spell_RES+Emy_Spell_RES_Add-Dec_Spell_RES)*(1+Emy_Spell_RES_Inc_Mult)*(1-Prec_Dec_Spell_RES)-Ign_Spell_RES))))*(1+Vul)*(1+Spell_Vul)*(1+Dmg_Inc)*(1+Spell_Dmg_Inc)*(1-Emy_Perc_Dmg_Red))
        return round(DPH,3)

    # 真实伤害计算公式   
    @staticmethod
    def trueDmg(dic):
        #我方属性
        ATK = dic.get('ATK', 0)
        ATK_Mod = dic.get('ATK_Mod', 1)
        ATK_Add = dic.get('ATK_Add', 0)
        ATK_Inc_Mult = dic.get('ATK_Inc_Mult', 0)
        Fin_ATK_Add = dic.get('Fin_ATK_Add', 0)
        ATK_Mult = dic.get('ATK_Mult', 0)
        Skill_Dmg_Mult = dic.get('Skill_Dmg_Mult', 1)
        Vul = dic.get('Vul', 0)
        True_Dmg_Inc = dic.get('True_Dmg_Inc', 0)
        Dmg_Inc = dic.get('Dmg_Inc', 0)

        DPH = ((ATK*ATK_Mod+ATK_Add)*(1+ATK_Inc_Mult)+Fin_ATK_Add)*(1+ATK_Mult)*Skill_Dmg_Mult*(1+Vul)*(1+True_Dmg_Inc)*(1+Dmg_Inc)
        return round(DPH,3)