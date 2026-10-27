class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if(strs.length == 0 && strs == null){
            return "";
        }
        String Prefix = strs[0];
        
        for (int i = 0 ; i < strs.length;i++){
            while(!(strs[i].startsWith(Prefix))){
                // System.out.println("Before: "+Prefix);
                Prefix = Prefix.substring(0,Prefix.length()-1);
                // System.out.println("After: "+Prefix);
                if(Prefix.isEmpty()){
                    return "";
                }
            }
        }

        // System.out.println(Prefix);
        return Prefix;
    }
}