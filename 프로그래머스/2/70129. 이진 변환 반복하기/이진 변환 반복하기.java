class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        int tryCount = 1;
        int removeCount = 0;
        
        while (true) {
            // 원래 길이를 측정한다.
            int originLength = s.length();
            
            // 제거할 0의 개수를 먼저 확인한다.
            int zeroCount = 0;
            
            // 0의 개수를 구한다.
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    zeroCount++;
                    removeCount++;
                 };
            }
            
            // 0 제거 후 길이를 측정한다.
            int afterLength = originLength - zeroCount;
            
            // 0 제거 후 길이를 이진법으로 변환한다.
            String binaryResult = "";
            
            while (afterLength > 0) {
                if (afterLength % 2 == 0) {
                    binaryResult = "0" + binaryResult;
                } else {
                    binaryResult = "1" + binaryResult;
                }
                
                afterLength = afterLength / 2;
            }
            
            // 이진법 변환 결과가 "1"인지 판단한다.
            if (binaryResult.equals("1")) {
                break;
            } else {
                // 결과가 "1"이 아니라면 s에 이진 변환 결과를 대입하고
                s = binaryResult;
                // 한 번 더 while 문을 수행한다.
                tryCount++;
            }
        }
        
        answer[0] = tryCount;
        answer[1] = removeCount;
        
        return answer;
    }
}