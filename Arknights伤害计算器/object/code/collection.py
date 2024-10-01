import data_object

class ATKCollections:
    ATKCollections_dict = {}
    all_collections = []
    finall_Data = {}

    def __init__(self, Id: int):
        self.Id = Id
        data = self.getData()
        self.No = data.get('No', 0)  # 设置默认值为 0
        self.Name = data.get('Name', 'Unknown')  # 设置默认值为 'Unknown'
        # 增益类型
        self.ATK_Inc_Mult = data.get('ATK_Inc_Mult', 0.0)  # 设置默认值为 1.0
        self.Dmg_Inc = data.get('Dmg_Inc', 0.0)  # 设置默认值为 0.0
        self.Phy_Dmg_Inc = data.get('Phy_Dmg_Inc', 0.0)
        self.Spell_Dmg_Inc = data.get('Spell_Dmg_Inc', 0.0)
        self.True_Dmg_Inc = data.get('True_Dmg_Inc', 0.0)
        self.Vul = data.get('Vul', 0.0)
        self.Phy_Vul = data.get('Phy_Vul', 0.0)
        self.Spell_Vul = data.get('Spell_Vul', 0.0)
        self.True_Dmg_Inc = data.get('True_Dmg_Inc', 0.0)
        self.ATK_Mult = data.get('ATK_Mult', 0.0)
        self.Prec_Dec_DEF = data.get('Prec_Dec_DEF', 0.0)
        self.Dec_Spell_RES = data.get('Dec_Spell_RES', 0.0)
        self.Ign_Spell_RES = data.get('Ign_Spell_RES', 0.0)
        self.Prec_Dec_Spell_RES = data.get('Prec_Dec_Spell_RES', 0.0)
        self.collection_list = []

        self.ATKCollections_dict[self.No] = {
            'Id' : self.Id
            ,'No' : self.No
            , 'Name' : self.Name
            , 'ATK_Inc_Mult' : self.ATK_Inc_Mult
            , 'Dmg_Inc' : self.Dmg_Inc
            , 'Phy_Dmg_Inc' : self.Phy_Dmg_Inc
            , 'Spell_Dmg_Inc' : self.Spell_Dmg_Inc
            , 'Vul' : self.Vul
            , 'Phy_Vul' : self.Phy_Vul
            , 'Spell_Vul' : self.Spell_Vul
            , 'True_Dmg_Inc' : self.True_Dmg_Inc
            , 'ATK_Mult' : self.ATK_Mult
            , 'Prec_Dec_DEF' : self.Prec_Dec_DEF
            , 'Dec_Spell_RES' : self.Dec_Spell_RES
            , 'Ign_Spell_RES' : self.Ign_Spell_RES
            , 'Prec_Dec_Spell_RES' : self.Prec_Dec_Spell_RES}
        self.collection_list.append(self.ATKCollections_dict[self.No])
        self.all_collections.append(self.ATKCollections_dict[self.No])
        self.collectionFinallData()

    def getData(self):
        return data_object.data[self.Id]
    
    @classmethod
    def collectionFinallData(self):
        ATK_Inc_Mult = 0
        Dmg_Inc_base = 1
        # print(ATKCollections.all_collections)
        # 去重(放置反复选中藏品)
        unique_data = list(set(tuple(item.items()) for item in self.all_collections))
        self.all_collections = [dict(item) for item in unique_data]
        # print(ATKCollections.all_collections)
        for collection in self.all_collections:
            # print(collection)
            # print(collection['ATK_Inc_Mult'])
            ATK_Inc_Mult +=collection['ATK_Inc_Mult']
            # print('直接乘算{}'.format(ATK_Inc_Mult))
            Dmg_Inc =Dmg_Inc_base * (1+collection['Dmg_Inc']) - 1
            # print('最终乘算{}'.format(Dmg_Inc))

        Dmg_Inc = round(Dmg_Inc,3)
        print('直接乘算{}'.format(round(ATK_Inc_Mult,3)))
        print('最终乘算{}'.format(round(Dmg_Inc,3)))
        self.finall_Data['ATK_Inc_Mult'] = ATK_Inc_Mult
        self.finall_Data['Dmg_Inc'] = Dmg_Inc

class DefenseCollections:
    def __init__(self,No,Name,):
        self.No = No
        self.Name = Name
        pass

class HPCollections:
    def __init__(self,No,Name,):
        self.No = No
        self.Name = Name
        pass

# 我方增益
class EnemyAttackCollections:
    def __init__(self,No,Name,):
        self.No = No
        self.Name = Name
        pass

class EnemyDefenseCollections:
    def __init__(self,No,Name,):
        self.No = No
        self.Name = Name
        pass

class EnemyHPCollections:
    def __init__(self,No,Name,):
        self.No = No
        self.Name = Name
        pass

