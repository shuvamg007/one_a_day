class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        unordered_map<char, char> umap;

        umap['('] = ')';
        umap['['] = ']';
        umap['{'] = '}';

        for (int i=0; i < s.length(); i++) {
            if (umap.count(s[i]) > 0) {
                stack.push(s[i]);
            }
            else {
                if (stack.size() == 0 || umap[stack.top()] != s[i])
                    return false;
                stack.pop();
            }
        }
        if (stack.size() != 0)
            return false;
        return true;
    }
};