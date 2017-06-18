"""
A bit of recursion.

@author: Tarek Samaali

"""

### Calculating the sum of a list
def sum_recur0(list):
  if len(list)==1:return list
  return list[-1]+sum(list[1:-1])+list[0]

def sum_recur1(list):
  if len(list)==1:return list
  return list[-1]+sum(list[:-1])

### Sorting a list ( Selection Sort )
def tri_min(list):
  if len(list)==1: return list
  min=0
  for i in range(len(list)):
    if list[i]<list[min]:
      list[i],list[min]=list[min],list[i]
  return [list[min]]+tri_min(list[1:])

### Sorting a list ( Another variant of Selection Sort )
def tri_max(list):
  if len(list)==1: return list
  max=0
  for i in range(len(list)):
    if list[i]>list[max]:
      list[i],list[max]=list[max],list[i]
  return tri_max(list[1:])+[list[max]]


#### The minimum of a list
def minim(L):
   if len(L)==1 : return L[0]
   if L[0] <L[1] : L.pop(1)
   else : L.pop(0)
   return minim(L)


#### The maximum of a list
def maxim(L):
  if len(L)==1: return L[0]
  if L[0]>L[1]: L.pop(1)
  else : L.pop(0)
  return maxim(L)


#### Sum of two integers
def add(a,b):
  if b==0: return a
  return add(a+1,b-1)

#### Greatest common divisor
def pgcd(a,b):
  if a==0: return b
  if b==0: return a
  if a>b: return pgcd(a-b,b)
  else : return pgcd(b-a,a)


#### N°th Fibonacci term
def fibonacci0(n):
  if n==0: return 1
  if n==1: return 1

  return fibonacci0(n-1)+fibonacci0(n-2)


#### N°th Fibonacci term ( efficient implementation)
def fibonacci_efficient(n):
  if n==0:
    return (0,1)
  elif n==1:
    return (1,1)
  else:
    (a,b)=fibonacci_efficient(n-1)
    a,b=b,a+b
    return a,b

def fib(n):
  return fibonacci_efficace(n)[1]

##### multiplying two integers
def multiply(a,b):
  if b==0: return 0
  # if b==1: return a
  # if b==2 return 2*a
  # if b==3: return 3*a
  # -----
  return a+multiply(a,b-1)


#### Reversing a string
def reverse(string):
  if len(string)==1:
    return string
  else:
    return string[-1] + reverse(string[:-1])



#### Length of a string
def length(string):
  if len(string)==1 : return 1
  return 1+length(string[1:])


#### Occurrence of a caracter in a string
def occur(carac,string):

    # The occurence of a caracter within a given string
    if len(string)==0 : return 0
    if carac==string[0]:
      return 1+occur(carac,string[1:])
    else :
      return occur(carac,string[1:])


##### Position of a caracter within a string
def global_pos(carac,string):

    def occur_position(carac,string):
        if not string: return -1
        return 1+occur_position(carac,string[:-1])

    # The position of a character within a provided string
    # If there are two or more of the same character, the last one is determined
    if not string: return -1
    return occur_position(carac,string) if carac==string[-1] else global_pos(carac,string[:-1])
        
        
#### calculating Exponentiation
def power0(integer,pow):
  if pow==0: return 1
  return integer*power(integer,pow-1)

#### calculating Exponentiation ( another variant )
def power1(integer,pow):
  if pow==0:return 1
  if pow==1:return integer
  if pow%2: return power1(integer,(pow+1)/2)*power1(integer,pow/2)
  else : return power1(integer,pow/2)*power1(integer,pow/2)
# def power_efficiency():


#### Converting a decimal number to a binary number
def decimal_to_binary(n):
  if not n: return '0'
  return int(str(decimal_to_binary(n/2)) + str(n%2))



#### give a substring of a given string starting from the first occurrence of a given value
def substring(el,list):
  if len(list)==0 :
    return False 
  #else :
  if list[0]==el :
    return list
  else :
    return substring(el,list[1:])


### generate a list up to the given element
def isto(el):
  if el == 0 : return []
  return isto(el-1) + [el-1]


### map function
def map(func,list):
  if len(list)==0 : return []
  return [func(list[0])] + map(func,list[1:]) 

### outpout the element wise product of two lists
### If len(list1)==a is superior to len(list2)==b then the product is calculated
### up to the last element of list2, giving a product list of b elements
def product_element_wise(list1,list2):
  if len(list1)*len(list2)==0:
      return []
  return [list1[0]*list2[0]] + product_element_wise(list1[1:],list2[1:])

#def maximum(list):


### calculating maximum using divide and conquer
def max_divide_and_conquer(array,begin,end):
  if begin == end:
    return array[begin]
  elif begin == end-1:
    return array[begin] if array[begin] >= array[end] else array[end]
  else:
    mid = (begin+end)/2
    left=max_divide_and_conquer(array,begin, mid)
    right=max_divide_and_conquer(array,mid+1, end)
    return left if left>=right else right 

def maximum(list):
  return max_divide_and_conquer(list,0,len(list)-1)


### calculating minimum using divide and conquer
def min_divide_and_conquer(array,begin,end):
  if begin == end:
    return array[begin]
  elif begin == end-1:
    return array[begin] if array[begin] <= array[end] else array[end]
  else:
    mid = (begin+end)/2
    left=min_divide_and_conquer(array,begin, mid)
    right=min_divide_and_conquer(array,mid+1, end)
    return left if left<=right else right 

def minimum(list):
  return min_divide_and_conquer(list,0,len(list)-1)


### Check if an element exists using divide and conquer paradigm
def find_element(el,array,begin,end):
    list=[]
    if begin == end:
              return [True] if array[begin]==el else [False]
    else:
      mid = (begin+end)/2
      list.extend(find_element(el,array,begin, mid))
      list.extend(find_element(el,array,mid+1, end))

    return list

def find_element_main(elem,list):
  result=find_element(elem,list,0,len(list)-1)
  return any(element for element in result)


#### flatten a list recursively 

import types
def flatten(S):
    if S == []: return []
    if isinstance(S,types.IntType) :  return [S]
    if isinstance(S[0], types.ListType):
        return  flatten(S[:-1]) + flatten(S[-1])
    return flatten(S[:-1])+flatten(S[-1])
    
## Example :
##
##terrible_list=[[[5,3],11,[],[7781,25,[84,13,[84,36],74]]],[41,[[8,3,35,58,[84,263]],[78,20],13],[15,28]],132]
##print flatten(terrible_list)
##[5, 3, 11, 7781, 25, 84, 13, 84, 36, 74, 41, 8, 3, 35, 58, 84, 263, 78, 20, 13, 15, 28, 132]



#######################
#### The tower of Hanoî 
# Description : https://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
#
# The Tower of Hanoi puzzle was invented by the French mathematician 
# Edouard Lucas in 1883. He was inspired by a legend that tells of a Hindu temple 
# where the puzzle was presented to young priests. At the beginning of time, the priests 
# were given three poles and a stack of 64 gold disks, each disk a little smaller than the 
# one beneath it. Their assignment was to transfer all 64 disks from one of the three poles 
# to another, with two important constraints. They could only move one disk at a time, and 
# they could never place a larger disk on top of a smaller one. The priests worked very 
# efficiently, day and night, moving one disk every second. When they finished their 
# work, the legend said, the temple would crumble into dust and the world would vanish.

def Hanoi(N,A,B,C):
    global number
    if N==1:
      time.sleep(0.3)
      number+=1
      print 'Move Peg from spot {} -------> to spot {} : move nb={} '.format(A,C,str(number))
      
    else :
       Hanoi(N-1,A,C,B)
       Hanoi(1,A,B,C)
       Hanoi(N-1,B,A,C)
    return number

number=0
def main_Hanoi(N):
  print 'Here are the following moves: '
  return Hanoi(N,'A','B','C')


#### output permutations of a list
def output_permutations(list):
  output=[]
  if len(list)==1:  return [list]

  else:
      print list[1:], 'here is the list'
      print output_permutations(list[1:]), " execute the code "
      for perm in output_permutations(list[1:]):
           print perm, ' perm   '
           for i in range(len(perm)+1):
              output.append(perm[:i] + list[:1] + perm[i:])
  return output

#print output_permutations(range(10))


## string and a list permutations
def permut(list):
  output=[]

  ## test base case
  if len(list)==1:
    return [list]

  ## test if we are dealing with a string or with a list 
  perm=permut(list[1:])
  if list is str :
    first_char_in_list=list[0]
  else :
    first_char_in_list=list[0:1]
  for el in perm:
    for i in range(len(el)+1):
      output.append(el[:i]+first_char_in_list+el[i:])

  return output


#### Partitions of a positive integer
def partitions(number):
  list_partitions=[]

  if number==1:
    return [[1]]

  for el in partitions(number-1):
      el1=[1]+el
      list_partitions.append(el1)

      if len(el)>1:
        if el[-1]>el[-2] :
            el2=el[1:-2]+[1+el[-2]]+[el[-1]]
            if sum(el2)==number :  
               list_partitions.append(el2)

  list_partitions.append([number])
  return list_partitions


#### Another solution to the minimum coin change problem
def control(coins,integers):
  coins_set=set(coins)
  integers_set=set(integers)
  
  return True if integers_set.issubset(coins_set) else False
## coins=[1,2,5,10]
def coin_changes(number,coins):
  list_partitions=[]

  if number==1:
    return [[1]]

  for el in coin_changes(number-1,coins):
      el1=[1]+el
      if control(coins,el1):
        list_partitions.append(el1)

      if len(el)>1:
        if el[-1]>el[-2] :
            el2=el[1:-2]+[1+el[-2]]+[el[-1]]
            if sum(el2)==number :  
              if control(coins,el2):
                list_partitions.append(el2)

  list_partitions.append([number])
  return list_partitions

#### function to test the different execution times
def see_execution_time(begin1,end1,begin2,end2):
 
  time1=end1-begin1
  time2=end2-begin2
  print '%.15f  first result '%time1
  print '%.15f  secoond result'%time2
  return
#see_execution_time(begin1,end1,begin2,end2)


#### different paths from the top to the bottom of a triangle-like list like so :
###
# tree=[[55],
# [94,48],
# [95,30,96],
# [77,71,26,67],
# [85,21,54,96,36],
# [10,185,21,154,96,365]]

def possible_paths(tree):
  paths=[]
  if tree==[]:  return []
  if len(tree)==1:  return tree
  for el in possible_paths(tree[:-1]):
      for last_element in tree[-1]:
          paths.append(el + [last_element])
  return paths
  
### Maximum path 
def max_path(tree):
    return max(possible_paths(tree))

### Minimum path
def min_path(tree):
    return min(possible_paths(tree))

# print possible_paths(tree)
# print 'maximum path : ',max_path(tree)
# print 'minimum path : ',min_path(tree)

