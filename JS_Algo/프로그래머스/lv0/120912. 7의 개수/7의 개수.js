function solution(array) {
    var answer = 0;
    
    let str = ''
    
    array.forEach(e => {
        str += String(e)
    })
    
    str.split('').forEach(e => {
        if (e == 7) {
            answer += 1
        }
    })
    
    return answer;
}