function solution(my_string) {
    var answer = '';
    
    let a = my_string.toLowerCase().split("").sort()
    console.log(a.join(''))
    
    return a.join('');
}