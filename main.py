# Dict items are key value pairs enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict keys are unique, cannot have duplicates
# Elements can be of different data types

'''
Dict Attributes
'''
# print(dir(dict))
# print(help(dict.pop))

'''
Creating Python Dictionary
'''

# dict_example= {}
# dict_example= {'name':'Kingsley', 'age':37}
# dict_example= dict([('1', 'car'), (2, 'bicycle', )])
# print(dict_example)

'''
Access Dictionary Values
'''
# student={'name':'Kingsley', 'age':37}

# # print(student['age'])
# # print(student.get('name'))
# # print(student.keys())
# # print(student.values())

# students=[{'name':'Kingsley', 'age':37}, {'name':'Lisa', 'age':24}]
# #print(students[1]['name'])
# for i in range (len(students)):
#   print(students[i]['age'])

'''
Changing Dictionary elements
'''
# student={'name':'Kingsley', 'age':37}
# student['age'] = 35
# print(student)

#===================
# student={'name':'Kingsley', 'age':37}
# student.update({'name':'Jennifer', 'age': '30'})
# print(student)

#==================

# student={'name':'Kingsley', 'age':37}
# student.setdefault('name','Steve')
# student.setdefault('Subject','English')
# print(student)

'''
Remove Element From Dictionary
'''

# student={'name':'Kingsley', 'age':37}
# student.pop('name')
# print(student)

#==================

# student={'name':'Kingsley', 'age':37}
# student.popitem()
# print(student)

#==================

# student={'name':'Kingsley', 'age':37}
# student.clear()
# print(student)

#==================

# student={'name':'Kingsley', 'age':37}
# del student
# print(student)

'''
Dictionary Membership Test
'''
student={'name':'Kingsley', 'age':37}

print('age' not in student)


