function solution(n) {
    var answer = 0;
    
    let arr = []
    
    for (let i = 0; i < 1000; i++) {
        if (i / 3 == parseInt(i / 3) || String(i).split('').includes('3')) {
            
        } else {
            arr.push(i)
        }
    }
    
    return answer = arr[n - 1];
}