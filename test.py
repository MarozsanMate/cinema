import sys
from model import Filmek,Sorozatok
if __name__ == '__main__':
    try:
        if (len(sys.argv) < 2): raise ValueError
        n = int(sys.argv[1])
        if not sys.argv[1].isnumeric():
            raise ValueError
        if(n <= 0):
            raise ValueError
    except Exception as exp:
        print(exp)
    nk = int(sys.argv[1])
    film = []
    for _ in range(nk):
        c = input().split(';')
        kh = c[2] == 'True'
        if (len(c)==3):
            film.append(Filmek(c[0],int(c[1]), kh))
        elif(len(c)==4):
            film.append(Sorozatok(c[0],int(c[3]),kh))
        raise ValueError
    film.sort()
    for f in film:
        print(f)