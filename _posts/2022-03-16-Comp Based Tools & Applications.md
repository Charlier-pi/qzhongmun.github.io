```
def test1(*a,**b):
  print(a,b)
  
test1(2,3,4,x=1,y=2)

//result is (2,3,4) {x=1,y=2}
------------------------------------------------------------------------------------
def test4(**a):
  b= list(a.values())
  return b[0] + b[1]*b[2]
test4(x=5,y=6,z=12)      //77

def factorial(n):
  if n ==0:
    return 1
  else:
    return n+factorial(n-1) 
factorial(10000)   //50005001

import sys
sys.setresursionlimit(20000)
sys.getresursionlimit(). //20000

func = lambda x,y: x+y
func(4,6) //10

func = lambda x: x**5
func(5) //3125

(lambda x: x**5)(4)     //1024

f = lambda : [x**3 for x in range(10)]
f()  //[0,1,8,27,64,...,729]

(lambda : [x**3 for x in range(10)])()

def countdown():
  yield 5
  yield 4
  yield 2
  yield 0
g = countdown()
next(g)
g = iter([5,4,2,0])
next(g)      //0

def countdown():
    for i in range(5,0,-1):
        yield i
 g = countdown()
 next(g)
 
 import numpy as np
 def test5(a,b):
    return a*b
 sumvec= np.vectorize(test5)
 y= sumvec([1,3,5,6],5)
y.dtype  //dtype("int64)

[1,3,5,6]*5 //[1,3,5,6,1,3,5,6,1,3,5,6,1,3,5,6,1,3,5,6]

def plus1(f):
    def wrapper(*args,**kwargs):
        return f(*args,**kwargs) + 1
    return wrapper

@plus1 
def power(base, x):
    return base**x
power(4,2)   //17
------------------------------------------------------------------------------------
a=1
help(a)
dir(a)

a.as_integer_ratio()  //(1,1)

a.__abs__() //1

abs(a). //1

import math
from math import sin
dir(sin)

sin.__dic__
--------------------------
class Particle(object):
  """A particle ...
  c: charge
  m: mass
  r: position"""
  
  roar = " I am a particle "
  def __init__(self):
    self.c = 0
    self.m = 0
    self.r ={"x":0,"y":0,"z":0}
Particle.roar  //" I am a particle "
print(Particle.roar) // I am a particle 
p= Particle()
p.roar //" I am a particle "
print(p.c)    //0
--------------------------
class Particle(object):
  """A particle ...
  c: charge
  m: mass
  r: position"""
  
  roar = " I am a particle "
  def __init__(self,charge,mass,position):
    self.c = charge
    self.m = mass
    self.r =position
    
  def hear_me(self):
     myroar = self.roar + ("My charge is :" + str(self.c) + "My mass is:" + str(self.m) + "My x position is :" + str(self.r[x]))
     print(myroar)
  def delta_x_min(self, delta_p_x):
      hbar = constants.hbar
      delx_min = hbar / (3.0 * delta_p_x)
      return delx_min
  def possible_flavors():
      return ["up","down","top","bottom"]
p= Particle(1,0.1,{"x":10,"y":20,"z":50})
print(p.r)   //{"x":10,"y":20,"z":50}
p.hear_me()
print(Particle.possible_flavors())   //["up","down","top","bottom"]
--------------------------
from scipy import constants
m_e = constants.m_e   // or constants.electron_mass
r_e = {"x":1,"y":5,"x":65}
elec = Particle(-1,m_e,r_e)
elec.hear_me()

dir(constants)
--------------------------
class ElementaryParticle(Particle):
  roar = " I am an elementary particle."
  def  __init__(self, charge, mass, position,spin):
      Particle.__init__(self,charge,mass,position)
      self.s = spin
      self.is_fermion = bool(spin%1.0)
      self.is_boson = not self.is_fermion
 spin = 1.5
 p = ElementaryParticle(1,m_e,r_e,spin)
 print(p.s)      //1.5
 p.hear_me()  // I am ...
 
 def add_fs_particle(cls):
    cls.is_particle = True
    return cls
 @add_is_particle
 class Particle(object):
  """A particle ...
  c: charge
  m: mass
  r: position"""
  
  roar = " I am a particle "
  def __init__(self,charge,mass,position):
    self.c = charge
    self.m = mass
    self.r =position
    
  def hear_me(self):
     myroar = self.roar + ("My charge is :" + str(self.c) + "My mass is:" + str(self.m) + "My x position is :" + str(self.r[x]))
     print(myroar)
  def delta_x_min(self, delta_p_x):
      hbar = constants.hbar
      delx_min = hbar / (3.0 * delta_p_x)
      return delx_min
  def possible_flavors():
      return ["up","down","top","bottom"]

Particle.is_particle //true
--------------------------
from math import sqrt
def add_distance(cls):
    def distance(self,other):
        d2 = 0.0
        for axis in ["x","y","z"]:
            d2 + = (self.r[axis]-other.r[axis])**2
        d = sqrt(d2)
        return d
     cls.distance = distance
     return cls
@add_distance
class Particle(object):
  """A particle ...
  c: charge
  m: mass
  r: position"""
  
  roar = " I am a particle "
  def __init__(self,charge,mass,position):
    self.c = charge
    self.m = mass
    self.r =position
    
  def hear_me(self):
     myroar = self.roar + ("My charge is :" + str(self.c) + "My mass is:" + str(self.m) + "My x position is :" + str(self.r[x]))
     print(myroar)
  def delta_x_min(self, delta_p_x):
      hbar = constants.hbar
      delx_min = hbar / (3.0 * delta_p_x)
      return delx_min
  def possible_flavors():
      return ["up","down","top","bottom"]
 m_e = constants.m_e
 m_p = constants.m_p
 r_p = {"x":0,"y":0,"z":0}
 r_e = {"x":0,"y":10,"z":40}
 p1 = Particle(1.m_p,r_p)
 p2 = Particle(11,m_e,r_e)
 p1.distance(p2)       //42.426...
```
