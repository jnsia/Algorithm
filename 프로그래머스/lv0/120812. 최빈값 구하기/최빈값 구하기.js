function solution(array) {
    var answer = 0;
    
    cnt_arr = []
    
    for (let i = 0; i <= Math.max(...array); i++) {
        cnt_arr.push(0)
    }
    
    for (num of array) {
        cnt_arr[num] += 1
    }
    
    console.log(cnt_arr)
    let same_cnt = 0
    let mx = 0
    
    for (let idx = 0; idx <= cnt_arr.length; idx++) {
        if (mx < cnt_arr[idx]) {
            mx = cnt_arr[idx]
            answer = idx
            same_cnt = 0
        } else if (mx == cnt_arr[idx]) {
            same_cnt += 1
        }
    }
    console.log(mx)
    console.log(same_cnt)
    
    if (same_cnt > 0) {
        return -1
    }
    
    return answer;
}