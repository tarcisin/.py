import stats
import math

class Student:
  def __init__(self, nome, *notas):
    self.nome = ' '
    self.notas = [0, 0, 0]
    pass

  def InserirNota(self):
    self.notas[0] =  float(input("Insira o Valor da Nota 1: "))
    self.notas[1] =  float(input("Insira o Valor da Nota 2: "))
    self.notas[2] =  float(input("Insira o Valor da Nota 3: "))
  
  def InserirNome(self):
    self.nome = input("Insira o nome do estudante: ")
    return(self.nome)

  def obterNotaAlta(self):
    self.pontoMaisAlto = max(self.notas)
    return(self.pontoMaisAlto)
  
  def obterNotaMedia(self):
    self.notaMedia = math.mean(self.notas)
    return (self.notaMedia)

  def exibirDados(self):
    print("Nome: ", self.nome)
    print("Ponto 1: ", self.notas[0])
    print("Ponto 2: ", self.notas[1])
    print("Ponto 3: ", self.notas[2])
    prog = str(input("Deseja alterar alguma nota? (S/N)"))
    if(prog == "S"):
      notaDecider = int(input("Qual das notas deseja alterar? (0/1/2)"))
      if (notaDecider == 0):
        self.nota[0] = float(input("Insira o novo valor da nota: "))
      if (notaDecider == 1):
        self.nota[1] = float(input("Insira o novo valor da nota: "))
      if (notaDecider == 2):
        self.nota[2] = float(input("Insira o novo valor da nota: "))
      else:
        print("Valor inválido!")
    else:
      print("\n")
 
def __main__(nome, *notas):
  aluno1 = Student(nome, *notas)
  aluno1.InserirNome(nome)
  aluno1.InserirNota(*notas)
  aluno1.exibirDados(nome, *notas)
  
  aluno1.obterNotaAlta(*notas)
  print("A nota mais alta é ", aluno1.pontoMaisAlto)

  aluno1.obterNotaMedia(*notas)
  print("A nota média é ", aluno1.notaMedia)

__main__()
