function solution(id_pw, db) {
    var answer = '';
    
    db.forEach(e => {
        if (id_pw[0] != e[0]) {
            answer = "fail"
        } else if (id_pw[0] == e[0] && id_pw) {
            id_pw[1] == e[1] ? answer = "login" : answer = "wrong pw"
        }
    })
    
    for (let i = 0; i < db.length; i++) {
        if (id_pw[0] != db[i][0]) {
            answer = "fail"
        } else if (id_pw[0] == db[i][0]) {
            if (id_pw[1] == db[i][1]) {
              answer = "login"
                
                break;
            } else {
                answer = "wrong pw"
                
                break;
            }
        }
    }
    
    return answer;
}