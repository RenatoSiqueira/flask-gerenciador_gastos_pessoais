class Usuario():
  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, email):
    self.__email = email

  @property
  def senha(self):
    return self.__saldo
  
  @senha.setter
  def senha(self, senha):
    self.__saldo = senha