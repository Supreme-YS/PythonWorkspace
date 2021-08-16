Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> 
>>> t.shape('turtle')
>>> for i in range(4):
	t.forward(100)
	t.rt(100)

	
>>> 
================================ RESTART: Shell ================================
>>> import turtle as t
>>> t.shape('turtle')
f
>>> for i in range(4):
	t.forward(100)
	t.rt(90)

	
>>> 
================================ RESTART: Shell ================================
>>> #오각형 그리기
>>> import turtle as t
>>> 
>>> t.shape('turtle')
>>> for i in range(5):
	t.forward(100)
	t.rt(360 / 5)

	
>>> 
================================ RESTART: Shell ================================
>>> #사용자가 원하는 다각형 그리기
>>> import turtle as t
>>> 
>>> n = int(input())
8
>>> t.shape('turtle')
>>> for i in range(n):
	t.forward(100)
	t.right(360 / n)

	
>>> 
================================ RESTART: Shell ================================
>>> import turtle as t
>>> n = 12
>>> t.shape('turtle')
>>> t.color('red')
>>> 
>>> t.begin_fill()
>>> for i in range(n):
	t.forward(100)
	t.right(360 / n)

>>> t.end_fill()
>>> 