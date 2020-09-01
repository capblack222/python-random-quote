import random as r

def original():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd=r.randint(0,len(quotes)-1)
  print(quotes[rnd])

if __name__== "__main__":
  original()
