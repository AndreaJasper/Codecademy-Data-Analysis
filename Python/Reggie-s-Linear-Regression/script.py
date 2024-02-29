# Task 1
# Write your get_y() function here
def get_y(m,b,x):
   y = m*x + b
   return y
# Uncomment each print() statement to check your work. Each of the following should print True
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)
print("  -----  ")


# Tasks 2 and 3
# Write your calculate_error() function here
def calculate_error(m,b,point):
  x_point, y_point = point
  getY = get_y(m, b, x_point)
  distance = getY - y_point
  return abs(distance)

# Task 4
# Uncomment each print() statement and check the output against the expected result

# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))

# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))

# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))

# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))
print("  -----  ")


# Task 5
# Write your calculate_all_error() function here
def calculate_all_error(m, b, points):
  total = 0
  for point in points:
    calculateError = calculate_error(m, b, point)
    total += calculateError
    return total


# Task 6
# Uncomment each print() statement and check the output against the expected result
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

# every point in this dataset lies upon y=x, so the total error should be zero:
print(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
print(calculate_all_error(-1, 1, datapoints))
print("  -----  ")


# Tasks 8 and 9
# Using a list comprehension, let’s create a list of possible m values to try. Make the list possible_ms that goes from -10 to 10 inclusive, in increments of 0.1.
# Now, let’s make a list of possible_bs to check that would be the values from -20 to 20 inclusive, in steps of 0.1.
possible_ms = [m*0.1 for m in range(-100, 101)]
possible_bs = [b*0.1 for b in range(-200, 201)]


# Task 10
# We are going to find the smallest error. First, we will make every possible y = m*x + b line by pairing all of the possible ms with all of the possible bs. Then, we will see which y = m*x + b line produces the smallest total error with the set of data stored in datapoints.
# First, create the variables that we will be optimizing:
# smallest_error — this should start at infinity (float("inf")) so that any error we get at first will be smaller than our value of smallest_error
# best_m — we can start this at 0
# best_b — we can start this at 0
# By the end of these nested loops, the smallest_error should hold the smallest error we have found, and best_m and best_b should be the values that produced that smallest error value.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

# Tasks 11 and 12
# Iterate through each element m in possible_ms
# For every m value, take every b value in possible_bs
# If the value returned from calculate_all_error() on this m value, this b value, and datapoints is less than our current smallest_error,
# Set best_m and best_b to be these values, and set smallest_error to this error.
for m in possible_ms:
  for b in possible_bs:
    error = calculate_all_error(m, b, datapoints)
    if error < smallest_error:
      best_m = m
      best_b = b
      smaller_error = error

print(best_m, best_b, smallest_error)
print("  -----  ")

# Task 13
# Using this m and this b, what does your line predict the bounce height of a ball with a width of 6 to be? In other words, what is the output of get_y() when we call it with:
# m = 0.4
# b = 1.6
# x = 6
print(get_y(0.4, 1.6, 6))