#!/usr/bin/python
import random
import matplotlib.pyplot as plt
import numpy as np
class plot:
  def __init__(self):
    self.x = []
    self.y = []
    self.sign = []
    self.pos_x = []
    self.pos_y = []
    self.neg_x = []
    self.neg_y = []
    self.num_pts = 0

class line():
  def __init__(self):
    self.m = 0
    self.b = 0
    self.A = 0
    self.B = 0
    self.C = 0
    self.D = 0
    self.E = 0
    self.F = 0

def generate_f(num_pts):
  x1=random.uniform(-1,1)
  x2=random.uniform(-1,1)
  y1=random.uniform(-1,1)
  y2=random.uniform(-1,1)

  # y = mx + b
  l = line()
  l.m = ((y2-y1)/(x2-x1))
  l.b = y1 - l.m*x1
  data = plot()
  data.num_pts = num_pts
  for i in range(0,num_pts):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    data.x.append(x)
    data.y.append(y)
    if x**2 + y**2 - 0.6 > 0:
      data.pos_x.append(x)
      data.pos_y.append(y)
      data.sign.append(1)
    else:
      data.neg_x.append(x)
      data.neg_y.append(y)
      data.sign.append(-1)
  # add noise
  for i in range(0,num_pts//10):
    data.sign[random.randint(0,num_pts-1)] *= -1
  data2 = plot()
  data2.num_pts = num_pts*10
  for i in range(0,data2.num_pts):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    data2.x.append(x)
    data2.y.append(y)
    if x**2 + y**2 - 0.6 > 0:
      data2.pos_x.append(x)
      data2.pos_y.append(y)
      data2.sign.append(1)
    else:
      data2.neg_x.append(x)
      data2.neg_y.append(y)
      data2.sign.append(-1)
  #print("f: y="+str(l.m)+"*x+"+str(l.b))
  l.A = y1-y2
  l.B = x2-x1
  l.C = (x1-x2)*y1 + (y2-y1)*x1
  #print("f: "+str(l.A)+"x+"+str(l.B)+"y="+str(l.C))
  return (data,l,data2)

def show_plot(d,l,l2):
  plt.plot(d.pos_x,d.pos_y,'ro', d.neg_x,d.neg_y,'bo')
  x = np.linspace(-15,15,d.num_pts)
  y = l.m*x+l.b
  plt.plot(x,y,'g-')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.axis([-1,1,-1,1])
  y2 = l2.m*x+l2.b
  plt.plot(x,y2,'r-')
  plt.show()
