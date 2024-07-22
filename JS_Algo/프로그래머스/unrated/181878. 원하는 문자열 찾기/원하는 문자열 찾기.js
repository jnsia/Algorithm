function solution(myString, pat) {
    let answer = 0;
    
    let a = myString.toLowerCase()
    let b = pat.toLowerCase()

    let arr = a.split(b)
    
    console.log(arr)
    
    if (arr.length > 1) {
        answer = 1;
    }
    
    return answer
}