
def main():
    i=[]
    def g():
        global i
        i=[1 ,2, 3, 4 ]
    g()
    print(i)
main()
