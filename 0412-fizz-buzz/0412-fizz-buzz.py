class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = [] 
        for i in range(1,n+1):
            t = str(i)
            if i%15==0:
                t = "FizzBuzz"
            elif i%5==0:
                t = "Buzz"
            elif i%3==0:
                t = "Fizz"
            answer.append(str(t))
        
        return answer
        