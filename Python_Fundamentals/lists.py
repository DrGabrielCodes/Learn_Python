#***********LISTS******************
#lists are like containers that are used to store items.
#These items could be numbers, strings, lists, dictionaries, sets or even tuples.
#It can contain virtually anything. 
#They are created using square brackets. Items in a list are seperated by commas.

#For instance we could have a list of professions, customers, drugs, etc  
professions = ["optometry", "pharmacy", "medicine and surgery", "scientist", "Data analyst"] 

customers = ["Brad Onyeka", "Tolu Williams", "Uchenna Onyeoma", "Philips Igbinovia"]

antibiotic_drugs = ["ciprofloxacin", "gentamicin", "tobramycin", "azithromycin"]
analgesic_drugs = ["acetaminophen", "ibuprofen", "diclofenac", "ketorolac"]
antiglaucoma_drugs = ["acetazolamide", "brimonidine", "timolol", "latanoprost"]

# An example of a nested list ie a list of lists
list_of_all_medications = [
    ["ciprofloxacin", "gentamicin", "tobramycin", "azithromycin"],
    ["acetaminophen", "ibuprofen", "diclofenac", "ketorolac"],
    ["acetazolamide", "brimonidine", "timolol", "latanoprost"]
]  

#INDEXING of LISTS
# Items in a list can be assessed using indexing just like strings. starting from 0 as the first item of the list
antibiotics = list_of_all_medications[0]  
print(antibiotics)  #This prints a list of all the antibiotics in the list_of_all_medications
analgesics = list_of_all_medications[1]  
print(analgesics)  #This prints a list of all the analgesics in the list_of_all_medications



# Also items of a nested list can be index by using more than one index number  