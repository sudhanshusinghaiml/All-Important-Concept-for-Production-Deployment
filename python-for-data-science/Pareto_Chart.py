'''
    Code to plot Pareto Chart in python
'''

from matplotlib.ticker import PercentFormatter

#define aesthetics for plot
bar_color = 'steelblue'
line_color = 'red'
line_size = 4

plt.figure(figsize=(12,4))
#create basic bar plot
fig, ax1 = plt.subplots()
ax1.bar(product_line_df['PRODUCTLINE'], product_line_df['Count'], color=bar_color)

#add cumulative percentage line to plot
ax2 = ax1.twinx()
ax2.plot(product_line_df['PRODUCTLINE'], product_line_df['Cumulative_Count'], color=line_color, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax1.tick_params(axis='y', colors=bar_color)
ax2.tick_params(axis='y', colors=line_color)

for label in ax1.containers:
    ax1.bar_label(label)

for x_val, y_val in zip (range(len(product_line_df)), round(product_line_df['Cumulative_Count'],2)):
    ax2.text(x=x_val-0.20, y=y_val+0.125, s=y_val, fontsize=10, color="black", ha="center", va="center")
    
plt.suptitle('Product line Pareto Chart', fontsize=12)

#display Pareto chart
plt.show();

## =============================================================================================