function solution(arr) {
    var answer = 0;
    var sum = 0;
    
    for (var i = 0; i < arr.length; i++) {
        var sum = sum + arr[i];
    }
    
    var answer = sum / arr.length
    
    return answer;
}