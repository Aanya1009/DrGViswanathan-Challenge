def findGCD(self, nums: list[int]) -> int:
        greatest=max(nums)
        smallest=min(nums)
        while smallest!=0:
            greatest, smallest= smallest, greatest%smallest
        return greatest