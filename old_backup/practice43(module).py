# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) #5명 군인이 영화 보러 갔을 때 가격

# import theater_module as mv #mv 별명으로 호출 모듈명이 길 때
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning #모듈 내에서 필요한 것만 호출
# price(5)
# price_morning(3) 
# #price_soldier는 오류가 난다. 호출을 안했기 때문에.

from theater_module import price_soldier as price
price(4)