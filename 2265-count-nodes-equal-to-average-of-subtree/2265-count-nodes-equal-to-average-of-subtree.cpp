class Solution {
public:
    int ans = 0;

    pair<int, int> dfs(TreeNode* node) {
        if (!node)
            return {0, 0};

        auto [ls, lc] = dfs(node->left);
        auto [rs, rc] = dfs(node->right);

        int sum = ls + rs + node->val;
        int count = lc + rc + 1;

        if (sum / count == node->val)
            ans++;

        return {sum, count};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};