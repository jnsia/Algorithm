function solution(array, n) {
    var answer = 0;
    
    array.forEach(e => {if (e == n) {
        answer += 1
    }})
    
    return answer;
}