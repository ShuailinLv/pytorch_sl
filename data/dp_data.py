# from torch.utils.data import Dataset, DataLoader, TensorDataset
import numpy as np 
from typing import List, Tuple, Dict
import os 
import pdb
import abc
from utils import GetAllFilesInRootFolder

class DPData(abc.ABC):
	
	def __init__(self, data_path: str) -> None:
		self._root = data_path
		self._paths = GetAllFilesInRootFolder(data_path)
		for i in self._paths:
			print(i)

	def __len__(self):
		return len(self._paths)

	# def __getitem__(self, index: int):
	# 	return 



