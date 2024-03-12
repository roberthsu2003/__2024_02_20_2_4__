import random
import pyinputplus as pyip

def play_game():
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print("========猜數字遊戲=========\n")
    print(target)
    while(True):
        keyin = pyip.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
        print(keyin)
        count += 1
        if keyin == target:
            print(f'賓果!猜對了, 答案是:{target}')
            print(f'您猜了{count}次')
            break
        elif (keyin > target):
            print("再小一點")
            max = keyin - 1
        elif (keyin < target):
            print("再大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")

while(True):
    play_game()
    is_again:str = input("請問還要繼續嗎(y,n)?")
    if not is_again == 'y':
        break
      
print("遊戲結束!") 