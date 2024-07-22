function solution(n) {
    var answer = [];
    
    for (let i = 0; i <= n; i++) {
        if (n/i == parseInt(n/i)) {
            answer.push(i);
        }
    }
    
    return answer;
}