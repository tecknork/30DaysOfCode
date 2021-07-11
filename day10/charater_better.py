import itertools as it 

def alternate(s):
    val = list(s)
    set_val = sorted(set(val),key=val.index)
    permu_val= it.combinations(set_val,2)
    permu_val = sorted(set(permu_val))
    max_ = 0 
    for i_set in permu_val: 
        if val.index(i_set[0]) < val.index(i_set[1]):
            ind = 0
        else: 
            ind = 1 
        count = 0 
        for s in val:
            if s in i_set:  
                if s == i_set[ind]:
                    count += 1 
                    ind = ind ^ 1 
                else: 
                    count =0 
                    break 
        max_ = max(max_,count)    
    
    return max_ 
    
    
    

if __name__ == '__main__':
    s = "asvkugfiugsalddlasguifgukvsa"
    print(alternate(s))

    s = "asdcbsdcagfsdbgdfanfghbsfdab"
    print(alternate(s))

    s= "ucwtvajqreigbqszaukfieswtlhdvwhvlzsxswzbfcropnxlektloohamginpsxeooqsnlbaglmhiyednqibglmodhylweshcquhvxtqclqbvmptqglungavqccwlmhhogdlrzufeccpdmwnnrmgcxqlwdvtqqbicqbfgldxgdkkyvpzvlsncotyhwqeilzmguhpyrazsbsfvkzjzabcvrqwqndoqgztxtlpbfjcvbsplvbwlmmuyyqhiknybizxjzmrjvrtrsshgbiidrrcbapdwsxzlzlmcwrtvngokdvywjglorficgxqvatsbnvplqinopcrttpseweeekbypkvdanbcofvziojhpzhzaltgqvpstrrxfrjhdsdhrtwqzcqneicivppiquubsrvvbrtmwyhhqailyaaypfeusuefgqmbxmfadxtznfxfdtqggxeorjpvtmixlykezahzhxjbovglxggwxfcyrfxpefzolryernhmebhvcidocnknucdldlqtfvcoecygvejdrjnfrfrbqagcbellxnodvlzieerarmzrzfrdgxuhcfuwxvjlqmlflciotcylyyeywgtqgmbwghxaqesjgisuarjhqldcvxgyqzkwpecbapxxhevazufbgkrrzgxcnuuqdzzizbethncfhuvfjgccikzkqnksexzdvbhabdbrdspuygmhvmlbsptzejjtqnbdjpnhzamqvwliukpxxvkspgqxkedqcaaqwhglfiteiqnweyyfwswrkitadrayaqpllnnfatktsdlwtggzvjpefjglqbvpkpgtwarolbmsfbqxjsznmlmdohxwuxlasppsmqfcmfggxvimymnyqqoxdljdcyqlleuhfbemkwyysykdnjcazwrjhqpsclzhezqzghsmuzrapkxccniagkzfkntzrufvgqhbkfgyajwczsihigazrwvkdzequtqabdqqixjqudvdkvydknuamcxr"
    print(alternate(s))

    #print(alternate("beabeefeab"))
    #print(is_alternating_string("bcdbcd","bcd"))

