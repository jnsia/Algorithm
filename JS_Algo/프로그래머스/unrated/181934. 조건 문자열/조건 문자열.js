function solution(ineq, eq, n, m) {
    var answer = 0;
    
    if (eq == '=') {
        if (ineq == '>' && n >= m) {
            answer = 1
        } else if (ineq == '<' && n <= m) {
            answer = 1
        } else {
            answer = 0
        }
    } else {
        if (ineq == '>' && n > m) {
            answer = 1
        } else if (ineq == '<' && n < m) {
            answer = 1
        } else {
            answer = 0
        }
    }
    
    
    
    return answer;
}