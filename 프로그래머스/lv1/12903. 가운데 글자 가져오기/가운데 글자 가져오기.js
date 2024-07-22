function solution(s) {
    var answer = '';
    
    let arr = s.split('')
    
    if (arr.length % 2 != 0) {
        answer = arr[(s.length -1) / 2]
    } else {
        answer = arr[(s.length / 2) - 1] + arr[s.length / 2]
    }
    
    return answer;
}