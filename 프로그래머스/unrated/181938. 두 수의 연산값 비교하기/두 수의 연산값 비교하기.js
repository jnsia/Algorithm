function solution(a, b) {
    var answer = 0;
    
    var first = Number(String(a) + String(b))
    var second = 2 * a * b
    
    first > second ? answer = first : answer = second
    
    return answer;
}