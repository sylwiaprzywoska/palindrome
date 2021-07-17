word = "potop"
word2 = "dom"
checked_word_backwards = ''

def check_if_palindrome(checked_word):
  checked_word_backwards = checked_word[::-1]
  if checked_word_backwards == checked_word:
    print("Zwrócono wartość TRUE")
    return True
  else:
    print("Zwrócono wartość FALSE")
    return False
check_if_palindrome(word)
check_if_palindrome(word2)
