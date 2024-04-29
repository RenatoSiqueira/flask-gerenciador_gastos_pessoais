from ..models import conta_model
from api import db

def cadastrar_conta(conta):
  conta_db = conta_model.Conta(nome=conta.nome, descricao=conta.descricao, saldo=conta.saldo)
  db.session.add(conta_db)
  db.session.commit()
  return conta_db

def listar_contas():
  return conta_model.Conta.query.all()

def buscar_conta(id):
  return conta_model.Conta.query.get(id)

def deletar_conta(conta):
  db.session.delete(conta)
  db.session.commit()

def atualizar_conta(conta, nova_conta):
  conta.nome = nova_conta.nome
  conta.descricao = nova_conta.descricao
  conta.saldo = nova_conta.saldo
  db.session.commit()
  return conta
