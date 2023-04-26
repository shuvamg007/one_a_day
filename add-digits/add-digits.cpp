class Solution {
public:
    int addDigits(int num) {
        while (num / 10 >= 1) {
            int tmp = 0;
            while (num > 0) {
                tmp = tmp + (num % 10);
                num = int(num / 10);
            }
            num = tmp;
        }

        return num;
    }
};