class Proxy:
    def __init__(self, bitstrings, qdit, configurations, part):
        self.bitstrings = bitstrings
        self.qdit = qdit
        self.configurations = configurations
        self.part = part
        self.numatoms = None
        self.numparts = None
        self.shannon_all = None

    def get_numatoms(self):
        # Method to get the number of atoms
        return

    def get_numparts(self):
        # Method to get the number of parts
        return

    def ordered_bitstring(self):
        # Method to get the ordered bitstring
        return

    def combos(self):
        # Method to get the combinations
        return

    def shannon_all(self):
        # Method to calculate Shannon entropy for the entire system
        return

    def shannon_in(self):
        # Method to calculate Shannon entropy for the in subsytem
        return

    def shannon_out(self):
        # Method to calculate Shannon entropy for out subsytem
        return

    def calculate_proxy(self):
        # Method to calculate the proxy
        return

    def set_part(self, part):
        # Method to set the part attribute
        self.part = part
        return
