class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        // ArrayList<Integer> returnData = new ArrayList<>();

        // for (int i =0 ; i<= nums.length -k ;i++){
        //     int iMax = Integer.MIN_VALUE;
        //     for (int j =i;j < i +k ;j++){
        //         iMax = (iMax> nums[j]) ? iMax : nums[j];
        //         // System.out.print( nums[j]+"-");
        //     }
        //     // System.out.println( iMax +"-");
        //     returnData.add(iMax);
        // }

        // return returnData.stream().mapToInt(Integer::intValue).toArray();


        int n = nums.length;
        int[] result = new int[n - k + 1];

        Deque<Integer> deque = new ArrayDeque<>();
        int index = 0;

        for (int i = 0; i< n ;i++){

             while (!deque.isEmpty() && deque.peekFirst() <= i - k) {
                deque.pollFirst();
            }

            // Remove indices of smaller or equal elements
            while (!deque.isEmpty()
                    && nums[deque.peekLast()] <= nums[i]) {
                deque.pollLast();
            }

            // Add current index
            deque.offerLast(i);

            // Record maximum when the first window is complete
            if (i >= k - 1) {
                result[index++] = nums[deque.peekFirst()];
            }
        }

        return result;
    }
}