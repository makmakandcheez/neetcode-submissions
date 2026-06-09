class Solution {
public:
    int hammingWeight(uint32_t n) {
        int set_bits = 0;
        while (n > 0) {
            if (n % 2 != 0) set_bits++;
            n /= 2;
        }
        return set_bits;
    }
};
