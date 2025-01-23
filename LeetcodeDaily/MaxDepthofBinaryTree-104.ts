function maxDepth(root: TreeNode | null): number {

  let ans:number=0;

    function dfs(node:TreeNode |null){
        if(!node) return 0;

//? Find the Left and right
        let left=dfs(node.left);

        let right=dfs(node.right);
//?Get the Max of it and Return 
        return Math.max(left,right)+1;
    }
    ans=dfs(root);

    return ans;
};