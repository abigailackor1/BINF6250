class HMM:
    """Class for HMM

        Attributes:
        init_probs (dictionary: initial probabilities (probability of starting in each state) 
        trans_probs (dictionary): transition probabilities (probability of moving from one state to another)
        emit_probs (dictionary): emission probabilities (probability of observing a symbol in a given state)

        probability_matrix (numpy matrix): observations x state (max probability of that observation given previous and state)
        traceback_matrix (numpy matrix): observations x state (where the max probability for that observation came from)
    """

    """
    def viterbi(self, observation):

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