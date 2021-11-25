from names_dataset import NameDataset # v2
from names_dataset import NameDatasetV1 # v1

m = NameDataset() # init it only once in your app because the V2 takes much more time to init than the V1.
# The scores are calculated based on the frequencies of the names for a given country. For example, the 
# most popular first name in Morocco is Mohamed so Mohamed will have a score of 100.
# print(m.search_first_name('محمد')) # 100.0

m.search_first_name('Luca') > 1