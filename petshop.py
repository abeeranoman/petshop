#A pet shop sells two types of pets: cats and dogs. All pets have a size (small, medium, large). Cats always make a “Meow” noise. Dogs always make a “Woof” noise. 
# White cats are lazy and black cats are hunters. Brown dogs are guards and golden dogs are guides.
#  👉 Model this in a class hierarchy: Base class: Pet Intermediate classes: Cat and Dog Lowest-level classes: Lazy, Hunter, Guard, and Guide. Each pet should be able to tell its type, color, job, size, and noise.
#  Finally: Instantiate a white cat (small) and a golden dog (large).

#(Quite literally the toy manufacturer but worded differently)




class PetShop:
    def __init__(self, size):
        
        self.size = size
        size = size.strip().lower()
        allowed_size = ["small", "large", "medium"]
        if size not in allowed_size:
            raise ValueError ("They can be either small, medium, or large")
        
    def talk(self):
        get_class = self.__class__.__bases__[0].__name__
        print(
            f"I am a {self.colour} {get_class}, and I'm good at being {self.job}."
            f"I am {self.size}, and I say {self.noise} very loudly!"
        )

class Cat(PetShop):
        noise = "meow"

class Dog(PetShop):
    
        noise = "woof"

class Lazy(Cat):
    def __init__(self):
        self.colour = "white"
        self.job = "lazy"
        self.size = "small" 
            
class Hunter(Cat):
    def __init__(self, size):
        super().__init__(size)
        self.colour = "black"
        self.job = "a hunter"
class Guard(Dog):
    def __init__(self, size):
        super().__init__(size)
        self.colour = "brown"
        self.job = "a guard"

class Guide(Dog):
    def __init__(self):
        self.colour = "golden"
        self.job = "a guide"
        self.size = "large"


def main():
    toys = [
        Lazy(),
        Hunter("medium"),
        Guard("large"),
        Guide()
    ]
    for toy in toys:
        toy.talk()

if __name__== "__main__":
    main()



