function solution(num_list) {
    var answer = 0;
    
    let x = 1
    let y = 0
    
    num_list.forEach(e => {
        x *= e
        y += e
    })
    
    if (x < y**2) {
        answer = 1
    }
    
    return answer;
}