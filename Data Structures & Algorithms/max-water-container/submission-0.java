class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length-1;
        int area = 0;
        int res = 0;

        while (l<r){

            int width = r-l;
            int height = Math.min(heights[l], heights[r]);
            
            area = width*height;
            res = Math.max(area, res);

            if(heights[l]<heights[r]){
                l++;
            }
            else{
                r--;
            }

            
        }

        return res;

    }
}
