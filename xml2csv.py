import untangle
import xmltodict
import mycsv
# get data

# xml = untangle.parse(data_string)
xml = untangle.parse(mycsv.getdata())



csv_string = xml.file.headers.cdata+"\n"
# replace _ in headers with spaces
csv_string = csv_string.replace('_',' ')

for recordIndex, record in enumerate(xml.file.data.record):
    for childIndex, child in enumerate(record.children):
        if childIndex < len(xml.file.data.children[recordIndex].children)-1 and recordIndex < len(xml.file.data.children):
            #continue row
            csv_string += record.children[childIndex].cdata+ ","
        elif childIndex == len(xml.file.data.children[recordIndex].children)-1 and recordIndex < len(xml.file.data.children)-1:
            #finish row
            csv_string += record.children[childIndex].cdata + "\n"
        else:
            #finish file
            csv_string += record.children[childIndex].cdata


print(csv_string)