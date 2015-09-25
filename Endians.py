
for i in range(int(input())):
    i = int(input())
    print ((i & (255 << 24)) >> 24 | (i & (255 << 16)) >> 8  | (i & (255 << 8)) << 8 | (i & 255) << 24 )


