function solution(sides) {
    var answer = 0;
    
    sides.sort((x, y) => x - y);
    
    for (let i = 0; i < sides[0] + sides[1]; i++) {
        if ( i > sides[1] - sides[0] ) {
            answer += 1
        }
    }
    
    return answer;
}