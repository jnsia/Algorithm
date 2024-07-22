function solution(n, m) {
    var answer = [];
    
    let gcd = 1
    
    for (let i = 0; i <= Math.min(n, m); i++) {
        if (n % i == 0 && m % i == 0) {
            gcd = i
        }
    }
    
    let lcm = (n * m) / gcd
    
    return [gcd, lcm];
}