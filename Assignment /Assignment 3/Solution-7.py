eid, ename, esal = 1, 'aaa', 10000.56

def emp(eid, ename, esal):
	globals()['eid'] = eid
	globals()['ename'] = ename
	globals()['esal'] = esal


print(eid, ename, esal)


def disp():
	print(eid, ename, esal)


emp(111, 'ratan', 10000.45)
disp()
print(eid, ename, esal)


# OUTPUT
"""
1 aaa 10000.56
111 ratan 10000.45
111 ratan 10000.45"""