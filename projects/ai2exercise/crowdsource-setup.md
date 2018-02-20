## Problem
AI2 wants to acquire training data for coreference on biology text. The coreference task identifies when words refer to the same thing, or entity. For example, here is a biology paragraph and the coreference clusters we would like to identify from it:
 
"The Golgi apparatus, also known as the Golgi complex, Golgi body, or simply the Golgi, is an organelle found in most eukaryotic cells. It was identified in 1897 by the Italian scientist Camillo Golgi and named after him in 1898."

Cluster 1: {Golgi, Golgi complex, Golgi body, an organelle, It}
Cluster 2: {Camillo Golgi, him}

Additionally we need character offsets for each word in a cluster.

## Questions & Answers 

#### How to set up this crowdsourcing task: technologies, componenets, etc?
1. Technology: we can use AWS and utilize Amazon Mechanical Turk marketplace to outsource this work. 
2. Summary of setup and components:
   * Split the whole text into paragraphs. Each paragraph is one HIT task.
   * Pay incentive per HIT: Easy rule is to make the pay proportional to simple word count in the paragraph.
   * For each HIT/paragraph, build a fancy html/javascript code which allows mturk worker to easily select a text and label entity for it. Details are explained below.   

#### Describe an example HIT
The crucial success of a HIT task is the html/javascript code. The more intuitive and easier to use, the more correct results workers can produce.

Description of a HIT task: as reminder, each HIT task is 1 paragraph:
1. Javascript main variables: 
    * A variable to hold a list of currently created distinct entity (created by the worker). It's initialized to empty.
    * Another variable to map each distinct entity to a list of text and its index in the paragraph as a string.
2. Upon the event the worker highlights a text (could be one word or consecutive words), a tooltip title "Is this entity same as..." pops up. Below is a list of:
    * (1) Top item is a textbox pre-filled with the selected text itself, followed by an "+" (add new) button titled "New entity". Implication: if the worker thinks this is a new entity so far, she should choose this option. She can change the text to interpret how she wants to keep track of this entity.
    * Followed below is a list of already added entities. Each of this item has 2 fancy UI functions:
        * on-hover: if the worker hovers on an entity, all texts mapped to that entity are highlighted.
        * "-" button to remove: the worker can click this to remove a created entity, which will deallocate all the mapped texts. There will be a simple prompt to ask the worker to confirm this intention. Eventually if removal is the choice, the worker would have to re-cluster some or all of the deallocated texts.
        * This list of distinct entities is sorted alphabetically for easy lookup purpose.
    * If the worker opts to create a new entity, it's added to the list explained above.
3. Some simply UI validation:
    * Highlighted text should not contains any punctuation: [.,!?]
    * But be smart about popular prefix/suffix such as "Mr. Brown"
    