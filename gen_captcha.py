# 导入所需的模块
import random
import time
import hashlib
from PIL import Image, ImageDraw, ImageFont

# 定义一个函数，用于生成随机的四则运算表达式和结果
def generate_expression_and_result():
    # 随机选择两个10以内的整数
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    # 随机选择一个运算符，+ - * /
    operator = random.choice(['+', '-', '*', '/'])
    # 根据运算符计算结果，并保留两位小数
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        if num1 == 0:
            expression = str(num1) + operator + str(num2) + '=?'
            return (expression, 0)
        else:
            pass
        # 如果除数为0，则重新生成表达式和结果
        if num2 == 0:
            return generate_expression_and_result()
        else:
            result = round(num1 / num2, 2)
    # 将表达式和结果转换为字符串，并添加等号和问号
    expression = str(num1) + operator + str(num2) + '=?'
    result = str(result)
    # 返回表达式和结果的元组
    return (expression, result)

# 定义一个函数，用于生成验证码图片并保存到指定目录下
def generate_captcha_image(expression):
    # 创建一个白色背景的图片对象，大小为200x100像素
    image = Image.new('RGB', (200, 100), (255, 255, 255))
    # 创建一个绘图对象，用于在图片上绘制文字或图形
    draw = ImageDraw.Draw(image)
    # 创建一个字体对象，用于指定文字的字体和大小，这里使用Arial.ttf字体文件，大小为40像素
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 55)
    # 获取表达式的宽度和高度（以像素为单位）
    width, height = font.getsize(expression)
    # 计算表达式在图片上居中显示时的左上角坐标（以像素为单位）
    x = (200 - width) // 2 
    y = (100 - height) // 2 
    # 在图片上绘制黑色文字，并指定文字内容、位置、字体和颜色 
    draw.text((x,y), expression ,font=font ,fill=(0 ,0 ,0)) 
    # 返回图片对象 
    return image 

    # 定义一个函数，用于将图片对象保存到指定目录下，并以结果作为文件名 
def save_image(image ,result): 
    # 指定目录名称 
    directory ='.\\captcha_train\\' 
    # 指定文件名，格式为png 
    filename=str(hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()) + '_' + str(result) + '_' + '.png' 
    # 拼接完整的路径名 
    path=directory+''+filename 
    # 将图片对象保存到路径名对应的文件中 
    image.save(path) 

    # 测试代码：生成10个验证码图片并保存到captcha_train目录下

for i in range(100):
    expression,result=generate_expression_and_result()
    image=generate_captcha_image(expression)
    save_image(image,result)
    