function solution(babbling) {
    var answer = 0;
    
    let bab = ["aya", "ye", "woo", "ma"]
    let com = []
    let comb = ["aya", "ye", "woo", "ma"]
    
    bab.map((key, index) => {
        for (let i = 0; i < bab.length; i++){
            if (!key.includes(bab[i])) {
                com.push(key + bab[i])
                comb.push(key + bab[i])
            }
        }
    })
    
    com.map((key, index) => {
        for (let i = 0; i < bab.length; i++){
            if (key != bab[i]) {
                comb.push(key + bab[i])
            }
        }
    })
    
    com.map((key, index) => {
        for (let i = 0; i < com.length; i++){
            if (!key.includes(com[i])) {
                comb.push(key + com[i])
            }
        }
    })
    
    
    for (let t = 0; t < comb.length; t++) {
        babbling.forEach(e => {
            if (e === comb[t]) {
                answer += 1
            }
        })
    }
    
    console.log(comb)
    
    return answer;
}