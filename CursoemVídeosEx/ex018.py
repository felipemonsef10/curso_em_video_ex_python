import trigonometry
aq = float(input('Coloque um ângulo qualquer: '))
sen = trigonometry.sin_ang(aq)
cos = trigonometry.cos_ang(aq)
tang = trigonometry.tan_ang(aq)
print('O seno, o cosseno e a tangente de {} respecticamente é:\n{}\n{}\n{}'.format(aq, sen, cos, tang))

import math
aq = float(input('Coloque um ângulo qualquer: '))
sen = math.sin(math.radians(aq))
cos = math.cos(math.radians(aq))
tang = math.tan(math.radians(aq))
print('O seno, o cosseno e a tangente de {} respecticamente é:\n{:.2f}\n{:.2f}\n{:.2f}'.format(aq, sen, cos, tang))