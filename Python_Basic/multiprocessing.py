from multiprocessing import Process

def test():
    print("this is my multi processing program..")

if __name__=='__main__':
    m=Process(target=test)
    print(" this is my  main program")
    m.start()
    m.join()