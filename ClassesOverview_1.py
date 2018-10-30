# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:54:30 2018

Classes and Methods Simple Example in Code

@author: vince
"""

#note capitalization.  It is common practice to capitalize the first letter
#of words in class name.
class DomesticDog():
    
    #Class Object Attribute
    #This will be the same for every object regardless of what you send in.
    
    species = 'mammal'
    genus = 'Canis (canines)'
    order = 'Carnivora'
    
    def __init__(self,breed,name, spots = 'None'): #you can set default values here
        
        #Object Attributes
        #Takes in the parameters in argument (*args) and assigns it to
        #whatever 'self' you set up.  example. object-> mydog = DomesticDog() <-Class Call pass params into ()
        
        self.breed = breed
        self.name = name
        self.spots = spots
        
    #Methods are functions specific to a class.  You make them very similarly to regular functions.
    
    def bark(self): #note self.  That allows you to reference attributues.  
        print('Meow. Come here KITTY.  My name is {}.'.format(self.name))
        
    #You can use local parameters that don't get assigned to the object as attributes too like you would a regular function.
    def mark(self, spot, time):
        print('Haha.  I the great {} known as {} will mark {} at precisely {}.'.format(self.order,self.name, spot, time))
  
class Box():
    
    #Our boxes will have 4 walls, two vertical and two horizontal
    vert_sides = 2
    horiz_sides = 2
    
    def __init__(self, height, width):
        
        self.height = height
        self.width = width
        
        #now those pesky calculated bits
        self.perimeter = self.vert_sides * height + self.horiz_sides * width
        self.area = height * width
    
    #now I don't want to actually write print statements each time i have a box...
    def summary(self):
        print('The height is {}'.format(self.height))
        print('The width is {}'.format(self.width))
        print('The perimeter is calculated at {}'.format(self.perimeter))
        print('The area is calculated at {}'.format(self.area))
        
        
def main():
    #Create an object of DomesticDog class
    my_dog = DomesticDog(breed = 'poodle', name = 'Basher')
    
    print(my_dog.name)
    
    #let's have my_dog bark:
    my_dog.bark()
    
    #Make him mark "Darlene's carpet"
    my_dog.mark("Darlene's carpet", "10:00AM")


    #This can be very nice in defining calculated features for an object
    #Let's have a class Box that automatically gives us perimeter and area
        
    #Now let's make a couple boxes
            
    box1 = Box(height = 5, width = 10)
    box2 = Box(height = 30, width = 10)
    
    #And let's get their summaries
    print("\nBox 1's stuff: \n")
    box1.summary() #Note there are print statements in the method, so don't call inside a print statement here.  Get's it's own line.
    print("\nBox 2's stuff: \n")
    box2.summary()
        

if __name__ == "__main__":
    main()
        
        
    