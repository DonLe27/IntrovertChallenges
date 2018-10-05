import pickle

def Load():
    with open('emailAddresses', 'rb') as f:
        while True:
            try:
                a = pickle.load(f)
            except EOFError:
                break
            else:
                print(a)

Load()