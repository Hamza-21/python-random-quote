import random

def quote():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 18
  rnd = random.randint(0,18)
  msr = random.randint(0,18)
  print(quotes[rnd], end="")
  print(quotes[msr], end="")


if __name__== "__main__":
  quote()
