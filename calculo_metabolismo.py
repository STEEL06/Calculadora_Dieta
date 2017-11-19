print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print "Calculo da Taxa do Metabolismo Basal (TMB)."

lacoTMB = 0
while ( lacoTMB != 1 ):
   print""
   genero = input ("Qual o seu genero? 1-Homem ; 2-Mulher ")

   while ( genero != 1 and genero != 2 ):
      print ""
      print "Escolha um genero existente."
      print ""
      genero = input ("Qual o seu genero? 1-Homem ; 2-Mulher ")
      print ""

   peso = input ("Qual seu peso em Kg ? ")
   alturam = input ("Qual sua altura em m ? ")
   alturacm = ( alturam * 100 )
   idade = input ("Qual sua idade em anos ? ")
   BF = input ("Qual o seu percentual de gordura corporal? Digite 0 caso nao saiba. ")
   print ""

   if   genero == 1:
      print "Voce e Homem."
   elif genero == 2:
      print "Voce e Mulher."
   else:
      print ""

   print "O seu peso e", peso, "Kgs."
   print "A sua altura e", alturam, "m."
   print "A sua idade e", idade, "anos."

   if   BF == 0:
      print "O seu percentual de gordura nao e conhecido."
   else:
      print "O seu percentual de gordura e de ", BF, "%."

   print""

   if   BF == 0:
      if   genero == 1:
         TMB = (( 10 * peso ) + ( 6.25 * alturacm ) - ( 5 * idade ) + 5 )
      elif genero == 2:
         TMB = (( 10 * peso ) + ( 6.25 * alturacm ) - ( 5 * idade ) - 161 )
      else:
         print ""
   else:
      TMB = ( 370 + ( 21.6 * ( peso - ( peso * BF * 1/100 ))))

   print "A sua Taxa Metabolica Basal e", TMB, "kcal."
   print ""

   lacoTMB = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ? ")

print ""
print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print "Calculo da Ingestao Calorica Recomendada (ICR)."

lacoICR = 0
while ( lacoICR != 1 ):
   print ""
   print "Com qual item dessa tabela se assemelha sua quantidade de exercicios semanal ?"
   print ""
   print "1- Nenhum ou pouco."
   print "2- Leve, de 1 a 3 vezes por semana."
   print "3- Moderado, de 3 a 5 vezes por semana."
   print "4- Pesado, de 6 a 7 vezes por semana."
   print "5- Extremo, duas vezes ao dia."
   print ""
   QES = input ("")  # QE = Quantidade de Exercicio Semanal
   print ""

   while ( QES != 1 and QES != 2 and QES != 3 and QES != 4 and QES != 5 ):
      print ""
      print "Valor invalido, escolha novamente."
      print ""
      print "Com qual item dessa tabela se assemelha sua quantidade de exercicios semanal ?"
      print ""
      print "1- Nenhum ou pouco."
      print "2- Leve, de 1 a 3 vezes por semana."
      print "3- Moderado, de 3 a 5 vezes por semana."
      print "4- Pesado, de 5 a 7 vezes por semana."
      print "5- Extremo, mais de uma vez ao dia."
      print ""
      QES = input ("")
      print ""

   if   QES == 1:
      ICR = ( 1.2 * TMB )
      print "Voce nao faz, ou faz pouquissimo exercicio."
   elif QES == 2:
      ICR = ( 1.375 * TMB )
      print "Voce se exercita de forma leve, de 1 a 3 vezes na semana."
   elif QES == 3:
      ICR = ( 1.55 * TMB )
      print "Voce se exercita de forma moderada, de 3 a 5 vezes na semana."
   elif QES == 4:
      ICR = ( 1.725 * TMB )
      print "Voce se exercita de forma pesada, de 5 a 7 vezes na semana."
   elif QES == 5:
      ICR = ( 1.9 * TMB )
      print "Voce se exercita de forma extrema, mais de uma vez ao dia."
   else:
      print ""

   print ""
   print "sua Ingestao Calorica Recomendada e de", ICR, "kcal"
   print ""

   lacoICR = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ? ")

print ""
print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print "Calculo do balanco do Deficit ou Superavit Calorico (DSC)"

lacoDSC = 0
while ( lacoDSC != 1 ):
   print ""
   print "Escolha o tipo de dieta pretendida:"
   print "1- Hipocalorica ; 2- Normocalorica ; 3- Hipercalorica"
   print ""
   DSC = input ("")

   while ( DSC != 1 and DSC != 2 and DSC != 3 ):
      print "Escolha um valor possivel."
      print ""
      print "Escolha o tipo de dieta pretendida:"
      print "1- Hipocalorica ; 2- Normocalorica ; 3- Hipercalorica"
      print ""
      DSC = input ("") # DSC: Deficit ou Superavit Calorico / CD: Calorias Diarias

   print ""

   if   DSC == 1:
      kcalsem = input ("Quantos kilos pretende perder por semana? ")
      kcaldia = ( kcalsem * 7700 / 7 )
      CD = ( ICR - kcaldia )
      print ""
      print "Voce optou em fazer uma dieta Hipocalorica."
      print "Voce deseja perder", kcalsem, "kg por semana."
   elif DSC == 2:
      CD = ICR
      print ""
      print "Voce optou em fazer uma dieta Normocalorica."
      print "Voce deseja manter seu peso."
   elif DSC == 3:
      kcalsem = input ("Quantos kilos pretende ganhar por semana? ")
      kcaldia = ( kcalsem * 7700 / 7 )
      CD = ( ICR + kcaldia )
      print ""
      print "Voce optou em fazer uma dieta Hipercalorica."
      print "Voce deseja ganhar", kcalsem, "kg por semana."
   else:
      print ""

   print "Sua necessidade Calorica Diaria e", CD, "kcal."
   print ""

   lacoDSC = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ? ")

print ""
print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print "Calculo dos Macro-Nutrientes."

lacoPMC = 0
while ( lacoPMC != 1 ):

   #________________________Percentuais de cada Macro-Nutriente_____________________________________________________________________________________________
   print ""
   PercCarbo = input ("Qual o percentual de Carboidratos de sua dieta? 0 a 100: ")
   PercProte = input ("Qual o percentual de Proteinas de sua dieta? 0 a 100: ")
   PercLipid = input ("Qual o percentual de Lipideos de sua dieta? 0 a 100: ")

   print "------------------------------------------------------------------------------"
   print "| Voce escolheu os seguintes percentuais para dividir seus Macro-Nutrientes: |"
   print "| Carboidratos -", PercCarbo, "%.                                            |"
   print "| Proteinas    -", PercProte, "%.                                            |"
   print "| Lipideos     -", PercLipid, "%.                                            |"
   print "------------------------------------------------------------------------------"


   #_______________________________Calorias por Macro-Nutriente_____________________________________________________________________________________________
   print ""
   KcalCarbo = ( PercCarbo * 1.0/100 * CD )
   KcalProte = ( PercProte * 1.0/100 * CD )
   KcalLipid = ( PercLipid * 1.0/100 * CD )

   print "----------------------------------------------------------------------------------"
   print "| Voce devera consumir os seguintes valores em calorias de cada Macro-Nutriente: |"
   print "| Carboidratos -", KcalCarbo, "kcal.                                             |"
   print "| Proteinas    -", KcalProte, "kcal.                                             |"
   print "| Lipideos     -", KcalLipid, "kcal.                                             |"
   print "----------------------------------------------------------------------------------"


   #____________________________Peso em Gramas por Macro-Nutriente__________________________________________________________________________________________
   print ""
   GramCarbo = ( KcalCarbo * 1.0 / 4.1 )
   GramProte = ( KcalProte * 1.0 / 4.3 )
   GramLipid = ( KcalLipid * 1.0 / 9.3 )

   print "---------------------------------------------------------------------------------"
   print "| Voce devera consumir a seguinte quantidade em gramas de cada Macro-Nutriente: |"
   print "| Carboidratos -", GramCarbo, "gramas.                                          |"
   print "| Proteinas    -", GramProte, "gramas.                                          |"
   print "| Lipideos     -", GramLipid, "gramas.                                          |"
   print "---------------------------------------------------------------------------------"


   #_______Peso em Gramas de Macro-Nutrientes por kg de peso corporal_______________________________________________________________________________________
   GrCarbPkg = ( GramCarbo / peso )
   GrProtPkg = ( GramProte / peso )
   GrLipiPkg = ( GramLipid / peso )

   print "-----------------------------------------------------------------"
   print "| Sua ingestao de Macro-Nutrientes em gramas por peso em kgs e: |"
   print "| Carboidratos -", GrCarbPkg, "gr/kg de peso corporal.          |"
   print "| Proteinas    -", GrProtPkg, "gr/kg de peso corporal.          |"
   print "| Lipideos     -", GrLipiPkg, "gr/kg de peso corporal.          |"
   print "-----------------------------------------------------------------"

   lacoPMC = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ")

print ""
print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print "Divisao de Macro-Nutrientes por numero de refeicoes."

lacoDMN = 0
while ( lacoDMN != 1 ):
   print ""
   QtRfCarbo = input ("Quantas refeicoes com carboidrato voce fara ao longo do dia? ")
   QtRfProte = input ("Quantas refeicoes com proteina voce fara ao longo do dia? ")
   QtRfLipid = input ("Quantas refeicoes com lipideo voce fara ao longo do dia? ")

   GrCarbPRf = ( GramCarbo / QtRfCarbo )
   GrProtPRf = ( GramProte / QtRfProte )
   GrLipiPRf = ( GramLipid / QtRfLipid )

   print "Voce optou por fazer", QtRfCarbo, "refeicoes de Carboidrato por dia, contendo", GrCarbPRf, "gramas cada uma."
   print "Voce optou por fazer", QtRfProte, "refeicoes de Proteina por dia, contendo", GrProtPRf, "gramas cada uma."
   print "Voce optou por fazer", QtRfLipid, "refeicoes de Lipideo por dia, contendo", GrLipiPRf, "gramas cada uma."

   lacoDMN = input ("Esses dados estao corretos? 1-Sim ; 2-Nao ")



print " "
print " "
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
