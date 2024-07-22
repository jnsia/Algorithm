function solution(num_list) {
    var answer = 0;
    
    let odd = 0
    let even = 0
    
for (let i = 0; i < num_list.length; i++) {
i % 2 != 0 ? odd += num_list[i] : even += num_list[i]
}
    if (odd >= even) {
        answer = odd
    } else if (odd < even) {
        answer = even
    }
    
    return answer;
}