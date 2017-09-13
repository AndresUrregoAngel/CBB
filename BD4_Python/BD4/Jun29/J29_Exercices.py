import csv
# _*_coding:utf-8_*_


registre = list()
#f = open("sortie.txt","w",newline='')
#ecrire = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

for ligne in open("heures.txt"):
    res=ligne.split()
    moyenne = float(res[2])+float(res[3])+float(res[4])+float(res[5])+float(res[6])

    #ecrire.writerow((res[1], int(res[0]), moyenne, moyenne / 5.0))

    registre.append("{},{},{},{}\n".format(res[1],res[0],moyenne,moyenne/5.0))
    print("{} code:{}, total hours:{},moyenne:{}".format(
                      res[1],res[0],moyenne,moyenne/5.0))



#obtenir objet writer
f = open("sortie.txt","w")
for ligne in registre:
       f.write(ligne)

f.close()