function solution(array, n) {
    var answer = 0;
    
    for (let i = 0; i < 100; i++) {
        if (array.includes(n - i)) {
            answer = n - i
                
            break
        } else if (array.includes(n + i)) {
            answer = n + i
                
            break
        }
    }
    
    return answer;
}