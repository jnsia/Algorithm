function solution(numbers) {
    var answer = 0;
    
    let list = []
    
    for (let i = 0; i < numbers.length; i++) {
        for (let k = 0; k < numbers.length; k++) {
            if (i != k) {
                list.push(numbers[i] * numbers[k])
            }
        }
    }
    
    answer = Math.max(...list)
    
    return answer;
}