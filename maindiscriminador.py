from discriminador import Filter
import matplotlib.pyplot as plt


result = Filter([1.0], [0.3],100)
lol = result.lms()
print(lol)
