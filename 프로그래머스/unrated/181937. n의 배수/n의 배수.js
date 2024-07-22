function solution(num, n) {
    var answer = 0;
    
    if (num % n == 0) {
        var answer = 1;
    } else {
        var answer = 0;
    }
    
    return answer;
}