function solution(array) {
    var answer = 0;

    for (let k = 0; k < array.length; k++) {
    for (let i = 1; i < array.length; i++) {
        if (array[i - 1] > array[i]) {
            let temp1 = array[i - 1]
            let temp2 = array[i]
            
            array[i] = temp1
            array[i - 1] = temp2
        }
    }
    }
    
    return answer = array[(array.length - 1) / 2]
}