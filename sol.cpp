#include<iostream>
using namespace std;

const long long int k=1e9+7;
long long int exp(long long int a,long long int b){
    if (b==0) return 1;
    long long int x=exp(a,b/2);
    x*=x;
    x%=k;
    if(b%2) x*=a;
    x%=k;
    return x;
}
int main (){
    int a,b;
    cin>>a>>b;
    cout<<INT MAX(a,b)<<endl;
    return 0;
}