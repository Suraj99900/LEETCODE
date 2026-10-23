class Solution {
    public int majorityElement(int[] nums) {
        int max = Integer.MIN_VALUE;
        int maxCount = 0;
       for (int i =0 ;i<nums.length;i++){
            if(maxCount == 0){
                max = nums[i];
            }

            if (max == nums[i]){
                maxCount++;
            }else{
                maxCount--;
            }
       }
       return max;
    }
}