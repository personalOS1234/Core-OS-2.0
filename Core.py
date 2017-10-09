import threading
from multiprocessing import Queue 



class Core:
    def __init__(self):
        self.threads = []
    
    def add_process(self, function_called_object, process_priority, process_name, thread_name = None):
        if not thread_name:
            thread_name = function_called_object.__name__
        process_object = {
            'name': thread_name,
            'priority' : process_priority,
            'thread' : threading.Thread(target=function_called_object())
        }
        process_object['thread'].start()
        self.threads.append(process_object)

    def sort_by_prioity(self):
        self.threads.sort()

    def get_threads_names(self):
        thread_names=[]
        for i in self.threads:
            thread_names.append(i['name'])
        return thread_names




def func():
    for i in range(10):
        print(i)


def func2():
    for i in range(10, 20):
        print(i)

def func3(result):
    result = 'lol'

obj = Core()
obj.add_process(function_called_object = func, process_priority = 1, process_name = 'test', thread_name='test name')
print(obj.threads)
obj.add_process(func2, process_priority = 3, process_name = 'test2')
obj.add_process(func2, process_priority = 2, process_name = 'test3')
print(obj.threads)
print(obj.get_threads_names())
