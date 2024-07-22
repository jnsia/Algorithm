function solution(s){
    var answer = true;
    
    let pCount = 0
    let yCount = 0

    let str = s.toLowerCase()
    
    for (let i = 0; i < str.length; i++) {
        if (str[i] == 'p') {
            pCount += 1
        } else if (str[i] == 'y') {
            yCount += 1
        }
    }
    
    pCount == yCount ? answer=true : answer = false;
    
    return answer
}