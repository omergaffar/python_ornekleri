#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:15:23 2017

@author: acs
"""
"""
Burada denklem çözmede daireyi yapacağız.
İlk olarak matematik olarak tanımlıyoruz.
Numpy kütüphanesini ekliyoruz.
Koordinat düzleminde x ve y'yi tanımlıyoruz.
Arange kullanarak dairenin matematiksel işlemlerini yazıyoruz.
En son olarakda for döngüsüyle koordinat sisteminde yerini belirliyoruz.
"""
from sympy.solvers import solve
# sympy solvers komutuyla çalıştırmaya yarar.
from sympy import Symbol
import numpy as np
from matplotlib import pyplot as plt
x = Symbol('x')
# x'i symbolle tanımlattı
y = np.arange(-1.0,1.01,0.1)
# arange komutuyla daire nin matematiksel komutları girildi.
xp=[]
xn=[]
#for döngüsüyle koordinat düzleminde dairenin yeri belirlendi.
for yi in y:
    sol=solve(x**2 +yi**2-1.0,x)
    print sol
    xp.append(sol[0])
    xn.append(sol[-1])
    print xp[-1],xn[-1]
plt.plot(xp,y)
plt.plot(xn,y)




