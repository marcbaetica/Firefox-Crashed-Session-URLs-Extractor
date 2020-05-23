#script for extract urls from a recovery.jsonlz4_converted.json file after Firefox crashed and corrupted data would not allow the session to restart
#instructions: add file in the same folder location as script and run it
#processes a list of tab urls for the windows that were not closed and another list of tab urls for windows that were marked as closed (some are common due to the data corruption causing the session to not recover)
#outputs:
# - the tab number for each window as it is processed (logged for debugging purposes)
# - a sets of (therefore unique) items representing the tabs that were open at the time of forced browser shutdown
# - a sets of (therefore unique) items representing the tabs that were closed at the time of forced browser shutdown (there is overlap between the set above and this one due to the data coruption)
# - a list of duplicate items found among open tabs
# - a list of duplicate items found among closed tabs
# - finally, and most importantly, an alphabetically sorted list of all tabs representing the union between the two sets. All items in this list are unique

import json

openTabs, closedTabs = set(), set();
duplicateOpenTabs, duplicateClosedTabs = [], [];

def loadFile(fileName):
	#returns a file descriptor (a pointer to a location)
	fileDesc = open(fileName, encoding="utf8"); #decoder.. otherwise defaults to utf16 or utf32 (if some characters show up but are not legible)
	content = fileDesc.read();
	jsonContentLoaded = json.loads(content); #load string instead of load. Also converts to JSON format (in the form of the dict). Objects are opened using ['state'] or [0] if array of jsons.
	# len(obj), obj.keys(), obj.values() and obj.items() are used for inspecting the first layer and choosing where to drill down next
	fileDesc.close();
	return jsonContentLoaded;

def extractWindows(json):
	jsonContentBase = jsonContent['windows'][0]['tabs'][0]['formdata']['id']['sessionData'];
	#this is where it splits as duplicate (will have to verify that the second one is the same as the first)
	windows = jsonContentBase['windows'];
	closedWindows = jsonContentBase['_closedWindows'][0]['_closedTabs'][0]['state']['formdata']['id']['sessionData']['windows'][0]['_closedTabs'][0]['state']['formdata']['id']['sessionData']['windows'];
	print(f"There are a total of {len(windows)} window(s) and {len(closedWindows)} closed window(s).");
	return windows, closedWindows;

def getTabsFromWindow(window):
	print(window.keys());
	for i in range(len(window['tabs'])):
		print(str(i));
		if len(window['tabs'][i]['entries'])==0:
			print('Nothing to print. Entry has been damaged.');
		else:
			title = window['tabs'][i]['entries'][0]['title'];
			url = window['tabs'][i]['entries'][0]['url'];
			#print(title);
			#print(url);
			if url in openTabs:
				duplicateOpenTabs.append(url)
			openTabs.add(url);

def getTabsFromClosedWindow(window):
	for i in range(len(window['tabs'])):
		print(str(i));
		if len(window['tabs'][i]['entries'])==0:
			print('Nothing to print. Entry has been damaged.');
		else:
			title = window['tabs'][i]['entries'][0]['title'];
			url = window['tabs'][i]['entries'][0]['url'];
			#print(title);
			#print(url);
			if url in closedTabs:
				duplicateClosedTabs.append(url);
			closedTabs.add(window['tabs'][i]['entries'][0]['url']);



#----main----
jsonContent = loadFile("recovery.jsonlz4_converted.json");
windows, closedWindows = extractWindows(jsonContent);

#getTabsFromWindow(windows[8]); #for window 9
#getTabsFromClosedWindow(closedWindows[4]); #for window 5

for i in range(10):
	print(f'WINDOW {i+1}');
	getTabsFromWindow(windows[i]);

for i in range(9):
	print(f'WINDOW {i+1}');
	getTabsFromClosedWindow(closedWindows[i]);

allTabsSet = openTabs.union(closedTabs)
allTabsList = list(allTabsSet) #need conversion to list as sets are not sortable
allTabsList.sort()




#Printing parsed and processed data:

#diffTabs = openTabs.difference(closedTabs);
#print(f'\nDIFF TABLS: {diffTabs}');

print(f'\nTabs maked as Open (no repetition): {openTabs}')
print(f'Tabs marked as Closed (no repetition): {closedTabs}')

print(f'\nDuplicate items in Open windows: {duplicateOpenTabs}');
print(f'Duplicate items in Closed windows: {duplicateClosedTabs}');
#getTabsFromWindow(windows[5]); #print(len(window['tabs'])); #715 for window 5 but craps out at 140


print('\nFull list of tabs:')
for val in allTabsList:
	if "newtab" not in val:
		print(val)