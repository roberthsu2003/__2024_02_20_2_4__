from pydantic import BaseModel, RootModel

class Item(BaseModel):
    name:str
    height:float
    weight:float

    def show(self):
        print(f'姓名: {self.name}, BMI: {self.bmi}, {self.judgment}')

    @property
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2
    
    @property
    def judgment(self) -> str:
        if self.bmi < 18.5:
            return '體重過輕'
        elif self.bmi < 24:
            return '正常範圍'
        elif self.bmi < 27:
            return '過重'
        elif self.bmi < 30:
            return '輕度肥胖'
        elif self.bmi < 35:
            return '中度肥胖'
        else:
            return '重度肥胖'

############################

class Items(RootModel):
    root:list[Item]

    def showAll(self):
        for item in self.root:
            item.show()

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, idx):
        return self.root[idx]

############################

def getItems() -> Items:
    names:list[dict] = [
        {'name':'徐xx','height':178,'weight':78},
        {'name':'王xx','height':168,'weight':75},
        {'name':'張xx','height':183,'weight':78}
    ]

    items:Items = Items.model_validate(names)

    return items

############################