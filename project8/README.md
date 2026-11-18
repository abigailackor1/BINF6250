# Introduction
In this project our group was tasked with creating and understanding Hidden Markov models by implementing the Viterbi algorithm, which finds the most likely sequence of hidden states for a sequence of observations.

Viterbi decoding is how an HMM turns a long, unlabelled sequence into an annotation. GENSCAN models the structure of human genes (exons, introns, splice sites, untranslated regions) as a probabilistic state machine and reports the most probable gene structure for a stretch of genomic DNA (Burge & Karlin, 1997). Then ChromHMM segments the genome into chromatin states from combinations of histone marks, assigning each region of the genome to a state such as "active promoter" or "repressed" (Ernst & Kellis, 2010, 2012). 

This is a very versatile and extensive tool that is used in many applications of the bioinformatics field to annotate and reconstruct genomic data. 

# Pseudocode

class HMM:
 def __init__(init_probs, trans_probs, emit_probs)
        self.init = init_probs
        self.trans = trans_probs
        self.emit = emit_probs
        self.states = list(emit_probs.keys())
    Allow us to access necasary probabilities. 
    Self.states gives a list of states, where the index of each state in the list is its row in the two matrices. Allows conversion. 

 def viterbi(sequence):
    CREATE probability matrix of the size states * sequence length
    CREATE traceback matrix of the size states * sequence length

    INITIALIZE first row of probability matrix using initial probabilities (only column 0)
    for row number in rows of matrix:
        determine state using self.states
        calculate log prob at that position [row number, 0] and add it to prob matrix: use state, initial/emission probabilities, and the observation (sequence[0])

    ITERATE
    for each remaining column
        get the current observation (sequence[column])

        for each row in that column
            this is the "current position"
            determine state using self.states
            determine what the last column number was
            create a dictionary to store the probabilities of current state and observation coming from a previous state (key)

            for each row in last column
                these are the "past positions"
                determine state using self.states
                get past position's prob value using it's coordinates and prob matrix
                get current prob coming from this past prob: multiply past prob * currrent prob (using tansition and emition probabilities)  
                store prob in dictionary with the past state as the key
            
            get key (last state) of max prob for the current position
            store max prob in prob matrix
            store where it came from (row of last state) in traceback matrix

    TERMINATION
    row with highest prob at end of probability matrix is the predicted ending state

    TRACEBACK
    make list that keeps track of predicted states
    add termination state to list
    set termination state to current state 
    for each column in traceback matrix (except the first):
        using traceback matrix, determine previous state (row) using current state: value stored in traceback matrix at [current state (row), column]
        add previous state to list
        set previous state to current state

# Successes
We were able to create two implementations of an HMM class, the one outlined above and another in alternate.ipynb. The alternate.ipynb uses dictionaries instead of numpy matrices, and takes inpiration form an example seen online (Viterbi Algorithm for Hidden Markov Models (HMMs), 2025). Both our HMM classes have a very similar structure and produce the same results for the "obs" sequence provide. We successed in not hardcoding anything, with the states and probabilites coming from the provided dictionaries. In our standard ipynb, we were also able to use log probabilities. This will help with future projects if we analyze longer sequences. Similarly, we beleive the OOP struture we set up in this project will help us down the line. Finally, our projec08.ipynb identified a 12bp CG repeat in the middle of a second observation as a CpG island, confirming the algorithm's functinoality.

# Struggles
We were not able to implement a few checks mentioned on the canvase page. These include checking that all probabilities in dictionaries add to 1 checking that all states in the dictionaries are the same. We also dont handle the case were an observation has a value that is not in one of the dictionaries. If we are using more complicated data in the next module, these will be necessary to add. 

# Personal Reflections
## Group Leader
This was my first project being a group leader so it was difficult at first for me to understand the steps I needed to take to ensure I was setting my team up for success. However, it was a quick learning curve and I think we did a great job collaborating and building this algorithm. I feel like I have kept developing my skill sets not only with Git but also coding.

## Other 
Jake (Matthew): This project always seemed doable becuase I had a basic understanding of the algorithm after the lecture. I then used the HMM primer (Sherman, 2026) and the powerpoint presentation (Langmead, n.d.) on canvas to help make my understanding more concrete. From here I thought the implementation would be easy, but it ended up being more complicated than I expected. When you are doing something by hand its easy to get the probabilites you need, but then translating this into code can become involved. Getting all the required states and probabilites to do each calculation lead to the 3 nested for loop seen above. Marcus said at the end of class that if you go over 3 nested for loops you have gone to far, so that gave me some confidence 3 was the right number. Also, it was challengeing and interesting using OOP for this project. I used the GffEntry class from the data_readers.py provided script in the Gibbs sampling project as a structural guide. Like the last time, the traceback was confusing at first, but eventually it made sense. Overall, I thought the group made good use of the extra time and we now have a solid foundation for the next 2 projects.

# Generative AI Appendix
As per the syllabus

# Referecnes
1. Langmead, B. (n.d.) *Hidden Markov Models* [PowerPoint slides]. Whiting School of Engineering, Johns Hopkins University. https://www.cs.jhu.edu/~langmea/resources/lecture_notes/23_hidden_markov_models_v2.pdf
2. Sherman, M. D. (2026). *A primer on HMMs: From one picture to five algorithms* [Class handout]. Canvas@NEU. https://canvas.northeastern.edu/
3. Viterbi Algorithm for Hidden Markov Models (HMMs). (2025, July 23). GeeksforGeeks. https://www.geeksforgeeks.org/artificial-intelligence/viterbi-algorithm-for-hidden-markov-models-hmms/
