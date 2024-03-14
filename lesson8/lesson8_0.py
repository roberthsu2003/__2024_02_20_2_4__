def inputFloat(prompt:str,min:float,max:float)->float:
    while(True):
        try:
            value:float = float(input(prompt))
            if value >= min and value <= max:
                return value
            else:
                value = print("輸入的範圍有問題請重新輸入")                
        except:
           print("格式有問題請重新輸入")
           
            
        
        

    
height = inputFloat("請輸入身高:",min=0,max=300)

weight = inputFloat("請輸入體重:",min=0,max=300)

bmi = weight / (height / 100) ** 2

print(f'您的BMI是: {bmi:.1f}')

if bmi < 18.5:
    msg = '體重過輕'
elif bmi < 24:
    msg = '正常範圍'
elif bmi < 27:
    msg = '過重'
elif bmi < 30:
    msg = '輕度肥胖'
elif bmi < 35:
    msg = '中度肥胖'
else:
    msg = '重度肥胖'

print(f'您的體重: {msg}')