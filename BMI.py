__H__ = input('請輸入身高: ')
__W__ = input('請輸入體重: ')
__H__ = int(__H__)
__W__ = int(__W__)
__BMI__ = __W__ *10000 / (__H__ * __H__)
print('你的BMI是 ', __BMI__)
if __BMI__ >= 35:
  print('重度肥胖')
elif __BMI__ >= 30 and __BMI__ < 35:
  print('中度肥胖')
elif __BMI__ >= 27 and __BMI__ < 30:
  print('輕度肥胖')
elif __BMI__ >= 24 and __BMI__ < 27:
  print('過重')
elif __BMI__ >= 18.5 and __BMI__ < 24:
  print('正常範圍')
else:
  print('體重過輕')
