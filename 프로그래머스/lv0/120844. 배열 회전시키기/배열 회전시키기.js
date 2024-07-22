function solution(numbers, direction) {
    var answer = [];

    let start = numbers[0]
    let end = numbers[numbers.length - 1]
    
    if (direction == 'right') {
        for (let i = numbers.length; i > 0; i--) {
            numbers[i] = numbers[i-1]
            }
        
        numbers.pop()
        numbers[0] = end
        
        console.log(numbers)
        
        } else if (direction == 'left') {
            for (let k = 0; k < numbers.length; k++) {
                numbers[k] = numbers[k + 1] 
            }
            
            numbers[numbers.length - 1] = start
        }
    
    return answer = numbers;
}