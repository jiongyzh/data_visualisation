import matplotlib.pyplot as plt

input_values = list(range(1, 11))
squares = [x**2 for x in input_values]
plt.scatter(input_values, squares, s=40, edgecolors='none', c=input_values, cmap=plt.cm.Blues)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 11, 0, 110])
plt.show()
# plt.savefig('aaa.png', bbox_inches='tight')