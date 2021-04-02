from collections import deque

def enqueue(data):
    try:
        return data.popleft()
    except IndexError as e:
        return None

def total(data):
    return len(data)
