def dict_grades(some_dict):
    approved=[]
    
    for students in some_dict:
        aux=0
        results=some_dict.get(students)
        for grades in results:
            if grades>=78:
                aux+=1
            if aux == len(results):
                approved.append(students)
    return approved
                        
dicctionary={'Hectar': [80, 50, 0], 'John': [70, 80, 85], 'Undertaker': [90, 92, 93], 'Priest': [75, 78, 83], 'Henry': [80, 85.2, 88]}
print(dict_grades(dicctionary))
