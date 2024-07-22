function solution(a, b) {
    var answer = 0;
    
    var first = String(a) + String(b);
    var second = String(b) + String(a);
    
    var intFirst = Number(first)
    var intSecond = Number(second)
    
    intFirst > intSecond ? answer = intFirst : answer = intSecond
    
    
    return answer;
}