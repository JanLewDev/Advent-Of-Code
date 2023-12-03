/* 
This is just the second part of the problem.
I implemented the same solution in C++ to compare the diffence in execution time.
Results - C++ solution is around twice as fast compared to the Python implementation.
3.cpp took 0.066s while 3.py 0.121s
*/
#include <bits/stdc++.h>
using namespace std;

#define upgrade ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define size(v) (int)v.size()
#define pp pair<int, int>
#define f first
#define s second
typedef long long ll;
const int N = 1e6;

vector<vector<char>> input;
vector<string> stringInput;
int n;
map<pp, set<int>> gears;

bool inside(int x, int y){
    return x >= 0 && x < n && y >= 0 && y < n;
}

int main(){
    upgrade
    string line;
    while(cin >> line){
        input.push_back({});
        stringInput.push_back(line);
        for(auto i : line){
            input[size(input) - 1].push_back(i);
        }
    }
    
    n = size(input);
    for(int i = 0; i < n; i++){
        regex pattern("(\\d+)");
        string str = stringInput[i];
        regex_iterator<string::iterator> rit(str.begin(), str.end(), pattern);
        regex_iterator<string::iterator> rend;

        vector<pair<string, int>> matches;
        while(rit != rend){
            matches.push_back({rit->str(), rit->position()});
            ++rit;
        }

        for(auto match : matches){
            string number = match.f;
            int idx = match.s;
            if(inside(i, idx-1) && input[i][idx-1] == '*'){
                gears[{i, idx-1}].insert(stoi(number));
            }

            for(int j = 0;j<size(number)+2;j++){
                if(inside(i-1, idx+j-1) && input[i-1][idx+j-1] == '*'){
                    gears[{i-1, idx+j-1}].insert(stoi(number));
                }
                if(inside(i+1, idx+j-1) && input[i+1][idx+j-1] == '*'){
                    gears[{i+1, idx+j-1}].insert(stoi(number));
                }
            }

            if(inside(i, idx+size(number)) && input[i][idx+size(number)] == '*'){
                gears[{i, idx+size(number)}].insert(stoi(number));
            }
        }
        
    }

    ll ans = 0;
    for(auto i : gears){
        if(size(i.s) == 2){
            ll add = 1;
            for(auto j : i.s)
                add *= j;
            ans += add;
        }
    }

    cout << "answer is " << ans << "\n";
    
    return 0;
}