class Solution {
    public int search(int[] nums, int target) {
        
        int num = nums.length;
        int left = 0;
        int right = num-1;
        
        // System.out.println(mid);
        while(left <= right){
            int mid = left +(right-left)/2;
            // System.out.println(mid);
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] < target){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        return -1;
    }
}