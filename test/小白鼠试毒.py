# 有1000个瓶子其中999瓶是水,1瓶是毒药,
# 现有10只小白和无限多的干净试管
# 你怎么找出那瓶毒药

if __name__ == '__main__':
    x = input("输入毒药编号:")
    n = int(1000)
    init = 1
    guess = 0
    id=[]
    for i in range(1,11):
        id.append(i)

    for i in range(0, 10):
        n = int(n/2)
        print("把编号%d到%d号药混合为一瓶给小白鼠%d,把%d号与%d号药混合为另一瓶给小白鼠%d"%(init,(init + n - 1),(id[0]),(init - 1 + n + 1),(init - 1 + 2 * n),(id[1])))
        if init <= int(x) <= init + n - 1:
            last=init + n - 1
            init = int(init)
            print('小白鼠%d挂了'%(id[0]))
            if n==1:
                guess=init
                break
            del id[0]

        else:
            last=init - 1 + 2 * n
            init =int (init - 1 + n + 1)
            print('小白鼠%d挂了'%id[1])
            if n==1:
                guess=init
                break
            del id[1]

        if n % 2 != 0:
            if int(last)==int(x):
                guess = last
                print("把编号%d号药给小白鼠%d,小白鼠%d挂了"%(guess,id[0],id[0]))
                break
            n = n - 1
            if n <= 1:
                guess = init
                print("把编号%d号药给小白鼠%d,小白鼠%d挂了"%(guess,id[0],id[0]))
                break

    print("药品号为:" + str(guess))
