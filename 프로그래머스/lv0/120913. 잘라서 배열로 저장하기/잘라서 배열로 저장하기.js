function solution(my_str, n) {
    var answer = [];
    
    for (let i = 0; i < my_str.length / n; i++) {
        answer.push(my_str.slice(n * i, n * (i + 1)))
    }
    
    return answer;
}