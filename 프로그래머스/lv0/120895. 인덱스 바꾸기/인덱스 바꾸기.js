function solution(my_string, num1, num2) {
    var answer = '';
    
    let str = my_string.split('')
    let c = str[num1]
    str[num1] = str[num2]
    str[num2] = c
    
    str.forEach(e => answer += e)
    
    return answer;
}