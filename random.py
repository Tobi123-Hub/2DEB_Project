w, h = 4, 4;

irand = randrange(0, 999)
matrix = [[0 for x in range(w)] for y in range (h)]
matrix = [[4,2,0,7],[6,9,6,9],[12,33,41,68],[213,999,827,617]]
for k in range(w):
    for n in range(h):
        num = matrix[k][n]
        if (matrix[k][n] % 2) == 0:
            print(matrix[k][n])
            print(' er et partall\n')
        elif (matrix[k][n] % 2) != 0:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num, ' er et oddetall\n')
                    break
            else:
                print(num, ' er et primtall\n')

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    for row in matrix]))

