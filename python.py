class Library:
    #constructor yapıcı metod
    def _init_(self):
        pass
    def listbooks(self):
        with open("books.txt","a+") as file:
            file.seek(0)
            content=file.read().splitlines()
            print(content)
        

    def addbook(self):
        booktitle=input("Kitap adini yaziniz:")
        bookauthor=input("Yazarini yaziniz:")
        releaseyear=input("Cikis yilini yaziniz:")
        numpages=input("Sayfa sayisini yaziniz:")
        bookinfo=f"{booktitle},{bookauthor},{releaseyear},{numpages}\n"
        with open("books.txt","a+")as file:
            file.write(bookinfo)

    def removebook(self, title):
        found = False
        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            for line in lines:
                if title.lower() not in line.lower():
                    file.write(line)
                else:
                    found = True

        if not found:
            print("Silme işlemi için uygun kitap bulunamadı.")



lib=Library()
secim=1
while(1):
    print("MENU")
    print("1-List Books \n2-Add Book \n3-Remove Book\n4-Exit")
    secim=int(input("Ne yapmak istediginizi seciniz:"))
    if(secim==1):
        lib.listbooks()
    elif(secim==2):
        lib.addbook()
    elif(secim==3):
        title = input("Kitap İsmi Giriniz : ")
        lib.removebook(title)
    elif(secim==4):
        print("Cikis Yapiliyor...")
        break
    else:
        print("Lutfen gecerli bir secim yapiniz.")