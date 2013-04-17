def save(data, filename, maxValue=2**16-1):
    width = len(data)
    hight = len(data[0])

    outFile = open(filename, 'w')
    outFile.write('P3\n{hight} {width}\n{max}\n'.format(
                      width=width,
                      hight=hight,
                      max=maxValue)
                 )

    for i in data:
        for j in i:
            outFile.write('{}\n{}\n{}\n'.format(*j))
