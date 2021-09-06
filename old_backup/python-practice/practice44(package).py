# #패키지 = 모듈을 모아놓은 것
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand)) 