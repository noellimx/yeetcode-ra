def solution(A):
  qualified_elems = []
  i = 0 
  while i < len(A):
    
    if i == len(A) - 1:
      if 0 not in qualified_elems and (A[0] + A[i]) % 2 == 0:
        qualified_elems += [i, 0]
        
      break
    elif (A[i] + A[i+1]) % 2 == 0:
      qualified_elems += [i, i+1]
        
      i += 2
    else: 
      print('no')
      i += 1
  
  return len(qualified_elems)/2
print(solution([14,21,16, 35, 22]))