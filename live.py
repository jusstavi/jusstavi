import time

Heart = ["Soukya"]

def live():
	
	if 'Soukya' in Heart:
		breathe()
		
	else:
		print("No reasons to live...")
		
def breathe():
	while True:
		print("Inhaling for you...\n")
		time.sleep(2)
		print("Exhaling for you...\n")
		time.sleep(2)
		

live()
