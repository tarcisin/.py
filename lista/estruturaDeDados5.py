import tabulate 

print("Plano de Crédito: TidBit Computer Store")
precoCompra = float(input("Insira o preço de compra: "))

pagInicial = precoCompra * 0.10
juroAnual = 0.12
pagMensal = (precoCompra - pagInicial) * 0.05
saldoAtual = precoCompra - pagInicial
mes = 1

print("Pagamento inicial: ", pagInicial)
print('{:<18s} {:<18s} {:<18s} {:<18s} {:<18s} {:<18s}'.format ('Mês', 'Saldo Devido', 'Juros-Mês', 'Valor-Principal', 'Valor Total', 'Saldo Rem.'))

while saldoAtual > 0:
  if(pagMensal > saldoAtual):
    valPrinc = saldoAtual
    pag = saldoAtual
    saldoRem = 0
  else:
    juroMes = saldoAtual * (juroAnual / 12)
    valPrinc = pagMensal - juroMes
    pag = pagMensal + juroMes
    saldoRem = saldoAtual - valPrinc
  print('{:<18d} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f}'.format(mes, saldoAtual, juroMes, valPrinc, pag, saldoRem))
  saldoAtual = saldoRem
  mes += 1