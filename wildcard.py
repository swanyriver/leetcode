def wildcard(wild):
    results = [""]

    i = 0

    while i<len(wild):
        j=i
        while i<len(wild) and wild[i] != '?': i+=1
        
        for x in range(len(results)): results[x] +=wild[j:i]

        if i<len(wild):
            length = len(results)
            for i in range(length):
                results.append(results[i]+'1')
                results[i] +='0'

        print "append: ",wild[j:i], "  ", results

        i+=1


    return results

print wildcard("01??01")


