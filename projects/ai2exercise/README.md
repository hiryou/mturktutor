# ai2exercise
Interprets an already processed HIT result

## Setup and run
```bash
# Execute setup.sh bash script which will install virtualenv and download required python modules.
sudo chmod +x ./setup.sh
sudo ./setup.sh
# That's it! Now you can run the program. For simplicity results are printed to console.
python progarm.py
```

## Problem
AI2 wants to acquire training data for coreference on biology text. The coreference task identifies when words refer to the same thing, or entity. For example, here is a biology paragraph and the coreference clusters we would like to identify from it:
 
"The Golgi apparatus, also known as the Golgi complex, Golgi body, or simply the Golgi, is an organelle found in most eukaryotic cells. It was identified in 1897 by the Italian scientist Camillo Golgi and named after him in 1898."

Cluster 1: {Golgi, Golgi complex, Golgi body, an organelle, It}
Cluster 2: {Camillo Golgi, him}

Additionally we need character offsets for each word in a cluster.

## Code Exercise 

Write a script in the language of your choice that processes [this file](https://gist.github.com/schmmd/c4fbc9f80dd23f7d25e463cbe653e68b) from the [ConLL 2012 shared task](http://conll.cemantix.org/2012/data.html). The script should count average number of distinct entities per sentence, where each distinct entity has a unique coref id. It should also find the sentence with the largest number of words (or multiple, if there is a tie).
