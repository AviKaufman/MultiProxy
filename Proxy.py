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
        return

    def get_numparts(self):
        return

    def ordered_bitstring(self):
        return

    def combos(self):
        return

    def shannon_all(self):
        return

    def shannon_in(self):
        return

    def shannon_out(self):
        return

    def calculate_proxy(self):
        return

    def set_part(self, part):
        self.part = part
        return
