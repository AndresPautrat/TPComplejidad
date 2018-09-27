#include "iostream"
#include "stdlib.h"
#include "fstream"
#include "sstream"
#include "string"
#include "vector"
#include "iomanip"
#include "math.h"
#include "chrono"

using namespace std;


void LeerCPS(string filename,vector<vector<long double>>& G){
	ifstream file(filename);
	if(file.fail()){
		cout<<"El archivo no pudo abrirse";
		exit(1);
	}
	string line;
	while(getline(file,line)){
		stringstream lineStream(line);
		vector<long double> pair;
		size_t sz;
		string n;
		
		while(getline(lineStream,n,',')){
			pair.push_back(stold(n, &sz));
		}
		G.push_back(pair);
	}
}
void CalcularMA(int n,vector<vector<long double>>& G,vector<vector<long double>>& MA){
	for(int i=0; i<n; i++){
		for(int j=i+1; j<n; j++){
			long double d=pow(pow(G[i][0]-G[j][0],2)+pow(G[i][1]-G[j][1],2),0.5);
			MA[i][j]=d;
			MA[j][i]=d;
		}
	}
}
void SimpleWrite(){
	ofstream file;
	file.open("CPS_MA.txt",ios::out); //python: open(filename,"w")
	
	if(file.fail()){
		cout<<"El archivo no pudo abrirse";
		exit(1);
	}
	
	file<<"Hola qué tal?, soy un gil";
	file.close();
}
void EscribirMA(int n,string filename, vector<vector<long double>> MA){
	ofstream file;
	file.open(filename,ios::out);
	if(file.fail()){
		cout<<"El archivo "<<filename<<" no pudo abrirse"<<endl;
		exit(1);
	}
	
	file<<"G={";
	for(int i=0; i<n-1; i++){
		ostringstream content;
		content<<setprecision(17)<<"{";
		for(int j=0;j<n-1;j++){
			content<<MA[i][j]<<",";
		}
		content<<MA[i][n-1]<<"},";
		file<<content.str();
	}
	ostringstream content;
	content<<setprecision(17)<<"{";
	for(int j=0;j<n-1;j++){
		content<<MA[n-1][j]<<",";
	}
	content<<MA[n-1][n-1]<<"}}";
	file<<content.str();
	file.close();
}
void EscribirDirecto(int n,string filename,vector<vector<long double>>& G){

	ofstream file;
	file.open(filename,ios::out);
	if(file.fail()){
		cout<<"El archivo "<<filename<<" no pudo abrirse"<<endl;
		exit(1);
	}
	
	file<<"float G["<<n<<"]["<<n<<"]={";
	for(int i=0; i<n-1; i++){
		float p=100*i*pow(n,-1);
		if(p==int(p))cout<<p<<"%\n";
		ostringstream content;
		content<<setprecision(5)<<"{";
		for(int j=0;j<n-1;j++){
			content<<pow(pow(G[i][0]-G[j][0],2)+pow(G[i][1]-G[j][1],2),0.5)<<",";
		}
		content<<pow(pow(G[i][0]-G[n-1][0],2)+pow(G[i][1]-G[n-1][1],2),0.5)<<"},";
		file<<content.str();
	}
	ostringstream content;
	content<<setprecision(5)<<"{";
	for(int j=0;j<n-1;j++){
		content<<pow(pow(G[n-1][0]-G[j][0],2)+pow(G[n-1][1]-G[j][1],2),0.5)<<",";
	}
	content<<pow(pow(G[n-1][0]-G[n-1][0],2)+pow(G[n-1][1]-G[n-1][1],2),0.5)<<"}};";
	file<<content.str();
	file.close();
}
int main(){
	int n=12;//145225;
	vector<vector<long double>> G;
	//vector<vector<long double>> MA(n, vector<long double>(n,0));
	//LEER CPS
	LeerCPS("CleanBDO.txt",G);
	//ESCRIBIR DIRECTO
	auto start = std::chrono::high_resolution_clock::now();
	EscribirDirecto(n,"CPS_MA_12.cpp",G);
	auto finish = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed = finish - start;
	cout << "Elapsed time EscribirDirecto: " << elapsed.count() << " s\n";
	//CALCULAR MA
	/*
	auto start = std::chrono::high_resolution_clock::now();
	CalcularMA(n,G,MA);
	auto finish = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> elapsed = finish - start;
	cout << "Elapsed time CalcularMA: " << elapsed.count() << " s\n";
	//ESCRIBIR MA
	start = std::chrono::high_resolution_clock::now();
	EscribirMA(n,"CPS_MA_1000.txt",MA);
	finish = std::chrono::high_resolution_clock::now();
	elapsed = finish - start;
	cout << "Elapsed time EscribirMA: " << elapsed.count() << " s\n";
	*/
	return 0;
}
