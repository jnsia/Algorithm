function solution(n) {
    var answer = 0;
    
    strArr = String(n).split('')
    numArr = []
    strArr.forEach(e => {
        numArr.push(parseInt(e))
    })
    numArr.sort()
    answer = ''
    while (numArr.length != 0) {
        answer += numArr.pop()
    }
    answer = parseInt(answer)
    
    return answer;
}