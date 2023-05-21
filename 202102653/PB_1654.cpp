#include<iostream>

// Declare variable
unsigned int numberOfHavingWire, numberOfNeedWire, ans;
unsigned int wireArr[10001];
int  max = 0;
long long mid, high, low;

int main()
{
	std::cin >> numberOfHavingWire >> numberOfNeedWire;

    if(numberOfHavingWire > numberOfNeedWire) {
        std::cout << "Error : Invalid Input" << std::endl;
        return 1;
    }

	for (unsigned int i = 0; i < numberOfHavingWire; i++)
	{
		std::cin >> wireArr[i];
		if (max < wireArr[i]) max = wireArr[i];
	}

	low = 1;
	high = max;
	ans = 0;

	while (low <= high)
	{
		mid = (low + high) / 2;
		int cnt = 0;
		for (unsigned int i = 0; i < numberOfHavingWire; i++)
			cnt += wireArr[i] / mid;

		if (cnt >= numberOfNeedWire) {
			low = mid + 1;
			if (ans < mid) ans = mid;
		} else {
			high = mid - 1;
		}
	}
	
    if(ans == 0) {
        std::cout << "Error: Cannot create as many wires as desired" << std::endl;
            return 1;
    }

	std::cout << ans << std::endl;

    return 0;
}
