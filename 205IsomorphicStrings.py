'''
create a key/value pair for each character in the primary string (arbitrarilly s)
if a character in s is not new or maps to the corresponding index character of t, return False
after checking every character without fail, return True
'''
def isIsomorphic(self, s: str, t: str) -> bool:
        
        length_s = len(s)
        length_t = len(t)

        if length_s != length_t:
            return False

        else:
            hash_map = {}
            for i in range(0,length_s):
                if s[i] not in hash_map.keys():
                    if t[i] not in hash_map.values():
                        hash_map[s[i]] = t[i]
                    else:
                        return False
                else:
                    if hash_map[s[i]] != t[i]:
                        return False

        return True