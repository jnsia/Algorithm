function solution(my_string, n) {
    var answer = '';
    
    let arr = my_string.split('')
    
    for (let i = 0; i < n; i++) {
        answer += arr[i]
    }
    
    return answer;
}