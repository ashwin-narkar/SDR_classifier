# this module will be imported in the into your flowgraph
# this module will be imported in the into your flowgraph

freq_values = [2412000000.0, 2417000000.0, 2422000000.0, 2427000000.0, 2432000000.0, 2437000000.0, 2442000000.0, 2447000000.0, 2452000000.0, 2457000000.0, 2462000000.0]
currIndex = 0


def sweepFreqs():
	global freq_values
	global currIndex
	currIndex += 1
	if currIndex > len(freq_values):
		currIndex = 0
	return freq_values[currIndex]	
