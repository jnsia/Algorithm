function solution(my_string) {
    var answer = [];
    
    let str = my_string.split('')
    let str2 = []
    
    str.filter(e => {if (e == parseInt(e)) {
        str2.push(Number(e))
    }})
    
    answer = str2.sort((a, b) => a - b)
    
    return answer;
}