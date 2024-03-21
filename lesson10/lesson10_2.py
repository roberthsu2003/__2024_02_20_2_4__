from tools import get_names,get_scores
import pyinputplus as pyip
from pprint import pprint

def main():
    nums:int = pyip.inputInt("請輸入學生數(1~30):",min=1,max=30)
    names:list[str] = get_names(nums=nums)
    scores = get_scores(names)
    pprint(scores)

if __name__ == '__main__':
    main()