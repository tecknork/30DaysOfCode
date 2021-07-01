## anagram 
"""
Input:"aa aa odg dog gdo"
Output:2
Input:"a c b c run urn urn"
Output:1
"""
def CountingAnagrams(strings):
    
    data = strings.split(" ")
    print(set(["".join(sorted(i)) for i in data]))
    
    #strings = tuple("".join(sorted(string)) for string in set(strings.split(" ")))
    #print(strings)
    
    #return len(strings) - len(set(strings))


if __name__ == '__main__':
    a ="aa aa odg dog gdo"
    print(CountingAnagrams(a))