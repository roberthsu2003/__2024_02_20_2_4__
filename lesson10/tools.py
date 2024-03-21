import random

def get_names(nums:int = 5) -> list[str]:
    with open('names.txt',encoding='utf8') as file:
        content:str = file.read()
        names:list[str] = content.split(sep='\n')
        random_names:list[str] = random.choices(names,k=nums)
    return random_names