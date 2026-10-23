class Solution {
    public void moveZeroes(int[] nums) {
        
       if (nums == null || nums.length <= 1) {
            return;
        }

        int insertPos = 0;

        for (int current = 0; current < nums.length; current++) {
            if (nums[current] != 0) {
                //  System.out.println(nums[current]);
                if (insertPos != current) {
                    // System.out.println(nums[current]);
                    int temp = nums[insertPos];
                    nums[insertPos] = nums[current];
                    nums[current] = temp;
                }
                insertPos++;
            }
        }


    }
}