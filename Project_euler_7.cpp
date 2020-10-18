#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cout << "Enter the number of test : ";
    cin >> t;

    for (int a0 = 0; a0 < t; a0++)
    {
        int flag, answer, number, count, n;
        cout << "Enter the n'th number : ";
        cin >> n;

        flag = count = 0;
        number = answer = 1;

        while (count < n)
        {
            flag = 0;

            if (number == 1)
                flag = 1;
            if (number % 2 == 0)
                flag = 1;
            if (number == 2)
                flag = 0;

            double boundary = (int)floor(sqrt(number));

            for (int i = 3; i <= boundary; i += 2)
            {
                if (number % i == 0)
                    flag = 1;
            }
            if (flag == 0)
            {
                answer = number;
                count++;
                // cout << count << " --> " << answer << endl;
            }
            number++;
        }
        cout << answer << endl;
    }
}
