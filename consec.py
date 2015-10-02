consec (node, clength):

    if not node: return 0

    maxlength = clength
    
    for child in node.children:
        if child.val == node.val+1:
            candidateLength = consec(child,clength+1)
        else:
            candidateLength = consec(child,1)
            
        if candidateLength > maxLength: maxLength = candidateLength
        
    return maxLength
    

consec (node, clength):
    return max( consec(child,clength+1) if child.val == node.val+1 else consec(child,1) for child in node)
    
    
x = b if b>y else y
