# PetShop Class Hierarchy in Python  

## Overview  
This project demonstrates **object-oriented programming (OOP)** in Python using **inheritance** and **polymorphism**.  
The `PetShop` base class is extended by `Cat` and `Dog` subclasses, and further specialized into unique roles like `Lazy`, `Hunter`, `Guard`, and `Guide`.  

Each pet can introduce itself using the `talk()` method, showcasing its properties.  

---

## Features  
- **Base Class (`PetShop`)**: Defines common attributes like size and validation.  
- **Subclasses (`Cat`, `Dog`)**: Add unique `noise` values.  
- **Specialized Roles**:  
  - `Lazy` Cat – small, white, lazy.  
  - `Hunter` Cat – black, a hunter, customizable size.  
  - `Guard` Dog – brown, a guard, customizable size.  
  - `Guide` Dog – golden, a guide, always large.  
- **Polymorphism**: Each pet introduces itself differently through `talk()`.  
- **Input Validation**: Pets can only be "small", "medium", or "large".  

---

## Example Usage  

```python
from petshop import Lazy, Hunter, Guard, Guide  

def main():
    pets = [
        Lazy(),
        Hunter("medium"),
        Guard("large"),
        Guide()
    ]
    for pet in pets:
        pet.talk()

if __name__ == "__main__":
    main()
