class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0] ;
        // System.out.println(nums.length);
        for (int i =1; i< nums.length;i++){
            // System.out.println("maxSum : "+maxSum +" currentSum: "+currentSum);
            // System.out.println("currentSum: "+ (currentSum + nums[i]));
            currentSum = Math.max(nums[i],currentSum + nums[i]);
            
            if(currentSum > maxSum){
                maxSum = currentSum;
            }
            // System.out.println("maxSum : "+maxSum +" currentSum: "+currentSum);

            
        }

        return maxSum;
    }
}