import numpy as np

def main():
    input = np.array(list(".#...####"), dtype=np.character).reshape(3,3)
    print(input)

if __name__ == '__main__':
    main()