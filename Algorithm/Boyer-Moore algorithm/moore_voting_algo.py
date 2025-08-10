def moore_voting_algo(nums:List(Any)):
    candidate = None
    count= 0 
    for n in nums:
        if count== 0:
            candidate = n 
            count=1
        elif candidate ==n :
            count+=1
        else:
            count-=1
    
    count=0
    for n in nums:
        if n == candidate:
            count+=1
    
    if count > len(nums)//2:
        return candidate 
    else:
        return None 
                    
                    
        