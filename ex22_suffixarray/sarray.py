

class SuffixArray(object):

    def __init__(self, instr):
        self.instr = instr
        sfx = []
        for i in range(0, len(instr)):
            sfx.append((self.instr[i:], i))

        self.sarray = sorted(sfx)

    def search(self, what):
        """
        Uses a binary search to find two indexes:
            first is where it is in self.sarray
            second is where is in self.instr
        """

        low = 0
        high = len(self.sarray)

        while low < high:
            mid = (high - low) // 2 + low
            mid_val, starts_at = self.sarray[mid]

            if mid_val == what:
                return mid, starts_at
            elif mid_val > what:
                high = mid
            elif mid_val < what:
                low = mid + 1

        return -1, -1

    def find_shortest(self, match):
        """Easiest is assume exact match of suffix."""
        sarray_i, instr_i = self.search(match)
        return instr_i

    def find_longest(self, match):
        sarray_i, instr_i = self.search(match)
        if sarray_i == -1: return -1, -1

        test, instr_i = self.sarray[sarray_i]
        longest, longest_i = test, instr_i

        while test.startswith(match):
            if len(test) > len(longest):
                longest, longest_i = test, instr_i

            sarray_i += 1

            try:
                test, instr_i = self.sarray[sarray_i]
            except IndexError:
                break

        return longest, longest_i

    def find_all(self, match):
        sarray_i, inst_i = self.search(match)
        if sarray_i == -1: return -1, -1

        test, instr_i = self.sarray[sarray_i]
        results = []

        while test.startswith(match):
            results.append((test, instr_i))
            sarray_i += 1

            try:
                test, instr_i = self.sarray[sarray_i]
            except IndexError:
                break

        return results

