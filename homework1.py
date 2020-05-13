import string
fin=open("words.txt")
din=open("book.txt")
for line_txt in fin:
  line_txt=fin.readline()
  word_txt=line_txt.strip()
  # print(word_txt)
  for din_book in din:
    if din_book == string.punctuation:
      din.replace("string.punctuation","")
      din_book=din.readline()
      word_book=din_book.strip()
      if word_book not in word_txt:
        print(word_book)

