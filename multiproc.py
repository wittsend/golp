import multiprocessing

class ValObj:
    def __init__(self, val1:str, val2:bool):
        self.val1 = val1
        self.val2 = val2

    def __str__(self):
        return f'Val1:{self.val1}, Val2:{self.val2}'

def do_some_work(val, val2):
    print('Doing some work in thread')
    print(f'echo: {val}')
    print('Doing some work in thread')
    print(f'echo: {val2}')

    return

if __name__ =='__main__':
    val = ValObj('text', True)
    val2 = ValObj('text2', False)
    t= multiprocessing.Process(target=do_some_work, args=(val,val2,))
    #t2= multiprocessing.Process(target=do_some_work, args=(val2,))
    t.start()
    #t2.start()
    t.join()
    #t2.join()