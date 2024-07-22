function solution(array) {
    var answer = [];
    
    answer[0] = Math.max(...array)
    
    array.map((key, index) =>
              {if (key == answer[0]) {
            answer[1] = index
    }})
    
    return answer;
}