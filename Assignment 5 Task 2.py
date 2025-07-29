#Program to demonstrate slicing of list
list1=[1,2,3,4,5,6,7,8,9,10]
print(f'Original List: {list1}')
extract=list1[0:5:1]
print(f'\nExtracted First Five Elements:{extract}')
extract.reverse()
print(f'\nReversed Extracted Elements: {extract}')