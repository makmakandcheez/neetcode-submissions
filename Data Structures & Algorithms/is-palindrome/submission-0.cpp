class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty())
            return true;

        int i = 0;
        int j = s.size()-1;
        char* left;
        char* right;

        while (i < j) {
            left = &s[i];
            right = &s[j];


            while (
                ((*left < 48 || *left > 57) &&
                (*left < 65 || *left > 90) &&
                (*left < 97 || *left > 122)) && 
                (i < j)
                ) {
                    i++;
                    left = &s[i];
                }
            while (
                ((*right < 48 || *right > 57) &&
                (*right < 65 || *right > 90) &&
                (*right < 97 || *right > 122)) && 
                (i < j)
                ) {
                    j--;
                    right = &s[j];
                }
            // cout << *left << *right << endl; 
            if (tolower(*left) == tolower(*right)) {
                i++;
                j--;
            }
            else {
                return false;
            }     
        }
        return true;
    }
};
