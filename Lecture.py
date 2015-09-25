for i in range(int(input())):
    i = input()
    print (''.join(sorted([i[j:j+2] for j in range(0, len(i), 2)])))
