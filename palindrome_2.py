zdanie = "Kobyła ma mały bok"
def check_if_palindrome(zdanie):
  zdanie_bez_znakow = ''
  zdanie_male_litery = zdanie.lower()
  items = zdanie_male_litery.split(" ")
  for item in items:
    zdanie_bez_znakow = zdanie_bez_znakow + item
  zdanie_backwards = zdanie_bez_znakow[::-1]
  if zdanie_backwards == zdanie_bez_znakow:
    return True
  else:
    return False
check_if_palindrome(zdanie)
