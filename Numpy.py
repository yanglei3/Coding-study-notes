#Numpy
import sys
import numpy as np

# Check Python version
print (sys.version)

# Check datatype
type(2)
type('2')
type(2.0)
type(False)

# Convert string to float
type(float('2'))

# Expression
25 // 6

# String operations
Name = "Michael Jackson"
print name[-10] #string indexing
Name[::2] #Get every second element
Name[0:5:2] #Get every second element from index 0 to 4

# Concatenate string
print (3 * Name) #Print Name 3 times

# Escape Sequences
print (" Michael Jackson \n is the best" )
print (" Michael Jackson \t is the best" )
print (" Michael Jackson \\ is the best" )
print (r" Michael Jackson \ is the best" )

# String methods
Name.upper()
Name.replace("Michael", "A")
Name.find("M")
 
# Tuple
tuple1 = ("disco",10,1.2 )
print(type(tuple1[0]))
tuple2 = tuple1 + ("hard rock", 10)
len(tuple2)
tuple2[0:3]
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
NestedT[2][0] #Returns pop

# List
L = ["Michael Jackson", 10.1, 1982]
L.extend(['pop', 10]) #Returns ['Michael Jackson', 10.2, 'pop', 10]
L.append(['pop', 10]) #Returns ['Michael Jackson', 10.2, ['pop', 10]]
L[0] = "Hard rock" #Lists are mutable
del(L[0]) #Delete the element based on the index
Lnew = L
L[0] = 'changed'
Lnew #Lnew[0] also changed to 'changed', since L and Lnew referencing to a same list
Lnew1 = L[:]
L[0] = 'change again'
Lnew1 # Lnew1[0] won't turns to 'change again', since Lnew1 is referencing the clone of L

# Dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict["key1"]
Dict[(0, 1)] #Keys could be any immutable objects
Dict.keys() #Get all the keys
Dict.values() #Get all values
Dict['Key7'] = 3.0 #Append value
del(['Key7']

# Sets
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"} #Python will automatically remove duplicate items
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19","Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
set1.add("item")
set1.remove("item")
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
intersection = album_set1 & album_set2
album_set1.difference(album_set2) #Items in set1 but not in set2
album_set1.intersection(album_set2) #Intersection of set1 and set2
album_set1.union(album_set2)
set(album_set1).issuperset(album_set2)

# Comparison Operators
'BA' > 'AB' #Upper Case Letters have different ASCII code than Lower Case Letters, which means the comparison between the letters in python is case-sensitive

# for loop execute a code block multiple times
for i in range(0, 8):
    print(i)

# while loop iterates merely until the condition in the argument is not met

# Create a class Circle
class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 
# Create an instance of class Circle
RedCircle = Circle(10, 'red')
dir(RedCircle) #Find out the methods could be used on this object, many of them are default python methods
RedCircle.radius
RedCircle.radius = 1

# Reading and writing files with Python
# example1 = "/resources/data/Example1.txt"
# file1 = open(example1, "r")
# file1.name
# file1.mode
# file_content = file1.read()
# file1.close()
# with open(example1, "r") as file1:
#    FileContent = file1.read()
#    print(FileContent)
# file1.read(4) means read 4 characters
# file1.readline() means read 1 line
# with open('/resources/data/Example2.txt', 'w') as writefile:
#    writefile.write("This is line A")

# Pass a scalar to a Numpy array
s = np.array(5) 

# Pass a list to a Numpy
a = np.array([1,2,3,4])

# Pass a list of lists to m, where each list represents a row
m = np.array([[1,2,3], [1,2,3], [1,2,3]])
m.size #returns the number of elements
m.ndim #returns the dimension of the array
m.shape #returns a tuple of integers indicting the size of the array in each dimension, (number of lists, number of items in each list)
type(a) #returns numpy.ndarray
m.dtype # returns datatype of the elements in the array, e.g float64
m.mean()
m.std()
m.min()
m.max()

# Numpy array indexing https://numpy.org/doc/stable/reference/arrays.indexing.html#arrays-indexing
m[1:3] = [4,5,6], [7,8,9] #***Set the 2nd element and 3rd element to new values***
m[1,2]
m[1][2]
m[0:3][2]

np.pi
np.six(m)

# Element-wise operations
nparray = np.array([1, 2, 3, 4, 5]) + 5
nparray1 = np.multiply([1, 2, 3, 4, 5], 5)
nparray + nparray1
nparray * nparray1
# m *= 0 Set all the elements of matrix m to zero
# 2D Numpy array multiplication requires the array in same shape

# Dot product
np.dot(nparray, nparray1) #1D nparry returns a real number
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[1,1],[1,1],[1,1]])
np.dot(a1,a2) #two inner dimensions need to be the same size, the answer matrix's shape is the two outer dimensions
 
# Numpy array transpose
a1.T
