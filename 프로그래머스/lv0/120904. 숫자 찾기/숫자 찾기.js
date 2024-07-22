function solution(num, k) {
    var answer = 0;
    
    let arr = String(num).split('')
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == k) {
            answer = i + 1
            
            break
        } else {
            answer = -1
        }
    }
    
    return answer;
}