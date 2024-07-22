function solution(str1, str2) {
    var answer = 0;
    
    str1.split(str2).length > 1 ? answer = 1 : answer = 2
    
    return answer;
}