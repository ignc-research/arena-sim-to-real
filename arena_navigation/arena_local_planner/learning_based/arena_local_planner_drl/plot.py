import numpy as np 
import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import random 



path = 'evaluation_360/'

#make dir for plots
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


#read in evaluation data
data = pd.read_csv('data/evaluation_360.csv')

done_reason = np.array(data['done_reason'])
episode = np.array(data['episode'])
adult_robot_distance = np.nan_to_num( np.array(data['nearest distance for adult']),nan=random.randint(3,14))
child_robot_distance = np.nan_to_num(  np.array(data['nearest distance for child']) ,nan=random.randint(3,14))
elder_robot_distance = np.nan_to_num(  np.array(data['nearest distance for elder']),nan=random.randint(3,14))
forklift_robot_distance =np.nan_to_num(   np.array(data['nearest distance for forklift']) ,nan=random.randint(3,14))
servicerobot_robot_distance = np.nan_to_num(  np.array(data['nearest distance for servicerobot']) ,nan=random.randint(3,14))
random_wanderer_robot_distance = np.nan_to_num(  np.array(data['nearest distance for random_wanderer']) ,nan=random.randint(3,14))
reward=np.array(data['reward'])
safe_dist_adult = np.nan_to_num( np.array(data['safe distance adult']),nan=1)
safe_dist_child = np.nan_to_num(  np.array(data['safe distance child']) ,nan=1)
safe_dist_elder = np.nan_to_num(  np.array(data['safe distance elder']),nan=1)
safe_dist_forklift =np.nan_to_num(   np.array(data['safe distance forklift']) ,nan=1)
safe_dist_servicerobot = np.nan_to_num(  np.array(data['safe distance servicerobot']) ,nan=1)
safe_dist_random_wanderer = np.nan_to_num(  np.array(data['safe distance random_wanderer']) ,nan=1)
#read out some values
adult_counter = np.count_nonzero(done_reason == 3)
child_counter = np.count_nonzero(done_reason == 4)
elder_counter = np.count_nonzero(done_reason == 5)
time_out_counter = np.count_nonzero(done_reason == 0)
collision_counter = np.count_nonzero(done_reason == 1)
goal_counter = np.count_nonzero(done_reason ==2)
num_episodes = adult_counter + child_counter  + elder_counter+ time_out_counter + goal_counter + collision_counter

#check if there were humans in level
# human_exist = adult_robot_distance.size != 0

#read safty distance

# time_to_goal = np.array(time_to_goal)
dic={0 : adult_robot_distance, 1 : child_robot_distance, 2 :elder_robot_distance,3 :forklift_robot_distance,4 :servicerobot_robot_distance,5 :elder_robot_distance}
dic_safe={0 : safe_dist_adult, 1 : safe_dist_child, 2 :safe_dist_elder,3 :safe_dist_forklift,4 :safe_dist_servicerobot,5 :safe_dist_random_wanderer}
dic_h={0 : 'adult', 1 : 'child', 2 :'elder', 3 :'forklift', 4 :'servicerobot', 5 :'random_wanderer'}
#hist plot of distances robot-human
for i in range(6):
    mu = np.mean(dic[i])
    std=np.std(dic[i])
    human_robot_distances = dic[i].flatten()
    counts, bins = np.histogram(human_robot_distances,bins=50)
    total_number = len(human_robot_distances)
    print()
    num_smaller_than_safety_distance = np.count_nonzero(np.array(human_robot_distances) < np.array(dic_safe[i]))

    plt.figure(i+1)
    plt.hist(bins[:-1],bins=bins,weights=counts/total_number*100, align = 'right',edgecolor='black', linewidth=0.8)
    # plt.axvline(dic_safe[i], color='r', linestyle='dashed', linewidth=1.5)
    plt.annotate('safety distance has been breached \n in %.1f %% of times '%(num_smaller_than_safety_distance/total_number*100) , xy=(0, 0.85), xycoords='axes fraction',color = 'red')
    plt.annotate('$\mu = %.2f$'%(mu) + ' \n$\sigma^2 = %.2f$'%(std), xy=(0.85, 0.85), xycoords='axes fraction',bbox=dict(boxstyle="round", fc="w"))
    plt.title('Hist of closest '+ dic_h[i] +' distances')
    plt.xlabel('distance')
    plt.ylabel('relative counts [%]')
    plt.savefig(path+dic_h[i]+'_distance_hist')
    plt.clf()

#calculate and plot ending counters per bins and in total and write text file
bin_size = 100
# ending = ending[~pd.isnull(data['Ending'])] #remove all nan
# ending = ending[ending != 'reset'] # remove all reset
done_reason = np.reshape(done_reason,(-1,bin_size))# reshape in bins of 100

collision_bin = []
adult_counter_bin = []
child_counter_bin = []
elder_counter_bin = []
time_out_counter_bin = []
goal_counter_bin = []

for row in done_reason:
    collision_bin.append(np.count_nonzero(row == 1)/bin_size*100)
    adult_counter_bin.append(np.count_nonzero(row == 3)/bin_size*100)
    child_counter_bin.append(np.count_nonzero(row == 4)/bin_size*100)
    elder_counter_bin.append(np.count_nonzero(row == 5)/bin_size*100)
    time_out_counter_bin.append(np.count_nonzero(row == 0)/bin_size*100)
    goal_counter_bin.append(np.count_nonzero(row == 2)/bin_size*100)

print('evaluation done')