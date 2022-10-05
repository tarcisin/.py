from msilib.schema import Class


class Urna:

  def __init__(self):
    self.votosA = 0
    self.votosB = 0
  
  def __setItem__(self, cand, value):
    if cand == "A":
      self.votosA = value
    
    if cand == "B":
      self.votosB = value

  def addA(self, value):
    self.votosA += value
    
  def addB(self, value):
    self.votosB += value

  def fraudAddA(self, value): # Retira votos do candidato A e adiciona ao candidato B, assim que a quantidade de votos de A supera a de B
    self.votosA += value
    if self.votosA > self.votosB:
      dif = self.votosA - self.votosB
      self.votosA -= dif
      self.votosB += dif
  
  def fraudAddB(self, value):
    self.votosB += value
    if self.votosB > self.votosA:
      dif = self.votosB - self.votosA
      self.votosB -= dif
      self.votosA += dif
