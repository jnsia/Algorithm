function solution(n) {
    var answer = 0;
    
    a = String(n).split('')
    a.forEach(e => answer += Number(e))
    
    return answer;
}