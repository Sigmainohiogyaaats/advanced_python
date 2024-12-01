abc = ('apple', 'banana', 'cherry')
my_itr = iter(abc) 

print(next(my_itr))
print(next(my_itr)) 
print(next(my_itr))

print("\n")

#iterating through a string object 
abc1 = "Arinjay" 
my_itr1 = iter(abc1) 

print(next(my_itr1)) 
print(next(my_itr1))  
print(next(my_itr1))  
print(next(my_itr1))  
print(next(my_itr1)) 
print(next(my_itr1))  
print(next(my_itr1))  
print("\n")

#looping through an iterator 
abc2 = ("apple", "Banana", "Cherry") 
for i in abc2: 
    print(i)
print("\n") 


abc3 = "Arinjay"  
for i in abc3: 
    print(i) 

print("\n") 

#creating an iterator 
class my_numbers: 
    def __iter__(self): 
        self.a = 1 
        return self 
    
    def __next__(self): 
        x = self.a 
        self.a += 1 
        return x  
    
my_class = my_numbers() 
my_iter = iter(my_class) 

print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 

