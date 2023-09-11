class Solution {
    public String[] solution(String[] strArr) {
        int size = 0;
        
        for (String tmp: strArr) {
            if (size % 2 == 0) {
                strArr[size++] = tmp.toLowerCase();
            } else {
                strArr[size++] = tmp.toUpperCase();
            }
        }
        
        return strArr;
    }
}