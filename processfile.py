import os

transfer=0
total=os.path.getsize('/home/tarena/xbh/2333333.jpg')
size=total
fpid=os.fork()
try:
    f1=open('2333333.jpg','rb')
    f2=open('666666.jpg','wb')
    if fpid<0:
        print('create process failed')
    elif fpid==0:
        if total%2==1:
            transfer=f1.read(1)
            f2.write(transfer)
            size=total-1
            transfer=f1.read(size//2)
            f2.write(transfer)
            size=size//2
        transfer=f1.read(total//2)
        f2.write(transfer)
        size=total//2
        os._exit(0)
    else:
        os.wait()
        transfer=f1.read(size)
        f2.write(transfer)
        f1.close()
        f2.close()
except OSError:
    print('打开文件失败')

