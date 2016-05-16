def binSea(a,key,s,e):
	if(e>=s):
		mid=s+(e-s)/2
		if(a[mid]==key):
			return mid
		elif(a[mid]>key):
			return binSear(a,key,s,mid-1)
		else:
			return binSear(a,key,mid+1,e)
	else:
		return -1

n=input("enter the number of elements")
print n