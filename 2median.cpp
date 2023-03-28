/*
Compute Median brute force and then compare with 
the new strategy
*/

#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
/*
* Returns Hamming distance between s and t
*/
int getDistance(string s, string t){
	int i, dist=0;
	for(i=0;i<s.length();i++){
		if(s[i]!=t[i])
			dist++;
	}
	return dist;
}
/*
Return median of the strings
*/
string getMedianOfASet(vector<string> & s){
	int d=s[0].length();
	string med(d,'0');
	for(int i=0;i<d;i++){
		int countI=0;
		for(string str : s){
			if(str[i]=='1')
				countI++;
		}
		if(countI > s.size()/2 )
			med[i]='1';
		else
			med[i]='0';
	}
	return med;
}

/*
 Compute the Median objective value of a set S
 Center can be obtained from - getMedianOfASet
*/
int getMedianObjValue(vector<string> &s){
	if(s.size() == 0)
		return 0;
	int objValue = 0;
	string center = getMedianOfASet(s);
	for(string str : s){
		objValue += getDistance(center, str);
	}
	return objValue;
}

/*
* Return Optimum Median Objective Value among all possible subsets
*/
int computeOPT2Median(vector<string> &input_strings, vector<string> &cluster1, vector<string> &cluster2){

	// For all possible subsets of input_strings S1 and S2 - check min median

	int optMedianObjValue = INT_MAX;

	int len, n=input_strings.size();
	
	// All Possible subsets of input_strings
	for(len=0 ; len < n ; len++){
		string subset(n,'0');
		for(int j=0 ; j<len ; j++){
			subset[n-j-1]='1';
		}

		do{

			vector<string> s1, s2;
			// Create subset s1 and s2
			for(int i=0; i < n ;i++){
				if(subset[i]=='1'){
					s1.push_back(input_strings[i]);
				}
				else{
					s2.push_back(input_strings[i]);
				}

			}

			// compute Median and Update
			int medianObjValueCurrent = getMedianObjValue(s1) + getMedianObjValue(s2);
			if(optMedianObjValue > medianObjValueCurrent){
				optMedianObjValue = medianObjValueCurrent;
				cluster1 = s1;
				cluster2 = s2;
			}
		}while(next_permutation(subset.begin(),subset.end()));
		
	}
	return optMedianObjValue;

}

int main(){

	vector<string> input_strings{"000","001","010","011","100","101","110","111"};

		//"0011000101","0010101010","1111000101","1001010010","1000010100","1000111111","1101001101","0101000011","1011110101","0001101001","0110110001","1001110110","1101001000","1010001001","1001000111","1010001011","0001101000","1101000000","1000111011","0111010001","0100110110"}; 

	vector<string> cluster1;
	vector<string> cluster2;
	int optMedianObjValue;

	optMedianObjValue = computeOPT2Median(input_strings,cluster1, cluster2);

	cout<<"Optimum Median Objective Value - "<<optMedianObjValue<<endl;
	cout<<"Cluster 1 "<<endl;
	// print cluster 1
	for(string s : cluster1)
		cout<<s<<" ";
	cout<<endl;
	// print center1
	cout <<getMedianOfASet(cluster1)<<endl;

	cout<<"\n Cluster 2 "<<endl;
	// print cluster 2
	for(string s : cluster2)
		cout<<s<<" ";
	cout<<endl;
	// print center2
	cout <<getMedianOfASet(cluster2)<<endl;
	return 0;
}