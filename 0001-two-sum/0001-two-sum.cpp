class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++)
        {
            int n1 = nums[i];
            for (int j = i+1; j < nums.size(); j++)
            {
                int n2 = nums[j];
                if (n1 + n2 == target)
                {
                    vector<int> ans{i, j};
                    return ans;
                }
            }
        }
        return {};
    }
};