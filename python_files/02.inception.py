Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5
5
>>> 5 + 5
10
>>> 4 * 5 - 3
17
>>> def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

	
>>> fact(5)
120
>>> fact(10000)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fact(10000)
  File "<pyshell#8>", line 5, in fact
    return n * fact(n-1)
  File "<pyshell#8>", line 5, in fact
    return n * fact(n-1)
  File "<pyshell#8>", line 5, in fact
    return n * fact(n-1)
  [Previous line repeated 1021 more times]
  File "<pyshell#8>", line 2, in fact
    if n == 0:
RecursionError: maximum recursion depth exceeded in comparison
>>> fact(99)
933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> [1,2,3]
[1, 2, 3]
>>> [[1,2], 4]
[[1, 2], 4]
>>> [[1,2,3], [3,4]]
[[1, 2, 3], [3, 4]]
>>> a = [1,2,3,3,2]
>>> a.sort()
>>> a
[1, 2, 2, 3, 3]
>>> for i in a:
	print(i ** 2)
1
4
4
9
9
>>> for i in range(10):
	print(i + 3)

	
3
4
5
6
7
8
9
10
11
12
>>> 5+5

