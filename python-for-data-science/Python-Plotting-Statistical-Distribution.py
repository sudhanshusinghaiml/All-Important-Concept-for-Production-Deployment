
plt.figure(figsize=(8,4))
# sns.set(font_scale=2)
# font = {'family':'cursive','color':'green','size':20}
sns.barplot(x =k, y = binomial_prob)
plt.title("Binomial: n=%i , p=%.2f" % (n, p), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
# plt.xticks(rotation = 90)
plt.show();

-----------------------------------------------------------------------------------------
- We are plotting the distributions here to better visualize the calculations.
- Of course you do not 'need' to create the following visualization to answer the question above.
- You can directly use the cdf function for probability calculations.

plt.figure(figsize=(8,4))
color_bar= ['red' if (k<8) else 'blue' for k in range(0,11) ]
sns.barplot(x=k, y=binomial_prob, palette=color_bar)
plt.title("Binomial: n=%i , p=%.2f" % (n, p), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
plt.show();
-----------------------------------------------------------------------------------------
# plot the probability distribution
barl = plt.bar(k, binomial_prob) # make a bar plot
plt.title("Binomial: n=%i , p=%.2f" % (n, p), fontsize=15) # set the title
plt.xlabel("Number of Successes") # set the x-axis label
plt.ylabel("Probability of Successes") # set the y-axis label
for i in range(0, 8):
    barl[i].set_color("r") # color the bars in red where number of successes is less than 8
plt.show() 
------------------------------------------------------------------------------------------
plt.figure(figsize=(15, 4))

plt.subplot(131)
binomial_70 = binom.pmf(k, n, p=0.7)

# plot the distribution of the same
plt.bar(k, binomial_70)
plt.title("p=%.2f" % (0.7), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")

plt.subplot(132)
binomial_80 = binom.pmf(k, n, p=0.8)

# plot the distribution of the same
plt.bar(k, binomial_80)
plt.title("p=%.2f" % (0.8), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")

plt.subplot(133)
binomial_90 = binom.pmf(k, n, p=0.9)

# plot the distribution of the same
plt.bar(k, binomial_90)
plt.title("p=%.2f" % (0.9), fontsize=15)
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")

plt.tight_layout(w_pad=5)

## ===================================================================
plt.figure(figsize=(8,4))
sns.pointplot(x='Weight_Gain', y='Response', data=df, hue='Duration',ci=None);
plt.title("Interaction plot of dentist and method", fontsize=15)
plt.xlabel("Dentist")
plt.ylabel("Mean of responses")
# plt.xticks(rotation = 90)
plt.show();

## ===================================================================

# We are plotting the probability distribution to better visualize the calculations.

plt.plot(df_data["BreakingStrength"], df_data["PDF"]) # plotting the pdf of the normal distribution
plt.axvline(breaking_strength_assume1, c="r") # draw a red vertical line at x = z_317
x1 = np.linspace(df_data["BreakingStrength"].min(), breaking_strength_assume1, 50) # create an array of 50 numbers between min SAT score and 800
plt.fill_between(x1, norm.pdf(x1, breaking_strength_mean, breaking_strength_std), color="r") # fill the specified region with red color
plt.xlabel("BreakingStrength") # set the x-axis label
plt.ylabel("Probability") # set the y-axis label
plt.title("Normal Distribution") # set the title
plt.show() # display the plot

## ===================================================================

# plot the probability distribution
# We are plotting the distributions here to better visualize the calculations.

plt.plot(df_data["BreakingStrength"], df_data["PDF"]) # plot the pdf of the normal distribution
x1 = np.linspace(5, 5.5, 50) # create an array of 50 numbers between min and max
plt.fill_between(x1, norm.pdf(x1, breaking_strength_mean, breaking_strength_std), color="r") # fill the specified region with red color
plt.xlabel("BreakingStrength") # set the x-axis label
plt.ylabel("Probability") # set the y-axis label
plt.title("Normal Distribution") # set the title
plt.show() # display the plot

## ====================================================================
# plot the standard normal distribution
# and visualize the standardized scores
# We are plotting the distributions here to better visualize the calculations.
fig, ax = plt.subplots()
x = np.linspace(-4,4,50)
ax.plot(x, norm.pdf(x, loc = 0, scale = 1), color = 'b')
ax.set_title('Standard Normal Distribution')
ax.set_xlabel('Z-scores')
ax.set_ylabel('Probability')
ax.axvline(z_from_5, linestyle = '--', color = 'green')
ax.axvline(z_from_55, linestyle = '--', color = 'black')
plt.show()

## ======================================================================

Less than 3.17
===============
fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.2, bottom = 0.3)
fig.suptitle('Plotting the Distribution for Breaking Strength of 3.17', fontsize=12)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# We are plotting the probability distribution to better visualize the calculations.
ax1.plot(df_data["BreakingStrength"], df_data["PDF"]) # plotting the pdf of the normal distribution
ax1.axvline(breaking_strength_assume1, c="g") # draw a red vertical line at x = 3.17
x1 = np.linspace(df_data["BreakingStrength"].min(), breaking_strength_assume1, 50) #create an array of 50 numbers between min breaking strength and breaking strength that we want to analyze 
ax1.fill_between(x1, norm.pdf(x1, breaking_strength_mean, breaking_strength_std), color="g") # fill the specified region with red color
ax1.set_xlabel("BreakingStrength") # set the x-axis label
ax1.set_ylabel("Probability") # set the y-axis label
ax1.set_title("Normal Distribution Plot") # set the title

## Plotting the Z-Score
x11 = np.linspace(-4,4,50)
y11 = norm.pdf(x31, loc = 0, scale = 1)
ax2.plot(x11, y11, color = 'b')
ax2.axvline(z_317, linestyle = '--', color = 'green')
ax2.set_xlabel('Z Scores')
ax2.set_ylabel('Probability')
ax2.set_title('Z Score Plot for Z=%0.4f' %(z_317))

plt.show() # display the plot
## ============================================================================================

More than 3.6
-------------
fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.2, bottom = 0.3)
fig.suptitle('Plotting the Distribution for Breaking Strength of 3.6', fontsize=12)
ax21 = fig.add_subplot(1,2,1)
ax22 = fig.add_subplot(1,2,2)

# We are plotting the probability distribution to better visualize the calculations.
ax21.plot(df_data["BreakingStrength"], df_data["PDF"]) # plot the pdf of the normal distribution
ax21.axvline(breaking_strength_assume2, c="g") # draw a green vertical line at x = 3.6
x2 = np.linspace(breaking_strength_assume2, df_data["BreakingStrength"].max(), 50) #create an array of 50 numbers between min breaking strength and breaking strength that we want to analyze
ax21.fill_between(x2, norm.pdf(x2, breaking_strength_mean, breaking_strength_std), color="g") # fill the specified region with red color
ax21.set_xlabel("BreakingStrength") # set the x-axis label
ax21.set_ylabel("Probability") # set the y-axis label
ax21.set_title("Normal Distribution Plot") # set the title

## Plotting the Z-Score
x12 = np.linspace(-4,4,50)
y12 = norm.pdf(x12, loc = 0, scale = 1)
ax22.plot(x12, y12, color = 'b')
ax22.axvline(z_lessthan_36, linestyle = '--', color = 'green')
ax22.set_xlabel('Z Scores')
ax22.set_ylabel('Probability')
ax22.set_title('Z Score Plot for Z=%0.4f' %(z_lessthan_36))

plt.show() # display the plot

## =========================================================================================================
BETWEEN 5 and 5.5
===================
fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.2, bottom = 0.3)
fig.suptitle('Plotting the Distribution for Breaking Strength between 5 and 5.5', fontsize=12)
ax31 = fig.add_subplot(1,2,1)
ax32 = fig.add_subplot(1,2,2)

# We are plotting the probability distribution to better visualize the calculations.
ax31.plot(df_data["BreakingStrength"], df_data["PDF"]) # plot the pdf of the normal distribution
ax31.axvline(breaking_strength_from_assume, c="g") # draw a green vertical line at x = 5
ax31.axvline(breaking_strength_to_assume, c="r") # draw a red vertical line at x = 5.5
x3 = np.linspace(breaking_strength_from_assume, breaking_strength_to_assume, 50) # create an array of 50 numbers between min and max
ax31.fill_between(x3, norm.pdf(x3, breaking_strength_mean, breaking_strength_std), color="g") # fill the specified region with color
ax31.set_xlabel("BreakingStrength") # set the x-axis label
ax31.set_ylabel("Probability") # set the y-axis label
ax31.set_title("Normal Distribution Plot") # set the title

## Plotting the Z-Score
x13 = np.linspace(-4,4,50)
y13 = norm.pdf(x13, loc = 0, scale = 1)
ax32.plot(x13, y13, color = 'b')
ax32.axvline(z_from_5, linestyle = '--', color = 'green')
ax32.axvline(z_from_55, linestyle = '--', color = 'green')
ax32.set_xlabel('Z Scores')
ax32.set_ylabel('Probability')
ax32.set_title('Z Score Plot for Z_lower=%0.4f and Z_higher=%0.4f' %(z_from_5, z_from_55))

plt.show() # display the plot
## ===============================================================================================

NOT BETWEEN 3 and 7.5
-----------------------
fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.2, bottom = 0.3)
fig.suptitle('Plotting the Distribution for Breaking Strength between 5 and 5.5', fontsize=12)
ax41 = fig.add_subplot(1,2,1)
ax42 = fig.add_subplot(1,2,2)

# We are plotting the probability distribution to better visualize the calculations.
ax41.plot(df_data["BreakingStrength"], df_data["PDF"]) # plot the pdf of the normal distribution
ax41.axvline(breaking_strength_from_assume2, c="g") # draw a green vertical line at x = 5
ax41.axvline(breaking_strength_to_assume2, c="r") # draw a red vertical line at x = 5.5
x4 = np.linspace(df_data["BreakingStrength"].min(), breaking_strength_from_assume2, 50)
x5 = np.linspace(breaking_strength_to_assume2,df_data["BreakingStrength"].max(), 50)
ax41.fill_between(x4, norm.pdf(x4, breaking_strength_mean, breaking_strength_std), color="r") # fill the specified region with red color
ax41.fill_between(x5, norm.pdf(x5, breaking_strength_mean, breaking_strength_std), color="r") # fill the specified region with red color
ax41.set_xlabel("BreakingStrength") # set the x-axis label
ax41.set_ylabel("Probability") # set the y-axis label
ax41.set_title("Normal Distribution Plot") # set the title

## Plotting the Z-Score
x14 = np.linspace(-4,4,50)
y14 = norm.pdf(x14, loc = 0, scale = 1)
ax42.plot(x14, y14, color = 'b')
ax42.axvline(z_from_3, linestyle = '--', color = 'green')
ax42.axvline(z_from_7_5, linestyle = '--', color = 'green')
ax42.set_xlabel('Z Scores')
ax42.set_ylabel('Probability')
ax42.set_title('Z Score Plot for Z_lower=%0.4f and Z_higher=%0.4f' %(z_from_3, z_from_7_5))

plt.show() # display the plot

## ====================================================================================================