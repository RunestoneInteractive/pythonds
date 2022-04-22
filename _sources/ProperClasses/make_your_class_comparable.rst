Making your Class Comparable
============================


Let us suppose that we want to know if one die is "equal to" another die.  What does that mean?  Does it mean that the same number is up on the face of the die?  What if one die is a 10 sided die and the other only six?  Could those two dice ever be equal?

With Python we get to decide what it means for two dice to be equal to each other.  We express what that means in code by writing the ``__eq__`` method for our MSDie class.  Not only does this allow us to define the rules but it also allows us to use the standard operators in our code, for example we could write ``die1 == die2`` to check if they are equal.  Further, we can write several different methods for all manner of comparisons that we may want to make including:

* ``__lt__`` less than ``<``
* ``__gt__`` greater than ``>``
* ``__eq__`` equal to ``==``
* ``__le__`` less than or equal to  ``<=``
* ``__ge__`` greater than or equal to ``>=``
* ``__ne__`` not equal to ``!=``


Let us look at an implementation of the ``__eq__`` method.

.. activecode:: msdie_eq

    class MSDie:
        """
        Multi-sided die
        
        Instance Variables:
            current_value
            num_sides
        
        """
        
        def __init__(self, num_sides):
            self.num_sides = num_sides
            self.current_value = self.roll()
        
        def roll(self):
            self.current_value = random.randrange(1,self.num_sides+1)
            return self.current_value
        
        def __str__(self):
            return str(self.current_value)
        
        def __repr__(self):
            return "MSDie({}) : {}".format(self.num_sides, self.current_value)
            
        def __eq__(self,other):
            return self.current_value == other.current_value
            
        def __lt__(self,other):
            return self.current_value < other.current_value
            
        def __le__(self, other):
            return self.current_value <= other.current_value

    
Notice that the ``__eq__`` method has two formal parameters, ``self`` as usual and ``other`` other represents the die to which we want to compare.  You can think of it as though we are testing ``self == other``.

Lets try these operations in action in the next activecode.  Before you run them answer the questions following the example.

.. activecode:: msdie_tryout
    :include: msdie_eq
    
    x = MSDie(6)
    y = MSDie(7)
    
    x.current_value = 6
    y.current_value = 5
    
    print(x == y)
    print(x < y)
    print(x > y)
    print(x != y)
    print(x<=y)
    print(x>=y)
    print(x is y)
    

.. mchoice:: test_ne

    What does ``x > y`` evaluate to?
    
    - True

      + Correct
      
    - False

      - Incorrect
      
    - This comparison will produce an Error
    
      - You might think this is a logical answer but Python is doing something tricky for us behind the scenes.
      

.. mchoice:: test_gt

    What does ``x != y`` evaluate to?
    
    - True
    
      + Correct
      
    - False
    
      - Incorrect
      
    - This comparison will produce an Error
    
      - You might think this is a logical answer but Python is doing something tricky for us behind the scenes.


You might think it would be tedius to write all of the comparison functions but in fact it appears that just three are required.  ``__eq__``, ``__lt__``, and ``__le__``.  What happens if you do not write ``__le__``?

.. activecode:: comp_onlygreater

    What happens if you only write the functions ``__eq__, __gt__, __ge__``?
    ~~~~
    

.. reveal:: gt_discussion

    Python wants you to write the less than versions of the comparison operators.  Writing the greater than versions will create errors.
    

So what is python doing?  It is providing default implementations of some of the comparison operators in the parent class!  It does this by writing them by calling the "dunder methods" directly and using logic.

.. activecode:: cmp_defaults

    Can you write versions of ``__ne__, __gt__, __ge__`` in terms of ``__eq__, __lt__, __le__``?
    ~~~~


    =====
    
    from unittest.gui import TestCaseGui
 
    class myTests(TestCaseGui):
 
       def testOne(self):
          x = MSDie(6)
          y = MSDie(7)
          
          x.current_value = 6
          y.current_value = 5
          
          print(x != y)
          print(x<=y)
          print(x>=y)
          print(x is y)
      
          self.assertIn("def __ne__", self.getEditorText(), "Your code should define __ne__")      
          self.assertIn("def __gt__", self.getEditorText(), "Your code should define __gt__")      
          self.assertIn("def __ge__", self.getEditorText(), "Your code should define __ge__")                          
          self.assertIn(".__eq__", self.getEditorText(), "Your code should use __eq__")
          self.assertIn(".__lt__", self.getEditorText(), "Your code should use __lt__")
          self.assertIn(".__le__", self.getEditorText(), "Your code should use __le__")
          self.assertFalse(x != y, "x should not equal y")
          self.assertTrue(x > y, "x is greater than y")
          self.assertTrue(x >= y, "x is greater than or equal to y")
 

    myTests().main()
    
