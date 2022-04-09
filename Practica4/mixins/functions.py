from typing import List
from time import time
import matplotlib.pyplot as plot
import math

def dist(p1, p2):
  	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y))


def number_length( num: int ):
  return len(str(num))


def algotithm_time( algorithm, title: str ):
  print( title )
  cpu_time_start = time()
  print( algorithm )
  cpu_time_end_karatsuba = (time() - cpu_time_start) * 1000
  return cpu_time_end_karatsuba


# Graph
def graph_bars(label: List[str], data: List[float], title: str, xlabel: str, ylabel: str):
  plot.bar(label,  data)
  plot.title(title)
  plot.xlabel(xlabel)
  plot.ylabel(ylabel)
  plot.show()
