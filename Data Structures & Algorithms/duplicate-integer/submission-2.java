class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> obj = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if (obj.contains(nums[i])){
                return true;
            }
            obj.add(nums[i]);

        }
        return false;
    }
}