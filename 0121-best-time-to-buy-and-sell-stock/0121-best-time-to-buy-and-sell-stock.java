class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for(int i =0;i < prices.length;i++){
            if(prices[i] < minPrice){
                minPrice = prices[i];
            }else{
                if(prices[i]-minPrice > maxProfit ){
                    maxProfit = prices[i]-minPrice;
                }
            }
            // System.out.println("prices[i]: "+prices[i]+ "minPrice : "+ minPrice + "maxProfit: " + maxProfit  );
        }
        System.out.println(maxProfit);
        


        return maxProfit;
    }
}