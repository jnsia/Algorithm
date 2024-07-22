function solution(n) {
    var answer = 0;
    
    for (let i = 1; i > 0; i++) {
        if (( i * 6 ) % n == 0) {
            answer = i
            
            break
        }
    }
    
    return answer;
}