class Solution {
public:
    bool checkValidString(string s) {
        int extraL = 0;
        int possLN = 0;
        int possLNR = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char c = s[i];
            switch (c)
            {
                case '(':
                    extraL += 1;
                    break;
                case ')':
                    extraL -= 1;
                    
                    break;
                default:
                    if (extraL == 0)
                    {
                        possLN += 1;
                    }
                    else
                    {
                        possLNR += 1;
                    }
                    break;
            }
            if (extraL < 0) {
                if (possLN > 0) { possLN -= 1; }
                else if (possLNR > 0) { possLNR -= 1; }
                else { return false; }
                extraL = 0;
            }
            if (extraL < possLNR)
            {
                possLNR -= 1;
                possLN += 1;
            }
        }
        return extraL <= possLNR;
    }
};