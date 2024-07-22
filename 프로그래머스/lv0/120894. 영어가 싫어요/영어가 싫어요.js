function solution(numbers) {
    var answer = '';
    
    let arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for (let i = 0; i < arr.length; i++) {
        if(numbers.includes(arr[i])) {
            numbers = numbers.replaceAll(arr[i], i)
        }
    }
    
    return answer = Number(numbers);
}