'''
4. Serialize and Deserialize a Binary Tree

Question:
Design algorithms to serialize and deserialize a binary tree.
 Serialization converts the tree into a string representation, 
and deserialization reconstructs the tree from the string.

Solution:                                                                                        I will use pre-order traversal for serialization, representing null pointers with a sentinel value (e.g., '#'). For deserialization, I'll use an iterator to reconstruct the tree from the serialized data.

'''