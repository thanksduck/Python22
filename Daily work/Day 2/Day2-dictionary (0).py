d1={'name':'sukhman','crn':'2015134','class':'d2 cse c1'}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('name'))
d1['name']='sukhmanpreet kaur'
print(d1)
d1.pop('name')
print(d1)
d1.popitem()
print(d1)
d1.clear()
print(d1)

x=('key1','key2','key3')
y=0
d=d1.fromkeys(x,y)
print(d)
d['key1']='1st key of d'
d['key2']='2nd key of d'
d['key3']='3rd key of d'
print(d)

d2=d.fromkeys(d)
print(d2)
d2['key1']='1st key of d2'
d2['key2']='2nd key of d2'
d2['key3']='3rd key of d2'
print(d2)

d3=d2.copy()
d3.update({'key1':'1st key of d3'})
d3.update({'key2':'2nd key of d3'})
d3.update({'key3':'3rd key of d3'})
print(d3)

d4=d2.setdefault('key1')
print(d4)