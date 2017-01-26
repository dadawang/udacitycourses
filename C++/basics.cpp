#include <iostream> 

using namespace std;

class Dstring 
{
	public:
		Dstring(const char *s) 
		{
			str = new char[MAX_LENGTH];
			strcpy(str, s)
		}

		~Dstring()
		{
			delete []str;
		}

		void print_str()
		{
			printf("%s\n", str);
		}

		friend operator = (const char *x, char *y)
		{
			int n = strlen(x);
			y = new char[n];
			for (int i = 0; i < n; i++) {
				y[i] = x[i]
			}
		}

	private:
		char *str;
}


int main()
{
	Dstring A("foo");
	Dstring B;
	
	B = A;

	B.print_str();	

	return 0;
}
