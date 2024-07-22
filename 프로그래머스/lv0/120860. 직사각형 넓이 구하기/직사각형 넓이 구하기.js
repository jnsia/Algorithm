function solution(dots) {
    var answer = 0;

    let x = 0
    let y = 0
    
    for (let i = 0; i < dots.length; i++) {
        for (let k = 0; k < dots.length; k++) {
            if (dots[i][1] == dots[k][1] && i > k) {
                x = dots[i][0] - dots[k][0]
            }
    
            if (dots[i][0] == dots[k][0] && i > k) {
                y = dots[i][1] - dots[k][1]
            }        
        }   
    }
    
    
    return answer = -x * y;
}