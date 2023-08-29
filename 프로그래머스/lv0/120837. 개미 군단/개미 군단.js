function solution(hp) {
    var answer = 0;
    
    a = hp % 5
    x = Math.floor(hp / 5)
    
    b = a % 3
    y = Math.floor(a / 3)

    z = b / 1
    
    console.log(a, x, b, y, z)
    
    return answer = x + y + z;
}