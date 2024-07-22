function solution(chicken) {
    var answer = 0;
    
    for (let i = 0; i < 6; i++) {
        answer += (chicken / 10**i)
    }
    
    return Math.floor(answer / 10);
}