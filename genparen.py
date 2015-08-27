def generate(str, opens, closes, n ,answerlist):
        
    #print str, opens, closes
    
    #add to list
    if opens == n and closes == n:
        answerlist.append(str)
        return
    
    #close parend
    if opens > closes and closes < n: generate(str + ")", opens, closes+1, n, answerlist)
    
    #open parend
    if opens < n: generate(str + "(", opens+1, closes, n, answerlist)
    
    
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    answerlist = []
    st = ""
    #self.generate(st,0,0,n,answerlist)
    generate(st,0,0,n,answerlist)
    return answerlist

def combs(n):
    x = 1;
    result = 1;

    while x < n:
        result = result * 3 - 1
        x+=1
    return result
                
        
for x in range(1,20):
    print "n:", x, "parencomb:", len(generateParenthesis(x)), " expected:",  combs(x)