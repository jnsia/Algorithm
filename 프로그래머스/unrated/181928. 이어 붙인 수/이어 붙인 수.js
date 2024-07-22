function solution(num_list) {
    var answer = 0;
    
    let a = ''
    let b = ''
    
    num_list.filter(e => {
        e % 2 != 0 ? a += e : b += e
    })
    
    return answer = Number(a) + Number(b);
}