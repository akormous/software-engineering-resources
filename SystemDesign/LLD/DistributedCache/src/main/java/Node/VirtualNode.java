package Node;
import Node.Node;

/**
 *
 * @param <T> type of Node, only virtual nodes are mapped on the hash ring
 */
public class VirtualNode<T extends Node> implements Node {
    final T physicalNode;
    final int replicaIndex;

    /**
     *
     * @param physicalNode each virtual node has a reference to its physical node
     * @param replicaIndex
     */
    public VirtualNode(T physicalNode, int replicaIndex) {
        this.physicalNode = physicalNode;
        this.replicaIndex = replicaIndex;
    }

    @Override
    public String getKey() {
        return physicalNode.getKey() + "-" + replicaIndex;
    }

    /**
     *
     * @param pNode physical node
     * @return true if it is a virtual node of the given reference of physical node
     */
    public boolean isVirtualNodeOf(T pNode) {
        return physicalNode.getKey().equals(pNode.getKey());
    }

    public T getPhysicalNode() {
        return physicalNode;
    }
}
