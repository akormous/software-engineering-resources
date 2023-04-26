package ConsistentHash;
import HashFunction.HashFunction;
import HashFunction.MD5HashFunction;
import Node.Node;
import Node.VirtualNode;

import java.util.Collection;
import java.util.SortedMap;
import java.util.TreeMap;

/**
 *
 * @param <T> ConsistentHashRouter for a type of Node
 */
public class ConsistentHashRouter<T extends Node> {
    private final SortedMap<Long, VirtualNode<T>> ring = new TreeMap<>();
    private final HashFunction hashFunction;

    /**
     *
     * @param physicalNodes collection of physical server nodes
     * @param virtualNodeCount number of virtual nodes required aka weight
     */
    public ConsistentHashRouter(Collection<T> physicalNodes, int virtualNodeCount) {
        /**
         * calls another constructor by passing a default MD5 hash function
         */
        this(physicalNodesNodes, virtualNodeCount, new MD5HashFunction());
    }

    /**
     *
     * @param physicalNodes collection of physical server nodes
     * @param virtualNodeCount number of virtual nodes required aka weight
     * @param hashFunction hash function used to generate hash
     */
    public ConsistentHashRouter(Collection<T> physicalNodes, int virtualNodeCount, HashFunction hashFunction) {
        if(hashFunction == null) {
            throw new NullPointerException("Hash Function is null");
        }
        this.hashFunction = hashFunction;
        if(physicalNodes != null) {
            for(T physicalNode : physicalNodes) {
                addNode(physicalNode, virtualNodeCount);
            }
        }
    }

    /**
     * Adds physical node and the given number of virtual nodes onto the hash ring
     * @param physicalNode physical server node
     * @param virtualNodeCount number of virtual nodes required
     */
    public void addNode(T physicalNode, int virtualNodeCount) {
        if(virtualNodeCount < 0) {
            throw new IllegalArgumentException("Count of virtual nodes cannot be negative: " + virtualNodeCount);
        }

        for(int i = 0; i < virtualNodeCount; i++) {
            VirtualNode<T> tempVirtualNode = new VirtualNode<T>(physicalNode, i);
        }
    }
}
