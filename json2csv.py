import mycsv
import json
jsonString = mycsv.getdata()
jasonData = json.loads(jsonString)
headers = jasonData['headers']
data =jasonData['data']

output = ''
for headIndex, head in enumerate(headers):
    if headIndex < len(headers)-1:
        # print with comma
        output+=head+","
    else:
        # move to next line
        output+=head+"\n"
for datumIndex, datum in enumerate(data):
    if datumIndex < len(data)-1:
        #print, without quotes, with comma
        for peiceIndex, peice in enumerate(datum):
            if peiceIndex < len(datum)-1:
                #add an entry
                output+=datum[peice]+","
            elif  peiceIndex == len(datum)-1:
                #finish non-last line
                output+=datum[peice]+"\n"
    else:
        #reached last row
        for peiceIndex, peice in enumerate(datum):
            if peiceIndex < len(datum)-1:
                #add an entry
                output+=datum[peice]+","
            else:
                #finish last line
                output+=datum[peice]

print(output)