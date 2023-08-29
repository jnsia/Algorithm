function solution(code) {
    var answer = '';
    
    let mode = 0;
    
    for (let idx = 0; idx < code.length; idx++) {
        if (code[idx] == '1') {
            mode == 0 ? mode = 1 : mode = 0
            
            console.log(mode)
        } else if (mode == 0 && idx % 2 == 0) {
            answer += code[idx]
            
            console.log(code[idx])
        } else if (mode == 1 && idx % 2 != 0) {
            answer += code[idx]
            
            console.log(code[idx])
        }
    }
    
    if (answer == '') {
        answer = "EMPTY"
    }
    
    return answer;
}