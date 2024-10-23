import java.util.*;

class Solution {
    class Car {
        String carNum;
        int fee;
        
        Car(String carNum, int fee) {
            this.carNum = carNum;
            this.fee = fee;
        }
    }
    
    public int[] solution(int[] fees, String[] records) {        
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> feeMap = new HashMap<>();
        
        for (String record: records) {
            String[] recordArray = record.split(" ");
            String[] timeArray = recordArray[0].split(":");
            int time = Integer.parseInt(timeArray[0]) * 60 + Integer.parseInt(timeArray[1]);
            
            String carNum = recordArray[1];
            
            if (map.get(carNum) == null) {
                map.put(carNum, time);
            } else {
                int diffTime = time - map.get(carNum);
                feeMap.put(carNum, feeMap.getOrDefault(carNum, 0) + diffTime);
                map.remove(carNum);
            }
        }
        
        for (String carNum: map.keySet()) {
            int time = 23 * 60 + 59;
            int diffTime = time - map.get(carNum);
            
            feeMap.put(carNum, feeMap.getOrDefault(carNum, 0) + diffTime);
        }
        
        List<String> list = new ArrayList<>(feeMap.keySet());
        Collections.sort(list);
        
        int index = 0;
        int[] answer = new int[list.size()];
        
        for (String carNum: list) {
            int time = feeMap.get(carNum);
            
            if (time <= fees[0]) {
                answer[index++] = fees[1];
            } else {
                int unitTime = (int) Math.ceil((double) (time - fees[0]) / fees[2]);
                answer[index++] = unitTime * fees[3] + fees[1];
            }
        }
        
        return answer;
    }
}