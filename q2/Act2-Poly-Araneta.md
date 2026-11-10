1. Answer the following questions
a. What is duck typing, as explained in the video?

- Duck typing is a concept in Python where an object can be used based on the methods it has, rather than its class or type. If an object has the required method, it can perform the action even if it does not belong to a specific parent class.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

- The Car class needed to have a method with the same name that the loop calls, such as move() or the method used in the video. It did not need to inherit from Animal as long as it had the required method.

3. How does the code in 2.2 demonstrate polymorphism?
- The code demonstrates polymorphism because the Car, Boat, and Drone classes all have the same move() method, but each performs a different action. The start_trip() function works with all three objects without needing to know their specific classes. This also demonstrates duck typing because the objects only need to have the required move() method to work with the function.