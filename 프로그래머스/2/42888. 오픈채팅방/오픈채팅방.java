import java.util.*;

class Solution {
    public String[] solution(String[] record) {        
        List<String> results = new ArrayList<>();
        Map<String, String> nicknames = new HashMap<>();
        
        for (String temp: record) {
            String[] recordArray = temp.split(" ");
            String command = recordArray[0];
            String uid = recordArray[1];
            
            if (command.charAt(0) == 'E') {
                String nickname = recordArray[2];
                nicknames.put(uid, nickname);
                results.add(command + " " + uid);
            } else if (command.charAt(0) == 'L') {
                results.add(command + " " + uid);
            } else {
                String nickname = recordArray[2];
                nicknames.put(uid, nickname);
            }
        }
        
        int index = 0;
        String[] answer = new String[results.size()];
        
        for (String result: results) {
            String[] resultArray = result.split(" ");
            String command = resultArray[0];
            String uid = resultArray[1];
        
            if (command.charAt(0) == 'E') {
                answer[index++] = nicknames.get(uid) + "님이 들어왔습니다.";
            } else {
                answer[index++] = nicknames.get(uid) + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}