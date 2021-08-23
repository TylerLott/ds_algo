class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (hm.containsKey(nums[i])) {
                int[] res = new int[2];
                res[0] = hm.get(nums[i]);
                res[1] = i;
                return res;
            } else {
                hm.put(target-nums[i],i);
            }
        }
        return new int[1];
    }
}