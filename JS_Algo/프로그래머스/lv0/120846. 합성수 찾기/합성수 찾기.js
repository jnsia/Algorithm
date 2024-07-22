function solution(n) {
    var answer = 0;
    
    not_prime_num = []
    
    for (let i = 2; i <= n; i++) {
        for (let j = 2; j < i; j++) {
            if (i % j == 0 && !not_prime_num.includes(i)) {
                not_prime_num.push(i)
            }
        }
    }
    
    answer = not_prime_num.length
    
    return answer;
}