using System;

public class GFG
{
	public const int MAX = 1000;

	public static int[] BITree = new int[MAX];

	public static void updateBIT(int n, int index, int val)
	{
		index = index + 1;

		while (index <= n)
		{
			BITree[index] += val;

			index += index & (-index);
		}
	}

	public static void constructBITree(int[] arr, int n)
	{
		for (int i = 1; i <= n; i++)
		{
			BITree[i] = 0;
		}

		for (int i = 0; i < n; i++)
		{
			updateBIT(n, i, arr[i]);
		}
		//for (int i = 1; i <= n; i++)
		//	Console.WriteLine(BITree[i]);
    }

	public static int getSum(int index)
	{
		int sum = 0; 		
		index = index + 1;

		while (index > 0)
		{
			sum += BITree[index];
			index -= index & (-index);
		}
		return sum;
	}

	public static void update(int l, int r, int n, int val)
	{
		updateBIT(n, l, val);
		updateBIT(n, r + 1, -val);
	}

	public static void Main(string[] args)
	{
		int[] arr = new int[] { 0, 0, 0, 0, 0 };
		int n = arr.Length;

		constructBITree(arr, n);

		int l = 2, r = 4, val = 2;
		update(l, r, n, val);

		int index = 4;

		Console.WriteLine("Element at index " + index + " is " + getSum(index));

		l = 0;
		r = 3;
		val = 4;
		update(l, r, n, val);
		index = 3;
		Console.WriteLine("Element at index " + index + " is " + getSum(index));
		Console.ReadKey();
	}
}
