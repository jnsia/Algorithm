def search(i):
    if store.get(i):
        return store[i]

    result = search(i // P) + search(i // Q)
    store[i] = result

    return result


N, P, Q = map(int, input().split())

store = dict()
store[0] = 1

search(N)
print(store[N])