class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        int i = 0;
        int j = 0;

        string op;
        while (i < m && j < n) {
            op.push_back(word1[i++]);
            op.push_back(word2[j++]);
        }

        while (i < m)
            op.push_back(word1[i++]);

        while (j < n)
            op.push_back(word2[j++]);

        return op;
    }
};