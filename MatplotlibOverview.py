Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.arange(1,50)
>>> y = np.random.randint(5,100,50)
>>> len(x)
49
>>> len(y)
50
>>> x = np.arange(1,51)
>>> len(x)
50
>>> len(y)
50
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000029804FFA668>]
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x000002980775B2E8>

>>> plt.show()
>>> 
