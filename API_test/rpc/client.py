import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:8080/')
client.system.listMethods()
mensagem = input("digite uma mensagem para enviar ao servidor").encode()
client.mensagem(mensagem)
print("mensagem enviada")
os.system("PAUSE")