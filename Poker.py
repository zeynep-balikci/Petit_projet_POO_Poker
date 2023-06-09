#!/bin/env python3
from random import randrange
import numpy as np

class Carte():
    valeurs = list(range(7,11)) + ['Valet','Dame','Roi','As']
    couleurs = ['Coeur','Carreau','Pique','Trèfle']

    def __init__(self,v=None,c=None):
        if v:
            if not v in Carte.valeurs:
                raise ValueError(f"{v}: valeur incorrecte")
        else:
            v = Carte.valeurs[randrange(0,len(Carte.valeurs))]

        if c:
            if not c in Carte.couleurs:
                raise ValueError(f"{c}: couleur incorrecte")
        else:
            c = Carte.couleurs[randrange(0,len(Carte.couleurs))]

        self.couleur = c
        self.valeur = v
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def __eq__(self,q):
      return self.valeur==q.valeur and self.couleur==q.couleur

    def __hash__(self):
      return hash((self.valeur,self.couleur))


class Cartes():

  def __init__(self,l=None):
    if l == None :
      self.cartes=[]
    else : 
      self.cartes=np.copy(l.cartes)

  def __str__(self):
    return ", ".join([str(c) for c in self.cartes])
    
  def __repr__(self):
    return ", ".join([str(c) for c in self.cartes])

  def ajoute(self,c):
    self.cartes += [c]
    
  def pioche(self):
    if len(self.cartes)!=0:
      k=self.cartes[randrange(0,len(self.cartes))]
      self.cartes.remove(k)
      return k
    else:
      raise ValueError(f"pioche vide!")


class Jeu():
  def __init__(self):
    self.jeu=[]
    for v in Carte.valeurs:
      for c in Carte.couleurs:
        self.jeu+=[Carte(v,c)]

  def __str__(self):
      return ", ".join([str(c) for c in self.jeu])

  def __repr__(self):
      return ", ".join([str(c) for c in self.jeu])
    
  def __isub__(self,c):
    if isinstance(c,Carte):
      for k in self.jeu:
        if k==c:
          self.jeu.remove(k)
    else:
      raise RuntimeError("Opération non prévue") 
    return self
          
class Main():

  def __init__(self,j):
    self.jeu=j
    self.main=[]
  def __str__(self):
    return ", ".join([str(c) for c in self.main])
    
  def __repr__(self):
    return ", ".join([str(c) for c in self.main])

  def copie(self):
    return np.copy(self.main)
    
  def __isub__(self,c):
    if isinstance(c,Carre):
      for k in self.main:
        if k.valeur==c.carre:
          self.main.remove(k)      
      return self
    if isinstance(c,Quinte):
      for k in self.main:
        for i in range (len(c.quinte)):
          if k.valeur==c.quinte[i] and k.couleur==c.color:
            self.main.remove(k)
      return self  
    if isinstance(c,Main):
      for k in self.main:
        for i in c.main:
          if k==i:
            self.main.remove(k)
      return self
    else:
      raise RuntimeError("Opération non prévue")   
    
  def complete(self):
    if len(self.jeu.jeu)!=0:
      i=randrange(0,len(self.jeu.jeu))
      c=self.jeu.jeu[i]
      self.main+=[c]
      self.jeu.jeu.remove(c)
    else : 
      raise ValueError(f"Plus de carte pour compléter la main {self.main}")

class Carre():
  def __init__(self,m):
    self.m=m
    self.c=0
    self.carre=''
    self.k=0
    for carte1 in self.m.main:
      self.k+=1
      for carte2 in self.m.main:
        if carte1.valeur==carte2.valeur:
          self.c+=1
        if self.c==4:
          self.carre=carte1.valeur
          break
      self.c=0
    if self.k==len(self.m.main) and self.carre=='':
      raise RuntimeError(f"pas de carré dans {self.m.main}")
      
      
  def __str__(self):
    return f"Un carre de {self.carre}"
  def __repr__(self):
    return f"Un carre de {self.carre}"
  
class Quinte():
  def __init__(self,m):
    self.m=m
    self.quinte=''
    self.color=''
    self.coeur=[]
    self.carreau=[]
    self.pique=[]
    self.trefle=[]
    L=[self.coeur,self.carreau,self.pique,self.trefle]
    
    for carte in self.m.main:
      for i in Carte.couleurs:
        if carte.couleur==i:
          L[Carte.couleurs.index(i)]+=[carte.valeur]

    for k in L:
      k=tri(k)
    
    valeurs=", ".join([str(c) for c in Carte.valeurs])
    
    for k in L:
      for i in range(len(k)-5):
        C=", ".join([str(c) for c in k[i:i+5]])
        if C in valeurs :
          self.quinte=k[i:i+5]
          self.color=Carte.valeurs[L.index(k)]
          break
    else :
      raise RuntimeError(f"pas de quinte dans {self.m.main}")
      
  def __str__(self):
    return f"Une quinte de {self.coeur}\n,{self.carreau}\n,{self.pique},\n{self.trefle}"
  def __repr__(self):
    return f"Une quinte de {self.coeur}\n,{self.carreau}\n,{self.pique},\n{self.trefle}"

def tri(L): #méthode de tri par insertion
    for i in range(1, len(L)):
        k1 = L[i]
        k2 = i - 1

        while k2 >= 0 and Carte.valeurs.index(L[k2]) > Carte.valeurs.index(k1):
            L[k2 + 1] = L[k2] 
            k2 -= 1

        L[k2 + 1] = k1

    return L
