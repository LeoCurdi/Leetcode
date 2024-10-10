public class Solution {
    public int ClimbStairs(int n) {
        int i1 = 1;
        int i2 = 1;
        int cur = 1;

        for (int i = 2; i <= n; i++) {
            cur = i1 + i2;
            i2 = i1;
            i1 = cur;
        }

        return cur;
    }
}