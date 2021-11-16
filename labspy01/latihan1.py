def main():
    print('menentukan nilai terbesar dari dua bilangan')
 
    a = int(input("masukan bilangan pertama: "))
    b = int(input("masukan bilangan kedua: "))

    if a > b:
        max = a
    else:
        max = b
  
    print('Nilai Terbesar adalah %d' % max)
 
if __name__ == '__main__':
    main()