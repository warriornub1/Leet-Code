import collections

def groupAnagrams(strs):
    
    hashmap = {}
    for word in strs:
        key = [0] * 26
        for alpha in word:
            key[ ord(alpha) - ord('a') ] += 1
        
        key = tuple(key)
        if key not in hashmap.keys():
            hashmap[ key ] = [word]
        else:
            hashmap[key].append(word)
    
    return list(hashmap.values())

def groupAnagrams1(strs):
    
    ans = {}
    
    for word in strs:
        sorted_str = "".join(sorted(word))
        if sorted_str in ans:
            ans[sorted_str].append(word)
        else:
            ans[sorted_str] = [word]
        
    return ans.values()
        
groupAnagrams( ["eat","tea","tan","ate","nat","bat"] )