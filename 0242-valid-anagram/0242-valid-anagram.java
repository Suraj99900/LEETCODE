class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i++) {
            // System.out.println();
            if (map.containsKey(s.charAt(i))) {
                map.merge(s.charAt(i), 1, Integer::sum);
            } else {
                map.put(s.charAt(i), 1);
            }
        }

        for (int j = 0; j < t.length();j++) {
            if (map.containsKey(t.charAt(j))) {
                if (map.get(t.charAt(j)) > 0) {
                    map.merge(t.charAt(j), 1, (oldVal, newVal) -> oldVal - newVal);
                }else{
                    return false;
                }
            } else {
                return false;
            }
        }

        return true;
    }
}