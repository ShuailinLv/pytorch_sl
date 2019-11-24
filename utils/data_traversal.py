import os
__all__ = ['GetAllFilesInRootFolder']

def GetAllFloders(data_path: str) -> None:
		allFolders = []
		dir_files = os.listdir(data_path)
		for i in dir_files:
			if os.path.isdir(data_path + i):
				allFolders.append(data_path  + i + '/')
		return allFolders

def GetAllFilesInOneFolder(data_folder: str) -> None:
	print(data_folder)
	allFiles = []
	file_extend = ['jpg', 'JPG', 'png', 'PNG']
	dir_files = os.listdir(data_folder)
	for i in dir_files:
		if os.path.isfile(data_folder + i) and (i.split('.')[-1] in file_extend):
			allFiles.append(data_folder + i)
	return allFiles

def GetAllFilesInRootFolder(data_root: str) -> None:
	allFolders = GetAllFloders(data_root)
	allLists = []
	for folder in allFolders:
		temp = GetAllFilesInOneFolder(folder)
		if len(temp): 
			allLists.append(temp)
	allFiles = []
	for item in allLists:
		for file in item:
			allFiles.append(file)
	list.sort(allFiles)
	return allFiles

