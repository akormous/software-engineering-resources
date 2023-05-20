package ConsistentHash;
import HashFunction.HashFunction;
import HashFunction.MD5HashFunction;
import Node.Node;
import Node.VirtualNode;

import java.util.Collection;
import java.util.Iterator;
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
        this(physicalNodes, virtualNodeCount, new MD5HashFunction());
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
        int existingReplicas = getExistingReplicas(physicalNode);
        for(int i = 0; i < virtualNodeCount; i++) {
            VirtualNode<T> tempVirtualNode = new VirtualNode<T>(physicalNode, i + existingReplicas);
            ring.put(hashFunction.hash(tempVirtualNode.getKey()), tempVirtualNode);
        }
    }

    /**
     * remove all the virtual nodes belonging to the given physical node
     * @param physicalNode
     */
    public void removeNode(T physicalNode) {
        Iterator<Long> it = ring.keySet().iterator();
        while(it.hasNext()) {
            Long key = it.next();
            VirtualNode<T> vNode = ring.get(key);
            if(vNode.isVirtualNodeOf(physicalNode)) {
                it.remove();
            }
        }
    }

    /**
     * returns the closest physical node on the ring for a given key
     * @param objectKey key of the object we want to route to the physical node
     * @return closest physical node to the key
     */
    public T routeNode(String objectKey) {
        if(ring.isEmpty()) {
            return null;
        }
        // calculate the hash value that can be searched on the ring
        Long hashVal = hashFunction.hash(objectKey);
        // get the part of the ring which has values >= hashVal
        SortedMap<Long, VirtualNode<T>> tailMap = ring.tailMap(hashVal);

        // get the hash val of the closest physical node in clockwise direction
        Long nodeHashVal = tailMap.isEmpty() ? ring.firstKey() : tailMap.firstKey();
        return ring.get(nodeHashVal).getPhysicalNode();
    }


    public int getExistingReplicas(T physicalNode) {
        int replicas = 0;
        for(VirtualNode<T> vNode : ring.values()) {
            if(vNode.isVirtualNodeOf(physicalNode)) {
                replicas++;
            }
        }
        return replicas;
    }
}
