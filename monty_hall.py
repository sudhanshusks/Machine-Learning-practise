import numpy as np

def simulate_prizedoor(nsim):
	arr=[]
	for i in np.arange(nsim):
		arr.append(np.random.randint(0,3))
	sims=np.array(arr)
	return sims

def simulate_guess(nsim):
	arr=[]
	for i in np.arange(nsim):
		arr.append(np.random.randint(0,3))
	guesses=np.array(arr)
	return guesses

def goat_door(prizedoors, guesses):
	goats=[]
	arr=0
	init=np.array([0,1,2])
	for x in np.arange(len(guesses)):
		init=[0,1,2]
		if(prizedoors[x]==guesses[x]):
			if(guesses[x]==0):
				arr=1
			elif(guesses[x]==1):
				arr=2
			else:
				arr=0
		else:
			init.remove(guesses[x])
			init.remove(prizedoors[x])
			arr=init[0]
		goats.append(arr)
	goats=np.array(goats)
	return goats

def switch_guess(guesses, goatdoors)	:
	goats=[]
	arr=0
	init=np.array([0,1,2])
	for x in np.arange(len(guesses)):
		init=[0,1,2]
		if(goatdoors[x]==guesses[x]):
			if(guesses[x]==0):
				arr=1
			elif(guesses[x]==1):
				arr=2
			else:
				arr=0
		else:
			init.remove(guesses[x])
			init.remove(goatdoors[x])
			arr=init[0]
		goats.append(arr)
	goats=np.array(goats)
	return goats

def win_percentage(guesses, prizedoors):
	count=[1 if(x==y) else 0 for (x,y) in zip(guesses, prizedoors)]
	return sum(map(int, count))/len(count)*100
'''
print(simulate_prizedoor(3))
print(simulate_guess(5))
print(goat_door(np.array([0, 1, 2]), np.array([1, 1, 1])))
print (switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1])))
'''

guess=simulate_guess(1000000)
prizedoor=simulate_prizedoor(1000000)
goatdoor=goat_door(prizedoor,guess)
switch=switch_guess(guess,goatdoor)
print (win_percentage(guess, prizedoor))
print(win_percentage(switch, prizedoor))