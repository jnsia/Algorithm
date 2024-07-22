function solution(n) {
    var answer = 0;
    let x = 1
    
    for (let i = 1; i <= 10; i++) {
        x = x * i
        
        if (x > n) {
            answer = i - 1
            
            break
        } else if (x >= n) {
            answer = i
            
            break
        }
    }
    
    return answer;
}