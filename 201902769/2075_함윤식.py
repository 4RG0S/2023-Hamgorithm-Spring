class hq:
    def __init__(self, n):
        self.queue = []
        self.size = 0
        self.limit = n

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 2
    
    def relocation(self):
        # queue[0]에 가장 작은 값이 위치하도록 한다.
        # queue[0]에 새로운 값이 들어오면, 부모 노드와 비교하여 작은 값이 부모 노드가 되도록 한다.
        child_index = self.size - 1
        while child_index > 0:
            parent_index = self.parent_index(child_index)
            if self.queue[child_index] < self.queue[parent_index]:
                self.queue[child_index], self.queue[parent_index] = self.queue[parent_index], self.queue[child_index]
                child_index = parent_index
            else:
                break

    def put(self, value):
        # 총 n개의 큰 데이터만 유지하기 위해, n개 이상의 데이터가 들어오면 가장 작은 데이터를 제거한다.
        if self.size >= self.limit:

            # value가 queue의 가장 작은 데이터보다 작을 경우, 리턴한다.
            # 이를 하지 않을 경우 큐의 원소를 재배치하는 과정에서 복잡도적인 큰 손해가 발생한다.
            if value <= self.queue[0]:
                return
            
            # value가 queue의 가장 작은 데이터보다 클 경우, queue[0]에 value를 넣고, queue[0]를 재배치한다.
            else:
                self.queue.append(value)
                self.size += 1
                self.relocation()
                self.get()
        # 큐의 원소가 n개 이하인 경우 무조건 재배치한다.
        else:
            self.queue.append(value)
            self.size += 1
            self.relocation()
        
    def get(self):
        if self.size == 0:
            return None
        else:
            value = self.queue[0]
            self.size -= 1
            self.queue[0] = self.queue[self.size]
            self.queue.pop()

            # queue[0]를 리턴하고, queue[0]에 나머지 원소중 가장 작은 값이 위치하도록 한다.
            parent_index = 0
            while parent_index < self.size:
                
                left = self.left_child_index(parent_index)
                right = self.right_child_index(parent_index)

                # 자식 노드가 둘 다 존재하는 경우
                if right <= self.size - 1:
                    target_index = left if self.queue[left] < self.queue[right] else right
                    if self.queue[parent_index] > self.queue[target_index]:
                        self.queue[parent_index], self.queue[target_index] = self.queue[target_index], self.queue[parent_index]
                        parent_index = target_index
                        continue
                # 자식 노드가 하나만 존재하는 경우
                if left <= self.size - 1:
                    if self.queue[parent_index] > self.queue[left]:
                        self.queue[parent_index], self.queue[left] = self.queue[left], self.queue[parent_index]
                        parent_index = left
                        continue
                #자식 노드가 존재하지 않는 경우
                return value


n = int(input())
heapq = hq(n)

if n == 1:
    print(input())
else:
    for _ in range(n):
        cur = list(map(int, input().split()))
        for i in cur:
            heapq.put(i)

    print(heapq.get())