public static Node lca(Node root, int v1, int v2) {
      	String[] str1 = find(root, v1).split("-");
        String[] str2 = find(root, v2).split("-");
        int strlength = Math.min(str1.length, str2.length);
        Node node = root;
        for(int i = 0; i < strlength; i++) {
            if(str1[i].equals(str2[i])) {
                if(str1[i].equals("L")) node = node.left;
                if(str1[i].equals("R")) node = node.right;
            }
            else break;
        }
        return node;
    }

    static String find(Node node, int v) {

        if(node.data == v) return "D";

        String result = "";
        if(node.left != null) {
            result = find(node.left, v);
            if(!result.equals("")) return "L-" + result;
        }
        if(node.right != null) {
            result = find(node.right, v);
            if(!result.equals("")) return "R-" + result;
        }        
        return result;
    }