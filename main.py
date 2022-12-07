# Roskabotti.py
# Ohjelman pohja
# Luvian yhtenäiskoulu MOK - projektin tehtävä


#*****************************
def TulostaVirhe():
  print("Nyt en oikein ymmärtänyt.")
  print("Kokeile kierrätettävän materiaalin sanan perusmuotoa,")
  print("kuten ”tietokone”, ”sohva”, ”lasi”.")
  print("Ohjeen saat kirjoittamalla ”ohje”.")


#*****************************
def Lopeta():
  print("Kiitos kun käytit RoskaBottia!")


#*****************************
# T1: Lisää tuoteen lasi
# kierrätysohjeet
#*****************************
def TulostaLasiOhje():
  print("")
  print("")
  print("")
  print("")
  return None


#*****************************
# T2: Lisää tuoteen muovi
# kierrätysohjeet
#*****************************
def TulostaMuoviOhje():
  print("")
  print("")
  print("")
  print("")
  return None


#*****************************
# T3: Lisää tuote 3
#
# def TulostaxxxxxOhje():
#    print("")
#    return None

#*****************************
# T4: Lisää tuote 5

#*****************************
# T5: Lisää tuote 5

#*****************************
# Lisää paaohjelmaan kolme uutta if - lausetta
#
#        elif tuote == "xxxxx":
#            print("Tuote on xxxxx ....")
#            TulostaxxxxxOhje()


#*****************************
def paaohjelma():
  while True:
    tuote = input("Anna tuote: ")
    tuote = tuote.lower()  # Muuttaa kaikki kirjaimet pieneksi
    if tuote == "lopeta":
      Lopeta()
      break
    elif tuote == "lasi":
      print("Tuote on lasia....")
      TulostaLasiOhje()
    elif tuote == "muovi":
      print("Tuote on Muovi....")
      TulostaMuoviOhje()
    else:
      TulostaVirhe()


paaohjelma()
