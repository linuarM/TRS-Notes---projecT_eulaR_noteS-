def result(q,number1,number2):

  for num in range(q):

    if num % number1 == 0 and num % number2 == 0:
      print(str(num) + " ", end = "")
    else:
      pass

if __name__ == "__main__":
  q = 1000
  number1=3
  number2=5

  
