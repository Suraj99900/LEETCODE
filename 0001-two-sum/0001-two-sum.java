class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] data = {0,0};
        for(int iii =0 ; iii < nums.length;iii++){
            for(int jjj = iii+1 ; jjj < nums.length ;jjj++){
                // Now target match with adding value
                if((nums[iii] + nums[jjj]) == target){
                    data[0] = iii;
                    data[1] = jjj; 
                }
                
            }
        }
        return data;
    }
}