not1 = float(input('Primeira nota: '))
not2 = float(input('Segunda nota: '))
media = (not1 + not2) / 2
if media < 5:
    print('Infelizmente você foi reprovado, com uma média de {:.1f} pontos. Estude mais no próximo ano!'.format(media))
elif media == 5 or 5 < media < 6.9 or media == 6.9:
    print('Você ficará de recuperação! Sua média de {:.1f} não alcançou os 7 pontos necessários para passar de ano!'.format(media))
else:
    print('Parabéns, você passou de ano com uma média de {:.1f} pontos!!'.format(media))
