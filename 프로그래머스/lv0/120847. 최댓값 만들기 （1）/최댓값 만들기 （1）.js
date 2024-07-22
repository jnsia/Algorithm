function solution(numbers) {
    var answer = 0;
    
    a = Math.max(...numbers)

    numbers.sort((x, y) => x - y)
    numbers.pop()
    
    b = Math.max(...numbers)
    
    answer = a * b
    
    return answer;
}