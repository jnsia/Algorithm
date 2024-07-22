function solution(emergency) {
    var answer = [];

    let a = 0
    let i = 0
    let sum = 0
    
    while(a <= emergency.length - 1) {
    emergency.map((key, index) => {
        if (Math.max(...emergency) == key && Math.max(...emergency) != 0) {
            a += 1
            answer[index] = a
            emergency[index] = 0
        }
    })
}
    
    console.log(emergency)
        
    return answer;
}