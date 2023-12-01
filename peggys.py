# Programmer: Noah
# Description: Peggy's

#Create a function to find the cost of Peggy's Pest Control
def peggys_price (level, size):
      if size < 0:
          print ("Invalid house size")
      elif level.lower () == "basic":
        answer = size * 0.05
        return (f"$ {answer:,.2f}")
      elif level.lower () == "advanced":
        answer = size * 0.10
        return (f"${answer:,.2f}")
      elif level.lower () == "complete":
        answer = size * 0.20
        return (f"${answer:,.2f}")
      else:
        print ("Invalid price level")