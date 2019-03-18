from  updateitems import *


def file_reader(file):
    """This method read a file and print the content"""
    with open(file,'r') as f:
        data = f.read()

        for line in data.rsplit('\n'):
            column = line.split(' ')
            print('le article {}, a {} items et le prix est {}'.format(
                column[0],column[1],column[2]))
    f.close()



def file_reader_transformation(file,qtyv):
    """This method read a file and print the content"""
    with open(file,'r') as f:
        data = f.read()

        for line in data.rsplit('\n'):
            column = line.split(' ')
            """Calculating new price based on product qty"""
            price = discount(int(column[1]),float(column[2]),int(qtyv))
            """Description in capital letters"""
            des = upper_case(column[0])
            print('le article {}, a {} items et le prix est {}'.format(
                des,column[1],price))
    f.close()

if __name__ == '__main__':
    file_reader('article.csv')
    qtyv = input("Apres quelle qte de produit aimeraiez vous fair une rebait?")
    file_reader_transformation('article.csv',qtyv)