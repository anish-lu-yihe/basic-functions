# Basic Functions
Here I maintain a handful of basic Python 3 functions, that are useful in multiple projects of mine.
For my study being often theoretical, I am not conern too much about huge tensors and `numpy` is the only dependence for this repository.
I attempt to keep these functions up-to-date with the newest version of Python 3 and `numpy`,
but I cannot promise and thus I choose the MIT license.

## List of functions
* `collapse(probas)`: takes in probabilities and outputs binary states.
* `logistic(x, temperature)`: takes in activations and outputs probabilities, common for artificial neurons.
* `softmax(x, temperature)`: takes in activations and outputs probabilities, when a neural layer has lateral inhibition.
* `entropy(P, base)`: takes in probabilities distributions and outputs their entropy values.

## Selfish but little wish
To those who are more experienced, knowledgeable and/or intelligent in programming than me, 
I sincerely hope that you would leave me any comments for correction and/or improvement, 
or suggest me any existing packages/modules that outperforms mine.
Although I do not care too much about the efficiency,
several of my projects are dependent on them so I need them to be absolutely correct.
In addition, as the functions are used a lot, any tiny improvement could lead to potentially a bigger one.