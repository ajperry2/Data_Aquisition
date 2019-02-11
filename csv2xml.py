import mycsv
from jinja2 import Environment, PackageLoader, select_autoescape


#get data
header, data = mycsv.readcsv(mycsv.getdata())


#write HTML table
#get templates from app
environ = Environment(
    loader = PackageLoader('csv2html', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

#fix headers as spaces are not allowed

#get template from available templates
template = environ.get_template('testXML.xml')

print(template.render(header=header,data=data))