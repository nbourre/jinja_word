from docxtpl import DocxTemplate
import jinja2
from datetime import datetime

# Template Docx
doc = DocxTemplate(r'D:\_data\projets\office\jinja_word\src_test.docx')

# Création d'un filtre personnalisé pour convertir les dates
def datetimeformat(value, format="%H:%M %d-%m-%y"):
    # Convert the value to a datetime object
    if isinstance(value, str):
        value = datetime.strptime(value, "%Y-%m-%d")
        
    return value.strftime(format)

jinja2.filters.FILTERS['datetimeformat'] = datetimeformat

# Nom des champs
context = {'wife_name' : "Véronique Larue",
           'wife_address' : "rue Des Orioles",
           'wife_revenue' : 123456.434,
           'husband_name' : "Frédéric Bernier",
           'husband_address' : "rue des Corneilles",
           'husband_revenue' : 123456.437,
           'marriage_date' : "2012-07-23",           
           }

doc.render (context)

# Sauvegarde du résultat dans un document 
doc.save (r'D:\_data\projets\office\jinja_word\output.docx')
