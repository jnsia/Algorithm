import java.util.*;

class Solution {
    
    static int result = 0;
    static Set<Set<String>> allSet = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;

        List<String> bannedIds = new ArrayList<>();
        
        for (String banned: banned_id) {
            // if (bannedIds.contains(banned)) continue;
            bannedIds.add(banned);
        }
        
        Set<String> set = new HashSet<>();
        recursion(0, set, user_id, bannedIds);
        answer = allSet.size();
        
        return answer;
    }
    
    private void recursion(int index, Set<String> set, String[] user_id, List<String> bannedIds) {
        if (index == bannedIds.size()) {
            allSet.add(set);
            return;
        }
        
        String banned = bannedIds.get(index);
        
        for (String user: user_id) {
            if (!set.contains(user) && check(user, banned)) {
                Set<String> newSet = new HashSet<>(set);
                newSet.add(user);
                recursion(index + 1, newSet, user_id, bannedIds);
            }
        }
    }
    
    private Boolean check(String user, String banned) {
        if (user.length() != banned.length()) return false;
        
        for (int i = 0; i < user.length(); i++) {
            if (banned.charAt(i) == '*') continue;
            if (user.charAt(i) != banned.charAt(i)) return false;
        }
        
        return true;
    }
}