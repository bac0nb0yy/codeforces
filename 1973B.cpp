#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
		}

		int low = 1, high = n, k = 1;

		while (low < high) {
			k = (low + high) / 2;
			bool valid = true;
			int old = -1;

			for (int i = 0; i <= n - k; ++i) {
				int r = 0;
				for (int j = i; j < i + k; ++j) {
					r |= a[j];
				}
				if (old != -1 && old != r) {
					valid = false;
					break;
				}
				old = r;
			}

			if (valid) {
				high = k;
			} else {
				low = k + 1;
			}
		}

		if (low == high) {
			k = low;
		}
		cout << k << '\n';
	}

	return 0;
}