function solution(my_string, overwrite_string, s) {
    var answer = '';
    
    var x = s + overwrite_string.length
    
    my_string[s].replace(overwrite_string[0])
    
    for (var i = 0; i < x; i++) {
        if (i < s) {
            answer = answer + my_string[i]
        } else {
            answer = answer + overwrite_string
            
            break;
        }
    }
    
    if (my_string.length != x) {
        for (var k = x; k < my_string.length; k++) {
            answer = answer + my_string[k]
        }
    }

    return answer;
}