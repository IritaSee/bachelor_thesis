from posixpath import split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

datas = ['result_AP.csv','result_ap50.csv','result_ap75.csv','result_AR1.csv','result_AR10.csv','result_AR100.csv']
names = ['Average Precision','AP50 Result','AP75 Result','ARmax1 Result','ARmax10 Result','ARmax100 Result']
idx = 0
pattern=["|" ,"-" , "+" , "x", "o"]
for file in datas:
    data = pd.read_csv(file)
    sgd = data['SGD']
    adam = data['Adam']
    labels = ['10 Epochs','20 Epochs','30 Epochs','40 Epochs','50 Epochs']
    x = np.arange(len(labels))
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, sgd, width, label='SGD', hatch = pattern[3])
    rects2 = ax.bar(x + width/2, adam, width, label='Adam', hatch = pattern[4])
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('value')
    ax.set_title(names[idx])
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc=2, handleheight = 2.0)
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    idx = idx+1
    #plt.savefig('./greyscale_result_graphs/'+file.split('.')[0]+'.png')
    plt.show()