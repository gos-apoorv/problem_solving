class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = sum(x*y for x,y in zip(self.arr, vec.arr))
        return dot_product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)