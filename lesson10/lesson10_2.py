from tools import get_names
import pyinputplus as pyip

def main():
    nums:int = pyip.inputInt("請輸入學生數(1~30):",min=1,max=30)
    names:list[str] = get_names(nums=nums)
    print(names)

if __name__ == '__main__':
    main()