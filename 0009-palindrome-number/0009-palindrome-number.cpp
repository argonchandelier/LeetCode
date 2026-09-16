class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        vector<int> digits;
        while (x > 0)
        {
            int d = x % 10;
            x = x / 10;
            digits.push_back(d);
        }
        int l = digits.size();
        int hl = l / 2;
        l = l-1;
        for (int i = 0; i < hl; ++i)
        {
            if (digits[i] != digits[l-i]) return false;
        }
        return true;
    }
};