class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        hash_map_s={}
        hash_map_t={}

        for i in range(len(s)):
            hash_map_s[s[i]]=1+hash_map_s.get(s[i],0)
            hash_map_t[t[i]]=1+hash_map_t.get(t[i],0)
        return hash_map_s == hash_map_t

        