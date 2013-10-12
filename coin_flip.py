#!/usr/bin/python
import random

def flip_coin():
  # heads = 1, tails = 0
  return random.randint(0,1)

def flip_coin_ten_times():
  head_count = 0
  for i in range(0,10):
    head_count += flip_coin()
  return head_count/float(10)
    
def flip_one_thousand_coins():
  first_result = 0
  rand_result = 0
  min_result = 0
  result = []
  for i in range(0,1000):
    result.append(flip_coin_ten_times())
  first_result = result[0]
  rand_result = result[random.randint(0,999)]
  min_result = min(result)
  return (first_result, rand_result, min_result)

def flip_ten_thousand():
  ten_k = 10000
  ave_result = [0.0,0.0,0.0]
  for i in range(0,ten_k):
    result = flip_one_thousand_coins()
    ave_result[0]+=result[0]
    ave_result[1]+=result[1]
    ave_result[2]+=result[2]
  ave_result[0]/=ten_k
  ave_result[1]/=ten_k
  ave_result[2]/=ten_k
  return ave_result
  
print(flip_ten_thousand())
