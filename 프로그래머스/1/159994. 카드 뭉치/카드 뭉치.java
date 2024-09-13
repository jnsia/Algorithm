class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        int goalIndex = 0;
        
        int cards1Index = 0;
        int cards2Index = 0;
        
        while (goalIndex < goal.length) {
            if (cards1Index < cards1.length && goal[goalIndex].equals(cards1[cards1Index])) {
                cards1Index++;
                goalIndex++;
            } else if (cards2Index < cards2.length && goal[goalIndex].equals(cards2[cards2Index])) {
                cards2Index++;
                goalIndex++;
            } else {
                answer = "No";
                break;
            }
        }
        
        return answer;
    }
}