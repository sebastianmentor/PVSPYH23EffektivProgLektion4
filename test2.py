GLOBAL_LISTA = [1,2,3,4]


# yttre_funktion()
print(GLOBAL_LISTA)

def main():
    def yttre_funktion():
        x = 5
        GLOBAL_LISTA[0] = 6 # main() GLOBAL_LISTA
        def inre_funktion():
            print(x)
            # GLOBAL_LISTA[3] = 10 Fungerar inte
            global GLOBAL_LISTA
            GLOBAL_LISTA[3] = 10
            
            # x = 10
            
        print(x)
        inre_funktion()
        print(x)

    GLOBAL_LISTA = ['a', 'b', 'c','d']
    print(GLOBAL_LISTA, '<- i main')
    yttre_funktion()
    print(GLOBAL_LISTA, '<- i main')


if __name__ == '__main__':
    main()
    print(GLOBAL_LISTA)