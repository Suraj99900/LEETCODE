class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> map = new HashMap<>();
        
        for(int i = 0 ; i < strs.length;i++){
            char [] charData = strs[i].toCharArray();
            Arrays.sort(charData);
            String sortedString = new String(charData);

            List<String> indexval = new ArrayList<>();
            if(map.containsKey(sortedString)){
                indexval = map.get(sortedString);
                indexval.add(strs[i]);
                map.put(sortedString,indexval);
            }else{
                indexval.add(strs[i]);
                map.put(sortedString,indexval);
            }
        }

        // Map to List array 
        List<List<String>> resultData = new ArrayList<>();
        for( List<String> data : map.values()){
            // System.out.println(data);
            resultData.add(data);
        }
        // System.out.println(map);
        return resultData;
    }
   
}