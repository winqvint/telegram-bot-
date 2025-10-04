class Queue:
    def __init__(self, items = []):
        self.items = items
    def enqueue(self,order_id):
        self.items.append(order_id)
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def dequeue(self):
        return self.items.pop(0)
    def show_queue(self):
        print(' '.join(map(str,self.items)))
# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()

# 3