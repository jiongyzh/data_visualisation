import pygal

from dice import Dice


dice_1 = Dice()
dice_2 = Dice(10)
results = []
frequencies = []
max_result = dice_1.num_sides+dice_2.num_sides

for i in range(5000):
    results.append(dice_1.roll() + dice_2.roll())

for val in range(2, max_result+1):
    frequencies.append(results.count(val))

hist = pygal.Bar()

hist.title = 'Results of rolling two dice 1000 times'
hist.x_labels = list(str(i) for i in range(2, max_result+1))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6 + D10', frequencies)
hist.render_to_file('output_files/dice_visual.svg')