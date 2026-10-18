class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int n = nums.length;
        for(int iii =0 ; iii < nums.length;iii++){
            for(int jjj = iii+1 ; jjj < nums.length ;jjj++){
                // Now target match with adding value
                if((nums[iii] + nums[jjj]) == target){
                    return new int[]{iii,jjj} ;
                }
                
            }
        }
        return new int[]{};
    }
}