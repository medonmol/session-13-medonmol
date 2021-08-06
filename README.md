<h2 align='center'> Assignment - Generators and Iteration tools 1</h3>

## Assignment 

### Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.


#### Solution 
The `VehicleGen` class in `session13.py` file takes in the filename ([NYC Parking Data](https://canvas.instructure.com/courses/2734597/files/146335396?wrap=1) in this assignment), and contains and `__iter__` method which allows us to access the car ticket tuple without having to initialize the class everytime the `get_tickets` generator is exhaused. The class also contains a static method `sanitize_raw_values`, which ensures basic data sanity, and a `count_violations` method, which returns the count of violations by car make 
### Goal 2

Calculate the number of violations by car make.


[link to the DeepNote notebook](https://deepnote.com/project/EPAi3-session13-medonmol-31OWeyXeRR6prl4DEmPImw/%2Fsession13.ipynb)