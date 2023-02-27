public class Solution {
    public int findNumbers(int[] nums) {
         int count_digits = 1; // count digits in number
         int count_even = 0; // count even numbers
         for (int num : nums) {
        	 count_digits = 1; // reset to one
        	 while (num/10 > 0) {
        		 num = num/10;
        		 count_digits += 1;
        	 }
        	 if (count_digits%2 == 0) {
        	 count_even+= 1;
        	 }
         }
         return count_even;
        }       
}