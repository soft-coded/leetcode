class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        
        for(int num: nums) s.insert(num);
        
        int ans = 0;
        
        for (int num: nums) {
            if (s.find(num - 1) == s.end()){
                int curnum = num;
                int curlen = 1;
                
                while (s.find(curnum + 1) != s.end()){
                    curlen++;
                    curnum++;
                }
                
                if (curlen > ans) ans = curlen;
            }
        }
        
        return ans;
    }
};