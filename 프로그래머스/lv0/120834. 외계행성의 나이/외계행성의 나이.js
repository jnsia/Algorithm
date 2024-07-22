function solution(age) {
    var answer = '';

    let str = []

    let str2 = String(age).split('')
    
    for (let i = 97; i < 123; i++) {
        str.push(String.fromCharCode(i));
    }
    
    for (let k = 0; k < str2.length; k++) {
        answer += str[str2[k]]
    }
    
    
    return answer;
}