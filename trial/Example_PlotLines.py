from matplotlib import pyplot as plt

#plt.style.use('seaborn-notebook')


ages_x = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850,
            57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392]


plt.plot(ages_x, py_dev_y, color='b', marker='.', linewidth='1', label='n=400')

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title('Accuracy by Epoch')

#plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('mygrapg.png')

plt.show()