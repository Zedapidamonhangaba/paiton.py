def cria_conta(numero,titular,saldo,limite):
    conta={"numero":numero,"titular":titular,"saldo":saldo,"limite":limite
}
    return conta
def saldo(conta):
        print("contanumero:{}".format(conta["numero"]))
        print("titular:"+ conta["titular"])
        print("saldo:{}".format(conta["saldo"]))

def deposito(conta,valor):
    conta["saldo"]+=valor

conta00 = cria_conta(1234,"Eduardo", 50.0, 100.0)
conta01 = cria_conta(4321,"Rodolfo", 50.0, 100.0)
saldo(conta00)
saldo(conta01)
