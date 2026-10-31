class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {

       /* What should be the condition of the while loop for two pointers?
        How will you compare nums1[i][0] and nums2[j][0]?
        What will you do when both IDs are equal?
        How will you handle the remaining elements? */

        ArrayList <int[]> num = new ArrayList<>();
        int i =0;
        int j =0;
        while(i < nums1.length && j<nums2.length){

            if(nums1[i][0] == nums2[j][0]){
                num.add(new int[] {nums1[i][0],nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            }else if(nums1[i][0] < nums2[j][0]){
                num.add(new int[] {nums1[i][0],nums1[i][1]});
                i++;
            }else {
                num.add(new int[] {nums2[j][0],nums2[j][1]});
                j++;
            }
        }

        while(i < nums1.length){
            num.add(new int[] {nums1[i][0],nums1[i][1]});
                i++;
        }

        while(j < nums2.length){
            num.add(new int[] {nums2[j][0],nums2[j][1]});
                j++;
        }

        return num.toArray(new int[num.size()][]);
    }
}