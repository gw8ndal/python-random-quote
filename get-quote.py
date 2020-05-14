import random as rng
def pizdec():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = rng.randint(0, last)
  rnd2 = rng.randint(0, last)
  print(quotes[rnd], quotes[rnd2])

if __name__== "__main__":
  pizdec()
