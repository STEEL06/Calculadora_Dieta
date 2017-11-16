print ""


print "Calculo do TMB (Taxa do Metabolismo Basal)"

lacoTMB = 0

while ( lacoTMB <> 1 ):

   print""

   genero = input ("Qual seu genero? 1-Homen ; 2-Mulher ")

   while (genero <> ( 1 or 2 )):
      print ""
      print "escolha um genero existente"
      genero = input ("Qual o seu genero? 1-Homen ; 2-Mulher ")
      print ""

   peso = input ("Qual seu peso em Kg ? ")
   alturam = input ("Qual sua altura em ms ? ")
   alturacm = ( alturam * 100 )
   idade = input ("Qual sua idade em anos ? ")
   BF = input ("Qual o seu percentual de gordura corporal? Digite 0 caso nao saiba? ")

   print ""

   if   genero == 1:
      print "Voce e Homem"
   elif genero == 2:
      print "Voce e Mulher"
   else:
      print ""

   print "o seu peso e", peso, "kgs"
   print "a sua altura e", alturam, "ms"
   print "a sua idade e", idade, "anos"
   if   BF == 0:
      print "o seu percentual de gordura nao e conhecido"
   else:
      print "o seu percentual de gordura e de ", BF, "%"

   print""

   lacoTMB = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ? ")


if   BF == 0:
   if   genero == 1:
      TMB = ((10 * peso) + (6.25 * alturacm) - (5 * idade) + 5  )
   elif genero == 2:
      TMB = ((10 * peso) + (6.25 * alturacm) - (5 * idade) - 161)
   else:
      print ""
else:
   TMB = (370 + ( 21.6 * ( peso - (peso * BF * 1/100 ))))



# Calculo do ICR (Ingestao Calorica Recomendada)

print " "
print "Com qual item dessa tabela se assemelha sua quantidade de exercicios semanal ?"
print " "
print "1- Nenhum ou pouco"
print "2- Leve, de 1 a 3 vezes por semana"
print "3- Moderado, de 3 a 5 vezes por semana"
print "4- Pesado, de 6 a 7 vezes por semana"
print "5- Extremo, duas vezes ao dia"
print " "

QES = input ("")  # QE = Quantidade de Exercicio Semanal

if   QES == 1:
       ICR = (1.2   * TMB)
elif QES == 2:
       ICR = (1.375 * TMB)
elif QES == 3:
       ICR = (1.55  * TMB)
elif QES == 4:
       ICR = (1.725 * TMB)
elif QES == 5:
       ICR = (1.9   * TMB)
else:
       print "Escolha um valor da tabela"



# Calculo do Deficit ou Superavit calorico (DSC)

print " "
print "Escolha o tipo de dieta pretendida:"
print "1- Hipocalorica ; 2- Normocalorica ; 3- Hipercalorica"
print ""

DSC = input ("") # DSC: Deficit ou Superavit Calorico / CD: Calorias Diarias

print ""

if   DSC == 1:
       kcalsem = input ("Quantos kilos pretende perder por semana? ")
       kcaldia = ( kcalsem * 7700 / 7 )
       CD = (ICR - kcaldia)
elif DSC == 2:
       CD = ICR
elif DSC == 3:
       kcalsem = input ("Quantos kilos pretende ganhar por semana? ")
       kcaldia = ( kcalsem * 7700 / 7 )
       CD = (ICR + kcaldia)
else:
       print "Escolha um numero valido"



# Calculo dos Macro-Nutrientes

print " "

PercCarbo = input ("Qual o percentual de Carboidratos de sua dieta? 0 a 100: ")
PercProte = input ("Qual o percentual de Proteinas de sua dieta? 0 a 100: ")
PercLipid = input ("Qual o percentual de Lipideos de sua dieta? 0 a 100: ")
                                                                                     # Percentuais de cada Macro-Nutriente
KcalCarbo = ( PercCarbo * 1.0/100 * CD )
KcalProte = ( PercProte * 1.0/100 * CD )
KcalLipid = ( PercLipid * 1.0/100 * CD )
                                                                                     # Calorias de cada Macro-Nutriente
GramCarbo = ( KcalCarbo * 1.0/4 )
GramProte = ( KcalProte * 1.0/4 )
GramLipid = ( KcalLipid * 1.0/9 )
                                                                                     # Peso em Gramas de cada Macro-Nutriente
GrCarbPkg = ( GramCarbo / peso )
GrProtPkg = ( GramProte / peso )
GrLipiPkg = ( GramLipid / peso )
                                                                                     # Peso em Gramas de Macro-Nutrientes por kg de peso corporal



# Divisao de Macro-Nutrientes por numero de refeicoes

print " "
QtRfCarbo = input ("Quantas refeicoes com carboidrato voce fara ao longo do dia? ")
QtRfProte = input ("Quantas refeicoes com proteina voce fara ao longo do dia? ")
QtRfLipid = input ("Quantas refeicoes com lipideos voce fara ao longo do dia? ")

GrCarbPRf = ( GramCarbo / QtRfCarbo )
GrProtPRf = ( GramProte / QtRfProte )
GrLipiPRf = ( GramLipid / QtRfLipid )
                                                                                      # Quantidade de Macro-Nutrientes em Grama por refeicao diaria




print " "
print "genero: ", genero, " ; peso: ", peso, " ; altura: ", alturam, " ; idade: ", idade
print "QES: ", QES, " ; TMB: ", TMB, " ; ICR: ", ICR
print "DSC: ", DSC, " ; CD: ", CD
print "PercCarbo, PercProte, PercLipid: ", PercCarbo, " , ", PercProte, " , ", PercLipid, " . "
print "KcalCarbo, KcalProte, KcalLipid: ", KcalCarbo, " , ", KcalProte, " , ", KcalLipid, " . "
print "GramCarbo, GramProte, GramLipid: ", GramCarbo, " , ", GramProte, " , ", GramLipid, " . "
print "GrCarbPkg, GrProtPkg, GrLipiPkg: ", GrCarbPkg, " , ", GrProtPkg, " , ", GrLipiPkg, " . "
print "QtRfCarbo, QtRfProte, QtRfLipid: ", QtRfCarbo, " , ", QtRfProte, " , ", QtRfLipid, " . "
print "GrCarbPRf, GrProtPRf, GrLipiPRf: ", GrCarbPRf, " , ", GrProtPRf, " , ", GrLipiPRf, " . "
