'''
This program estimates the value of Pi (π) using a Monte Carlo simulation.

- **Process**:
  1. A large number of random points (`generatedPoints`) are generated within a square of side length 2 (centered at the origin).
  2. Each point has random x and y coordinates between -1 and 1.
  3. The program checks if each point lies within a unit circle (radius 1) centered at the origin, using the equation:
     \[
     x^2 + y^2 < 1
     \]
  4. The ratio of points inside the circle (`numberOfHits`) to the total points generated is used to approximate π:
     \[
     \pi \approx 4 \times \frac{\text{number of points inside the circle}}{\text{total number of points}}
     \]

- **Output**:
  - The program calculates and displays the estimated value of Pi (π) to six decimal places.

- **Key Features**:
  - This method demonstrates the use of probability and randomness to estimate mathematical constants.
  - The accuracy of the estimate increases with a larger number of generated points.
'''
import random
generatedPoints = 1000000
numberOfHits = 0
for i in range (1000000):
   x = random.uniform (-1,1) 
   y = random.uniform (-1,1) 
   
   if x * x + y * y < 1:
    numberOfHits += 1

pi = (4 * numberOfHits) / generatedPoints

print ("PI is", "{:+.6f}".format(pi))
