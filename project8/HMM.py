class HMM:
    """Class for HMM

        Attributes:
        init_probs (dictionary): initial probabilities (probability of starting in each state) 
        trans_probs (dictionary): transition probabilities (probability of moving from one state to another)
        emit_probs (dictionary): emission probabilities (probability of observing a symbol in a given state)


        probability_matrix (numpy matrix): observations x state (max probability of that observation given previous and state)
        traceback_matrix (numpy matrix): observations x state (where the max probability for that observation came from)
    """
    """
    letters(string)
    for number in range(len(string))
        dictionary = {}
        dictrionary[number] = letter



    1: A, 2: A

    probability_matrix

    state_number = trans_probs.keys()

    matrix = np.array(state_number,len(seq)) 

    for column in range(len(sequence))
        for i in observed states
            if column == 0
                matrix[1,1] = initial prob I
                matrix[1,2] = intirial prob G
            else:
                if row == 1
                    state = "I"
                else
                    state = "G"
                letter = dictrionary[column] 
                if state == "I":
                    prob_1 = matrix[row, column -1] *
                    
                    




      A     A     A     C     C     C     C    A     A 
    I 0.2  0.014
    G 0.8

        0.2 * 0.7 * 0.1 = 
        0.8 * 0.1 * 0.3 = 
    
    # Example initial probabilities (probability of starting in each state)
    init_probs = {
        "I": 0.2,
        "G": 0.8
    }

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "I": {"I": 0.7, "G": 0.3},
        "G": {"I": 0.1, "G": 0.9}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
        "G": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}
    }


    for observed states, initialize by -1

    """



    """
    def __viterbi__(self, observation):

    """



    pass










# Example class from Gibbs sampling
class GffEntry:
    """Main class for handling GFF entries
    
    Truncates the GFF entry to required data only. Also, class is totally ordered.
    This means that comparison operators can be used on GffEntry objects
    
    Attributes:
        seqid (str): The contig that the GFF entry is associated with
        type (str): The type of object that the GFF entry classifies as
        start (int): The left-most nucleotide position of the GFF entry relative to seqid (1-indexed)
        end (int): The right-most nucleotide position of the GFF entry relative to seqid (1-indexed)
        strand (str): Whether the entry is on the forward (+), backward (-) strand or N/A (.)
    """
    
    slots = 'seqid type start end strand'.split()
    
    def __init__(self, args):
        """Initialize the object.
        
        Aggregates all GFF entry columns, and selectively assigns them to attributes
        
        Args:
            args (list): the complete stripped and split GFF entry line
        """
        self.seqid = args[0]
        self.type = args[2]
        self.start = int(args[3])
        self.end = int(args[4])
        self.strand = args[6]
    
    def __str__(self):
        """Determines how GffEntry appear when `print()` is called on them"""
        return f'{self.seqid}\t{self.type}\t{self.start}\t{self.end}\t{self.strand}'
    
    def __len__(self):
        """Determines how GffEntry reports when `len()` is called on them"""
        return self.end - self.start

    def __eq__(self, other):
        self_check = (self.seqid, self.type, self.start, self.end, self.strand)
        other_check = (other.seqid, other.type, other.start, other.end, other.strand)
        if  self_check == other_check:
            return True
    
    def __lt__(self, other):
        if self.seqid < other.seqid:
            return True
        elif self.seqid == other.seqid:
            if self.start < other.start:
                return True
            elif self.start == other.start:
                if self.end < other.end:
                    return True