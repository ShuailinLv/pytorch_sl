# from torch.utils.data import Dataset, DataLoader, TensorDataset
import numpy as np 
from typing import List, Tuple, Dict
import os 
import pdb
import abc
# from utils import GetAllFilesInRootFolder

def GetAllFloders(data_path: str) -> List:
		allFolders = []
		dir_files = os.listdir(data_path)
		for i in dir_files:
			if os.path.isdir(data_path + i):
				allFolders.append(data_path  + i + '/')
		return allFolders

def GetAllFilesInOneFolder(data_folder: str) -> List:
	allFiles = []
	file_extend = ['jpg', 'JPG', 'png', 'PNG']
	dir_files = os.listdir(data_folder)
	for i in dir_files:
		if os.path.isfile(data_folder + i) and (i.split('.')[-1] in file_extend):
			allFiles.append(data_folder + i)
	return allFiles

def GetAllFilesInRootFolder(data_root: str) -> List:
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
	return allFiles

class DPData(abc.ABC):
	
	def __init__(self, data_path: str) -> None:
		self._root = data_path
		self._paths = GetAllFilesInRootFolder(data_path)
		for i in self._paths:
			print(i)

	def __len__(self):
		return len(self._paths)

	def __getitem__(self, index: int) -> torch.Tensor:
		return 

temp = DPData('/Users/lvshuailin/pytorch_sl/')

