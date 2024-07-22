function solution(order) {
    var answer = 0;
    
    let tsn = [3, 6, 9]
    
    String(order).split('').forEach(e => {
        if (e == 3 || e == 6 || e == 9) {
            answer += 1
        }
    })
    
    return answer;
}