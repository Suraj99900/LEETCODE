class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        map.put(0,1);
        int prefixSum = 0;
        int count = 0;
        for (int i =0 ; i< nums.length;i++){
            prefixSum += nums[i];
            int req = prefixSum -k;
             // Count subarrays ending at current index
            count += map.getOrDefault(req, 0);
            // System.out.println("count:"+count+ " req:"+req+" prefixSum: "+prefixSum);

            // Store/update frequency of current prefix sum
            map.put(prefixSum,
                    map.getOrDefault(prefixSum, 0) + 1);
        }

        return count; 
    }
}