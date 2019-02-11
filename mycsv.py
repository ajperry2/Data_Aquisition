import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):

    lines = data.split('\n')
    headers = lines[0].split(',')
    dataLines=lines[1:]
    data = dataLines
    for lineInd, line in enumerate(dataLines):
        data[lineInd] = line.split(',')
    return headers, data
