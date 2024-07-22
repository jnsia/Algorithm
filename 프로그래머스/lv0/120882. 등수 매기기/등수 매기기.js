function solution(score) {
    var answer = [];
    
    let arr = []
    let sorted = [];
    let str = ''
    let map = []
    let strArr = []
    
    score.forEach(e => {
        arr.push((e[0] + e[1]) / 2)
    })
    
    sorted = [...arr].sort((x, y) => y - x)
    
    sorted.map((k, v) => {
        str += v
        map.push(k)
    })
    
    for (let i = 0; i < map.length; i++) {
        if (map[i] == map[i - 1]) {
           str = str.replace(str[i], str[i - 1])
        }
    }
    
    strArr = str.split('')
    
    console.log(map)
    console.log(strArr)
    console.log(arr)
    
    arr.forEach(e => {
        for (let i = 0; i < map.length; i++) {
            if (e == map[i]) {
                answer.push(Number(strArr[i]) + 1)
                
                if (map[i] == map[i + 1]) {
                    answer.pop()
                }
            }
        }
    })

    return answer;
}