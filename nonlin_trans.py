#!/usr/bin/python
import non_lsp as lsp
import numpy as np
runs = 10
e_out = 0
e_in = 0
for loop in range(0,runs):
  # generate data
  num_pts = 100
  d = lsp.generate_f(num_pts)
  data = d[0]
  l = d[1]
  data2 = d[2]

  # derive linear regression line
  #x = np.matrix([data.x,data.y,np.ones(num_pts)])
  xpow = []
  ypow = []
  xy = []
  for i in range(0,data.num_pts):
    xpow.append(data.x[i]**2)
    ypow.append(data.y[i]**2)
    xy.append(data.x[i]*data.y[i])
  x = np.matrix([np.ones(num_pts),data.x,data.y,xy,xpow,ypow])
  y = np.matrix(data.sign)
  x_inv = np.linalg.pinv(x.T)
  w = np.dot(x_inv,y.T)
  #print(w)
  l2 = lsp.line()
  l2.A = w.item(0,0)
  l2.B = w.item(1,0)
  l2.C = w.item(2,0)
  l2.D = w.item(3,0)
  l2.E = w.item(4,0)
  l2.F = w.item(5,0)
  l2.m = float(-1)*l2.A/float(l2.B)
  l2.b = float(-1)*l2.C/l2.B

  # plot data
  #lsp.show_plot(data,l,l2)

  # calc e_in
  in_miss = 0
  for i in range(0,data.num_pts):
    if data.sign[i] > 0:
      if data.y[i] < float(l2.m)*data.x[i]+l2.b:
        in_miss+=1
    else:
      if data.y[i] > float(l2.m)*data.x[i]+l2.b:
        in_miss+=1
  if in_miss > data.num_pts/2:
    in_miss = data.num_pts - in_miss
  in_miss = in_miss/float(data.num_pts)
  e_in+=in_miss
  # calc e_out
  out_miss = 0
  for i in range(0,data2.num_pts):
    print(data2.sign[i], 1 if l2.A+l2.B*data2.x[i]+l2.C*data2.y[i]+l2.D*data2.x[i]*data2.y[i]+l2.E*data2.x[i]**2+l2.F*data2.y[i]**2 > 0 else -1) 
    if data2.sign[i] * (l2.A+l2.B*data2.x[i]+l2.C*data2.y[i]+l2.D*data2.x[i]*data2.y[i]+l2.E*data2.x[i]**2+l2.F*data2.y[i]**2) < 0:
      out_miss+=1
      print("miss")
  e_out+=out_miss/float(data2.num_pts)
print("E in:",e_in/float(runs))
print("E out:",e_out/float(runs))
