print('Spelling List Program')
filename = ''
def create():
  filename = input('What filename do you want: ')
  filename = filename + ".txt"
  print(filename)
  c = open(filename,"w")
  c.close()
  return filename

def fopen():
  filename = input('What filename do you want: ')
  filename = filename + ".txt"
  print(filename)
  c = open(filename,"r")
  c.close()
  return filename

def add():
  f = open(filename, 'r')
  complete = f.read()
  f.close()
  print(complete)
  ls = complete.split()
  print(ls)
  word = input('Enter a word: ')
  if word in ls:
    print(word + ' is already in the file.')
  else:
    file = open(filename,"a")
    file.write(word + '\n')
    file.close()

def delete():
  f = open(filename, 'r')
  complete = f.read()
  f.close()
  print(complete)
  ls = complete.split()
  print(ls)
  word = input('Which word would you like to delete? ')
  ls.remove(word)
  print(ls)
  f = open(filename,"w")
  for item in ls:
    f.write(item + '\n')
  f.close()

def sort():
  f = open(filename, 'r')
  complete = f.read()
  f.close()
  print(complete)
  ls = complete.split()
  print(ls)
  ls.sort()
  print(ls)
  f = open(filename,"w")
  for item in ls:
    f.write(item + '\n')
  f.close()

def show():
  f = open(filename,"r")
  print(f.read())
  f.close()



while(True):
  try:
    print('Press C to create a new list: ')
    print('Press O to open an existing list: ')
    print("Press A to add a word: ")
    print('Press B to sort the words alphabetically')
    print("Press S to show all words: ")
    print("Press D to delete a word: ")
    print("Press E to exit: ")
    task = input()
    if task.upper() == 'C':
      filename = create()
    if task.upper() == 'O':
      filename = fopen()
    if task.upper() == 'A':
      add()
    if task.upper() == 'B':
      sort()
    if task.upper() == 'S':
      show()
    if task.upper() == 'D':
      delete()
    if task.upper() == 'E':
      break
  except:
    print("That is not a choice, try again!")
print('Your list has been saved.')
