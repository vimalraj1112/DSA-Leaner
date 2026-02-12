def pat16():
    n=5
    v=65

    for i in range(n):
        for j in range(i+1):
            x=chr(v)
            print(x,end=" ")

        print()
        v=v+1

pat16()            