print(5-4.935) 

b=0.1+0.2+0.3
if b==0.6:
    print('b je 0.6')
else:
    print('b nije 0.6')    

#  a) 5.0-4.935 ocekujemo razliku od 0.065
# računalni rezultat ce bit aproksimacija
# Koristenje float tipa podataka u Pythonu moze uzrokovati neke probleme s tocnoscu, pogotovo ako se vrse operacije s velikim brojevima
#rezultat nije 0.065 jer  računalni zapis decimalnih brojeva koristi binarni sustav, što može uzrokovati zaokruživanje i gubitak preciznosti.

#b) #nije jednako 0.6.jer decimalni brojevi koji se koriste u računalima nemaju točnu vrijednost u binarnom zapisu i to dovodi do zaokruživanja i gubitka preciznosti