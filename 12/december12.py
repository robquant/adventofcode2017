def main():
    input = open("december12_input.txt").readlines()
    mappings = {}
    for line in input:
        items = line.split(' ')
        start = int(items[0])
        targets = [int(item.rstrip(',')) for item in items[2:]]
        mappings[start] = targets
    print(mappings)

if __name__ == '__main__':
    main()