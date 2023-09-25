# 求一元二次方程的根
import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
x1 = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
x2 = ((-b-math.sqrt(b**2-4*a*c))/(2*a))
print("x1=", x1, "\n", "x2=", x2)

