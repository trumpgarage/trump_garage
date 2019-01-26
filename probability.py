def get_percentages(values):
    
    totalfreq = sum(values) #total number of frequencies
    size=len(values) #size of the array
    totalfreq1=[totalfreq]*size #creates array with value total freq with the same size as number of frequencies
    prob=[]
    for i in range(size):
    	prob.append(values[i]/totalfreq1[i])
    return prob
