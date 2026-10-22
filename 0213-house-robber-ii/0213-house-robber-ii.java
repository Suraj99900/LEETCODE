class Solution {

    private int robLinear(int [] nums,int start,int end){
        
        
        int prev1 = 0;
        int prev2 = 0;
        int current = 0;

        for(int i = start  ;i<=end;i++){
            // System.out.println("prev1: "+prev1+" prev2: "+ prev2 + " nums[i]: "+ nums[i]);
            current = Math.max(prev1,prev2+nums[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
    public int rob(int[] nums) {

        if(nums.length <=1){
            return nums[0];
        }



        int result1 = robLinear(nums,0,nums.length-2);
        int result2 = robLinear(nums,1,nums.length-1);
        int result = Math.max(result1 ,result2);
        return result;
    }
}