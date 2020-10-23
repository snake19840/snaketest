if __name__ == '__main__':
    d=1000
    id=[]
    for i in range(0,10):
        if d%2==1:
            d=(d-1)/2
            id.append(d)
        else:

            d=d/2
            id.append(d)
    print(id)
    print(11)


