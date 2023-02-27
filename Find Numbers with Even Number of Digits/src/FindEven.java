
public class FindEven {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] test_nums = new int[5];
		test_nums[0] = 12;
		test_nums[1] = 34;
		test_nums[2] = 20;
		test_nums[3] = 67;
		test_nums[4] = 7896;
		
		Solution a = new Solution();
		int result = a.findNumbers(test_nums);
		
		System.out.println(result);
	}

}
