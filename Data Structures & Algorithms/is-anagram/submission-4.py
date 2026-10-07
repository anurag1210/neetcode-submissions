class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={} #Initialize a dictionary

        for c in s.lower():
            counts[c]=counts.get(c,0)+1
        for c in t.lower():
            counts[c]=counts.get(c,0)-1

        return all (v==0 for v in counts.values())
