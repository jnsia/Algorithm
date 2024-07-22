function solution(s) {
    var answer = '';
    
    let strArr = s.split(' ')
    let numArr = []
    
    console.log(strArr)
    
    strArr.forEach(e => {
        numArr.push(Number(e))
    })
    
    console.log(numArr)
    
    answer = String(Math.min(...numArr)) + ' ' + String(Math.max(...numArr))
    
    return answer;
}