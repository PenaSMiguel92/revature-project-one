# import mysql.connector
import requests
import random

service_domain = 'https://rxnav.nlm.nih.gov'
api_getDisplayTerms = '/REST/Prescribe/displaynames.json'
result = requests.get(service_domain + api_getDisplayTerms)
print(result.status_code)
display_terms: dict = result.json()
result.close()
term_list = display_terms.get('displayTermsList').get('term')

medications = [ term for term in term_list if len(term) < 255]

limited_medications = []

for _ in range(100):
    index = random.randint(0, len(medications))
    first_term = medications[index].split(' / ')[0]
    if first_term not in limited_medications:
        limited_medications.append(first_term)
    
medications_ordered = [[term, "{:.2f}".format(5.0 + (random.random() * 50.0))] for term in limited_medications]

insert_query = 'INSERT INTO medications (medicationID, medicationName, medicationCost) VALUES \n'

for index, med_sublist in enumerate(medications_ordered):
    if index == len(medications_ordered) - 1:
        insert_query += f'(DEFAULT, \'{med_sublist[0]}\', {med_sublist[1]});\n'
        continue
    insert_query += f'(DEFAULT, \'{med_sublist[0]}\', {med_sublist[1]}),\n'

print(insert_query)
