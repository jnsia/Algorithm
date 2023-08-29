function solution(box, n) {
    var answer = 0;
    
    a = Math.floor( box[0] / n )
    b = Math.floor( box[1] / n )
    c = Math.floor( box[2] / n )
    
    return answer = a * b * c;
}