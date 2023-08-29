function solution(dot) {
    var answer = 0;
    
    const [x, y] = dot

    if (x > 0) {
        y > 0 ? answer = 1 : answer = 4
    } else {
        y > 0 ? answer = 2 : answer = 3
    }
    
    return answer;
}