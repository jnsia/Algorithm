function solution(number) {
    var answer = 0;
    
    let a = number.split('')
    
    a.forEach((e) => {
        answer += Number(e)
    })
    
    console.log(answer)
    
    answer = answer % 9
    
    return answer;
}