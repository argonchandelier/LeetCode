# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        layer = [root.val]
        layerNode = [root]
        layers = []
        odd = False
        while layer:
            if odd:
                layers.append(list(reversed(layer)))
            else:
                layers.append(layer)
                
            newLayer = []
            newLayerNode = []
            
            for node in layerNode:
                if node.left:
                    newLayer.append(node.left.val)
                    newLayerNode.append(node.left)
                if node.right:
                    newLayer.append(node.right.val)
                    newLayerNode.append(node.right)
            
            layer = newLayer
            layerNode = newLayerNode
            
            odd = not odd
        
        #for i, l in enumerate(layers):
        #    if i & 1:
        #        l.reverse()
        
        return layers