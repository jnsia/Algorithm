function solution(s1, s2) {
    var answer = 0;
    
    for (let i = 0; i < s1.length; i++) {
       if (s2.includes(s1[i])) {
           answer += 1
           console.log(s1[i])
       } else {
           console.log(s1[i])
           console.log(s2)
       }
    }
    
    return answer;
}