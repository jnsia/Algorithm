function solution(n) {
    var answer = 0;

    for (var x = 0; x < 1000000; x++) {
        if (n % x == 1) {
            return answer = x;
        }
    }
    
    return answer;
}