class G():
  def __init__(self):
    cnt = 0
    def isPrime(n):
      if n <= 1:
        return False
      if n <= 3:
        return True
      if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
      i, r = 5, int(n ** 0.5)
      while i <= r:
        if n % i == 0: return False
        if n % (i + 2) == 0: return False
        i += 6
      return True 

    for i in range(1000000000, 1000210101):
      if isPrime(i): 
        print('  [+]', i)
        cnt += 1
        if cnt >= 9: break

class R():
  def __init__(self):
    with open('primes.txt') as primes:
      for i in primes.read().split('\n'): print('  [+]', i)

if __name__ == '__main__':
  print('[+] [R]ead from file ')
  print('[+] [G]enerate')
  req = input('[+] Your choice: ')

  if req.upper() == 'R': R()
  elif req.upper() == 'G': G()
  else: 
    print('[-] Exiting')
    exit()
