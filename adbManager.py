import subprocess
import random

# 定义答题框区域，用于随机点击该区域内的位置
answeringArea = [[0,1070],[1080,1900]] # 答题框区域 [[起始坐标x,起始坐标y],[结束坐标x,结束坐标y]]

# 定义开心按钮区域，用于随机点击该区域内的位置
happyArea = [[280,1480],[800,1620]] # 开心按钮区域 [[起始坐标x,起始坐标y],[结束坐标x,结束坐标y]]

# 定义继续按钮区域（榜单右下角的继续按键），用于随机点击该区域内的位置
continueArea_1 = [[620,2040],[950,2140]] # 继续按钮区域（榜单右下角的继续按键） [[起始坐标x,起始坐标y],[结束坐标x,结束坐标y]]

# 定义继续按钮区域（继续PK的继续按键），用于随机点击该区域内的位置
continueArea_2 = [[500,1780],[930,1890]] # 继续按钮区域（继续PK的继续按键） [[起始坐标x,起始坐标y],[结束坐标x,结束坐标y]]

# 随机点击答题框区域内的位置
def answerQuestion():
  # 使用adb命令模拟点击操作，点击位置为答题框区域内的随机点
  subprocess.run(["adb","shell","input","tap",str(random.randint(answeringArea[0][0],answeringArea[1][0])),str(random.randint(answeringArea[0][1],answeringArea[1][1]))])

# 随机点击开心按钮区域内的位置
def clickHappy():
  # 使用adb命令模拟点击操作，点击位置为开心按钮区域内的随机点
  subprocess.run(["adb","shell","input","tap",str(random.randint(happyArea[0][0],happyArea[1][0])),str(random.randint(happyArea[0][1],happyArea[1][1]))])

# 随机点击榜单右下角的继续按键区域内的位置
def clickContinue_1():
  # 使用adb命令模拟点击操作，点击位置为继续按钮区域（榜单右下角的继续按键）内的随机点
  subprocess.run(["adb","shell","input","tap",str(random.randint(continueArea_1[0][0],continueArea_1[1][0])),str(random.randint(continueArea_1[0][1],continueArea_1[1][1]))])

# 随机点击继续PK的继续按键区域内的位置
def clickContinue_2():
  # 使用adb命令模拟点击操作，点击位置为继续按钮区域（继续PK的继续按键）内的随机点
  subprocess.run(["adb","shell","input","tap",str(random.randint(continueArea_2[0][0],continueArea_2[1][0])),str(random.randint(continueArea_2[0][1],continueArea_2[1][1]))])