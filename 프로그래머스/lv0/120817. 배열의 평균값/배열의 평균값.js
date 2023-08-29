function solution(numbers) {
    var answer = 0;
    
    numbers.forEach((e) => answer += (e / numbers.length))
    
    return answer;
}