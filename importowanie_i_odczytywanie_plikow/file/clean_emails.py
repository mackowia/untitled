import sys
adresy = set()

with open (sys.argv[1]) as f:
    for line in f:
        adres = line.strip()    #strip() usuwa spacje z przodu i z tylu adresu e-mail
        adres = adres.lower()

        #if adres.count("@") != 1:      #to samo co kod nizej
            #continue
        #adresy.add(adres)
        if adres.count("@") == 1:
            adresy.add(adres)

with open (sys.argv[2], "w") as f:
    for adres in sorted(adresy):
        f.write(adres + "\n")

if __name__ == "__main__":
    main()
