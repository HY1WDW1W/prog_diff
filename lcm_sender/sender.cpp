#include <lcm/lcm-cpp.hpp>
#include "mvec_pk/mvec.hpp"


using namespace std;


int main(int argc, char *argv[])
{

	lcm::LCM lcm;
	if(!lcm.good())
	{
		return -1;
	}

	mvec_pk::mvec data;
	data.title = argv[1];
	data.len=10;
	data.vec.resize(data.len);
	for(int i=0; i<data.len; i++)
		data.vec[i]=i;

	lcm.publish("TEST", &data);
}
