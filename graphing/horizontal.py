import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Drinks last night')
ax.set_title('Who needs coffee?')

# display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    #plt.savefig("/home/student/mycode/graphing/2018summary.pdf")
    # save a copy to "~/static" (the "files" view)
plt.savefig("/home/student/static/lookatthat.pdf")
plt.show()
