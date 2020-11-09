## SIMPLE LINEAR SEARCH ALGORITHM ##

l=[1,2,3,4,5,7,10,25,64,89,7,8,12,45,7,96,58,6,46,123]


for i in range(len(l)):
	if l[i]==7:
		print("element found at index " + str(i))
		#break 											# for finding 1st occurance of element
	else:
		continue
else:
	print("element not found !")


#-------------------------------------------------------------------------

#another method

for i,v in enumerate(l):
	if v==64:
		print("element found at index ",i)
		break                                            # for finding 1st occurance of element
	else:
		continue

else:
	print("element not found !")


#--------------------------------------------------------------------------------------------------------------------------


## SIMPLE BINARY SEARCH ALGORITHM [For sorted lists only] ##

def binary_search(l,val):
	

	if len(l) == 0:
		return False

	else:

		mid = len(l)//2

		if val == l[mid]:
			return True

		elif val < l[mid]:
			return binary_search(l[:mid],val)	

		else:
			return binary_search(l[mid+1:],val)	

l=[100,200,300,400,500,600,700,800,900,1000]

print(binary_search(l,100))

#----------------------------------------------------------------------------------

## MODIFIED BINARY SEARCH ALGORITH [For any sorted/unsorted list]


def issoretd(list):
	l=list
	for i in range(len(l)-1):
		if l[i] <= l[i+1]:
			continue
		else:
			return False
	return True



def mod_binary_search(l,val):

	sort_ans = issoretd(l)

	if sort_ans == False:
		l.sort()
        # Or we can simply sort every list passed as arg. In that case we dont need issorted() function.	

	if len(l) == 0:
		return False

	else:

		mid = len(l)//2

		if val == l[mid]:
			return True

		elif val < l[mid]:
			return binary_search(l[:mid],val)	

		else:
			return binary_search(l[mid+1:],val)	

l1=[100,2007,300,4000,500,600,700,80,9010,1000]

print(mod_binary_search(l1,80))
