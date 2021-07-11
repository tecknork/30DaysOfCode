import itertools as it
def alternate(s):
    
    val = list(s)
    set_val = sorted(set(val),key=val.index)
    alter_str = []
    #print(val)
    #print(set_val)
    
    
    for i in range(len(set_val)+1): 
        permu_val= it.combinations(set_val,i)
        permu_val = set(permu_val)
        print(list(permu_val))
        for valx in permu_val:
            #print(valx)
            #print(valx)
            remove_list = list(filter(lambda a: a not in valx, val))
            
          #  [x for x in val if x not in list(valx)]
            #print(remove_list)
            characters = sorted(set(remove_list),key=remove_list.index)
            if is_alternating_string(remove_list,list(characters)):
                alter_str.append(remove_list)
        alter_str.sort(key=lambda s: len(s),reverse=True)
        # print(alter_str)
        if len(alter_str) > 0: 
            return len(alter_str[0])    
        alter_str = []

    return 0
    

def is_alternating_string(s,chaters): 
   # print(chaters)
    for i in range(len(s)): 
        if s[i] != chaters[i%len(chaters)]: 
            return False
        else: 
            if i>0:
                if s[i-1] == s[i]: 
                    return False
            if (i+1)< len(s):
                if s[i+1] == s[i]: 
                  return False  
   # print(s)
    return True
    
if __name__ == '__main__':
    s = "asvkugfiugsalddlasguifgukvsa"
    print(alternate(s))

    s = "asdcbsdcagfsdbgdfanfghbsfdab"
    # print(alternate(s))

    
    s= "ucwtvajqreigbqszaukfieswtlhdvwhvlzsxswzbfcropnxlektloohamginpsxeooqsnlbaglmhiyednqibglmodhylweshcquhvxtqclqbvmptqglungavqccwlmhhogdlrzufeccpdmwnnrmgcxqlwdvtqqbicqbfgldxgdkkyvpzvlsncotyhwqeilzmguhpyrazsbsfvkzjzabcvrqwqndoqgztxtlpbfjcvbsplvbwlmmuyyqhiknybizxjzmrjvrtrsshgbiidrrcbapdwsxzlzlmcwrtvngokdvywjglorficgxqvatsbnvplqinopcrttpseweeekbypkvdanbcofvziojhpzhzaltgqvpstrrxfrjhdsdhrtwqzcqneicivppiquubsrvvbrtmwyhhqailyaaypfeusuefgqmbxmfadxtznfxfdtqggxeorjpvtmixlykezahzhxjbovglxggwxfcyrfxpefzolryernhmebhvcidocnknucdldlqtfvcoecygvejdrjnfrfrbqagcbellxnodvlzieerarmzrzfrdgxuhcfuwxvjlqmlflciotcylyyeywgtqgmbwghxaqesjgisuarjhqldcvxgyqzkwpecbapxxhevazufbgkrrzgxcnuuqdzzizbethncfhuvfjgccikzkqnksexzdvbhabdbrdspuygmhvmlbsptzejjtqnbdjpnhzamqvwliukpxxvkspgqxkedqcaaqwhglfiteiqnweyyfwswrkitadrayaqpllnnfatktsdlwtggzvjpefjglqbvpkpgtwarolbmsfbqxjsznmlmdohxwuxlasppsmqfcmfggxvimymnyqqoxdljdcyqlleuhfbemkwyysykdnjcazwrjhqpsclzhezqzghsmuzrapkxccniagkzfkntzrufvgqhbkfgyajwczsihigazrwvkdzequtqabdqqixjqudvdkvydknuamcxr"
    # print(alternate(s))

    print(alternate("beabeefeab"))
    #print(is_alternating_string("bcdbcd","bcd"))
    #print(is_alternating_string("ababab","ab"))
   