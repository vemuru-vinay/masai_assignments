#Task 1
import numpy as np

temps_celsius = np.array([22,25,28,24,26])

temps_fahrenheit = temps_celsius * 1.8 + 32

avg_fahrenheit = np.sum(temps_fahrenheit)/len(temps_fahrenheit)

print(f"Celsius : {temps_celsius}")
print(f"Fahrenheit : {temps_fahrenheit}")
print(f"Average Fahrenheit : {avg_fahrenheit}")

#Task - 2
students_marks = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape :",np.shape(students_marks))
print("Total Elements :",np.size(students_marks))
print("Highest Score:",np.max(students_marks))
print("Lowest Score:",np.min(students_marks))
print("Range",np.max(students_marks) - np.min(students_marks))


#Task - 3
import numpy as np
import time

np_array = np.arange(1, 50001)
py_list = list(range(1, 50001))


runs = 10000


start_np = time.time()
for _ in range(runs):
    np_sum = np.sum(np_array)
end_np = time.time()
np_time = (end_np - start_np) / runs

start_py = time.time()
for _ in range(runs):
    py_sum = sum(py_list)
end_py = time.time()
py_time = (end_py - start_py) / runs

speed_factor = py_time / np_time if np_time > 0 else float("inf")

print(f"NumPy sum: {np_sum}")
print(f"Python sum: {py_sum}")
print(f"NumPy time: {np_time:.6f} seconds")
print(f"Python time: {py_time:.6f} seconds")
print(f"NumPy is {speed_factor:.1f}x faster")