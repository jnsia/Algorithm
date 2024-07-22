function solution(i, j, k) {
    var answer = 0;
    
    let result = ''
    
    for (let x = i; x <= j; x++) {
        result += String(x)
    }
    
    result.split('').forEach(e => {
        if (e == `${k}`) {
            answer += 1
        }
    })
    
    return answer;
}