#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

//전역 변수 선언

//hash power array
double *hash;
//cryptocurrency array
double *crypto;
//Maximum number of nodes
int Dimension;
//Initial setting parameter
//int para;
//Processing nubmer
int processing_number;
//Number of repetition
int repeat;

//int p;
int G;
//int r;

void setParameter(int *D, int *N, int *R, /*int *P,*/ int *G/*, int *r*/);
void setarrays(double *a, double *b, int para, int G, int r);
void mining(double *a, double *b);
void investment(double *a,/* double *b,*/ int para, int r);
void reinvestment(double *a, double *b, int re, int g, int N);
double rand_exp(double a);
double rand_pareto(double a);
void print_output(double *a, int cond, int R, int state, int di, int G, int dp, int re);

int compare(const void *a, const void *b)    // 내림차순 비교 함수 구현
{
	double num1 = *(double *)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	double num2 = *(double *)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 > num2)    // a가 b보다 클 때는
		return -1;      // -1 반환

	if (num1 < num2)    // a가 b보다 작을 때는
		return 1;       // 1 반환

	return 0;           // a와 b가 같을 때는 0 반환
}

//메인 함수
int main(void) {

	setParameter(&Dimension, &processing_number, &repeat,/* &p,*/ &G/*, &r*/);

	srand(time(NULL));

	hash = (double *)malloc(sizeof(double) *Dimension);
	crypto = (double *)malloc(sizeof(double) *Dimension);

	double *init_hash = (double *)malloc(sizeof(double) *Dimension);
	//double *init_crypto = (double *)malloc(sizeof(double) *Dimension);
	//double *diffh = (double *)malloc(sizeof(double) *Dimension);
	//double *diffc = (double *)malloc(sizeof(double) *Dimension);

	for (int R = 0; R < repeat; R++) {
		//for (int G = 0; G < 2; G++) {
			for (int p = 0; p < 3; p++) {
				for (int r = 0; r < 3; r++) {
					//for (int dh = 0; dh < 3; dh++) {
					for (int re = 0; re < 5; re++) {
						setarrays(hash, crypto, p, G, r);

						for (int i = 0; i < Dimension; i++) {
							*(init_hash + i) = *(hash + i);
						//	*(init_crypto + i) = *(crypto + i);
						}

						for (int i = 0; i < processing_number; i++) {
							//printf("%d, ", i);
							mining(hash, crypto);
							//printf("mining %d회\n", i);
							investment(hash, /*crypto,*/ p, r);
							//printf("investment %d회\n", i);
							reinvestment(hash, crypto, re, G, i);
							//printf("reinvestment %d회\n", i);
							printf("process %d회 종료\n", i);
						}
						/*
						for (int i = 0; i < Dimension; i++) {
							*(diffh + i) = *(hash + i) - *(init_hash + i);
						//	*(diffc + i) = *(crypto + i) - *(init_crypto + i);
						}*/

						printf("sorting Start\n");
						//qsort(init_hash, Dimension, sizeof(double), compare);
						qsort(hash, Dimension, sizeof(double), compare);
						qsort(crypto, Dimension, sizeof(double), compare);
						//qsort(diffh, Dimension, sizeof(double), compare);

						//print_output(init_hash, 0, R, 1, p, G, r, re);
						//print_output(&init_crypto, 1, R, 1, p + 1, G, dh, r, re);
						print_output(hash, 0, R, 2, p, G, r, re);
						print_output(crypto, 1, R, 2, p, G, r, re);
						//print_output(diffh, 0, R, 3, p, G, r, re);
						//print_output(&diffc, 1, R, 3, p + 1, G, dh, r, re);

						printf("%d 회 실험, %d 사이즈 변화, %d 파라미터 종료\n", R, G, p);

						//exit(1);
					//}
					}
				//}
			}
		}
	}

	free(init_hash);
	//free(init_crypto);
	free(hash);
	free(crypto);
	//free(diffh);
	//free(diffc);

	return 0;
}

//전역변수들의 설정
void setParameter(int *D, int *N, int *R,/* int *P,*/ int *G/*, int *r*/) {

	printf("최대 노드 갯수를 입력하시오. 정수로 입력할 것.\n");

	int input;
	scanf("%d", &input);
	*D = input;
	printf("입력한 노드의 갯수: %d \n", *D);
	/*
	printf("분포형태 값을 입력하시오. 0: uniform, 1. exp, 2. power \n");
	
	
	int temp;
	scanf("%d", &temp);
	*P = temp;
	printf("입력한 파라미터: %d \n", *P);

	printf("파라미터 값을 입력하시오. \n");

	int para;
	scanf("%d", &para);
	*r = para;
	printf("입력한 파라미터: %d \n", *r);
	*/
	printf("성장 여부 값을 입력하시오. 0: static 1: growth \n");

	int growth;
	scanf("%d", &growth);
	*G = growth;
	printf("입력한 파라미터: %d \n", *G);
	
	printf("시스템이 작동할 횟수를 입력해주시오 \n");
	int temp2;
	scanf("%d", &temp2);

	*N = temp2;

	printf("입력한 숫자: %d \n", *N);

	int temp3;
	printf("몇 회 실험을 진행할지 입력하시오 \n");
	scanf("%d", &temp3);

	*R = temp3;


}

//hashpower와 cryptocurrancy 행렬의 초기화
void setarrays(double *a, double *b, int para, int G, int r) {

	double * arr1;
	arr1 = (double *)malloc(sizeof(double) *Dimension);

	double * arr2;
	arr2 = (double *)malloc(sizeof(double) *Dimension);

	int uni[3] = { 1, 5, 10 };
	double exp[3] = { 0.1, 1, 5 };
	double pow[3] = { 2, 2.5, 3};


	//G == 0 : Non growth
	if (G == 0) {
		//uniform distribution
		if (para == 0) {
			for (int i = 0; i < Dimension; i++) {

				arr1[i] = rand() / (double)RAND_MAX * uni[r];

			}
		}
		//exponential distribution
		else if (para == 1) {
			for (int i = 0; i < Dimension; i++) {

				arr1[i] = rand_exp(exp[r]);

			}
		}
		//Power-law distribution or Pareto distribution
		else if (para == 2) {
			for (int i = 0; i < Dimension; i++) {

				arr1[i] = rand_pareto(pow[r]);


			}
		}
	}
	else if (G == 1) {
		if (para == 0) {
			arr1[0] = rand() / (double)RAND_MAX * uni[r];
		}
		else if (para == 1) {
			arr1[0] = rand_exp(exp[r]);
		}
		else if (para == 2) {
			arr1[0] = rand_pareto(pow[r]);
		}

		for (int i = 1; i < Dimension; i++) {
			arr1[i] = 0;
		}
	}

	for (int i = 0; i < Dimension; i++) {
		arr2[i] = 0;
	}

	for (int i = 0; i < Dimension; i++) {
		*(a+i) = arr1[i];
		*(b+i) = arr2[i];
	}

	free(arr1);
	free(arr2);
}

//채굴에 성공할 노드의 결정 함수
void mining(double *a, double *b) {

	double * arr1;
	arr1 = (double *)malloc(sizeof(double) *Dimension);

	double * arr2;
	arr2 = (double *)malloc(sizeof(double) *Dimension);

	for (int i = 0; i < Dimension; i++) {
		arr1[i] = *(a + i);
		arr2[i] = *(b + i);
	}

	double total = 0;

	for (int i = 0; i < Dimension; i++) {
		total += arr1[i];
	}

	double possibility = rand() / (double)RAND_MAX * total;

	double indicator = 0;
	for (int i = 0; i < Dimension; i++) {

		indicator += arr1[i];

		if (possibility <= indicator) {
			arr2[i] += 1;
			//보상 수치는 이후 파라미터값으로 변경
			break;
		}
		else {

		}
	}

	for (int i = 0; i < Dimension; i++) {
		//*(a + i) = arr1[i];
		*(b + i) = arr2[i];
	}

	free(arr1);
	free(arr2);
}

//신규 진입 결정
void investment(double *a,/* double *b,*/ int para, int r) {

	double * arr1;
	arr1 = (double *)malloc(sizeof(double) *Dimension);

//	double * arr2;
//	arr2 = (double *)malloc(sizeof(double) *Dimension);

	for (int i = 0; i < Dimension; i++) {
		arr1[i] = *(a + i);
//		arr2[i] = *(b + i);
	}

	int uni[3] = { 1, 5, 10 };
	double exp[3] = { 0.1, 1, 5 };
	double pow[3] = { 2, 2.5, 3 };

	for (int i = 0; i < Dimension; i++) {

		if (arr1[i] == 0) {
			if (para == 0) {
				arr1[i] = rand() / (double)RAND_MAX * uni[r];
			}
			else if (para == 1) {
				arr1[i] = rand_exp(exp[r]);
			}
			else if (para == 2) {
				arr1[i] = rand_pareto(pow[r]);
			}

			//arr2[i] -= 5;
			break;
		}
	}

	for (int i = 0; i < Dimension; i++) {
		*(a + i) = arr1[i];
		//*(b + i) = arr2[i];
	}

	free(arr1);
//	free(arr2);


}

//재투자 여부
void reinvestment(double *a, double *b, /*int dh,*/ int re, int g, int N) {

	if (N != 0) {
		double * arr1;
		arr1 = (double *)malloc(sizeof(double) *Dimension);

		double * arr2;
		arr2 = (double *)malloc(sizeof(double) *Dimension);

		for (int i = 0; i < Dimension; i++) {
			arr1[i] = *(a + i);
			arr2[i] = *(b + i);
		}
		double * arr3;
		arr3 = (double *)malloc(sizeof(double) *Dimension);

		double chance;
		double maximum = 0;

		//int hash_ratio[3] = { 1, 5, 10 };
		//double wealth_ratio[4] = { 0.001, 0.01, 0.1, 0.5 };
		double wealth_ratio[5] = { 0.0125, 0.025, 0.05, 0.075, 0.0875 };

		for (int i = 0; i < Dimension; i++) {
			arr3[i] = 0;
		}

		for (int i = 0; i < Dimension; i++) {

			if (maximum < arr2[i]) {
				maximum = arr2[i];
			}
		}

		for (int i = 0; i < Dimension; i++) {

			chance = rand() / (double)RAND_MAX;

			if (chance <= arr2[i] / maximum) {
				arr1[i] += wealth_ratio[re] * arr2[i];
				arr3[i] = arr2[i] * wealth_ratio[re];
				arr2[i] -= arr2[i] * wealth_ratio[re];
			}
		}

		double multi;
		double temp = 0;

		if (g == 0) {

			multi = 1.0 / (Dimension - 1);

			for (int i = 0; i < Dimension; i++) {
				temp += arr3[i];
			}

			for (int i = 0; i < Dimension; i++) {
				arr3[i] = (temp - arr3[i]) * multi;

			}

			for (int i = 0; i < Dimension; i++) {
				arr2[i] += arr3[i];
			}
		}
		
		else if (g == 1) {
			if (N > 1) {
				multi = 1.0 / (N - 1);
			}
			else if (N == 1) {
				multi == 1.0;
			}

			for (int i = 0; i < N; i++) {
				temp += arr3[i];
			}

			for (int i = 0; i < N; i++) {
				arr3[i] = (temp - arr3[i]) * multi;

			}

			for (int i = 0; i < N; i++) {
				arr2[i] += arr3[i];
			}
		}
		

		for (int i = 0; i < Dimension; i++) {
			*(a + i) = arr1[i];
			*(b + i) = arr2[i];
		}

		free(arr1);
		free(arr2);
		free(arr3);
	}

}

double rand_exp(double a) {

	//y = - 1/a * log (1 -x) a = 1로 가정
	double result;
	double uncheckedChance = rand() / (double)RAND_MAX;
	while (uncheckedChance == 0 || uncheckedChance == 1) {
		uncheckedChance = rand() / (double)RAND_MAX;
	}
	double change = uncheckedChance;
	result = (-1 / a) * log(1 - change);

	return result;
}

double rand_pareto(double a) {

	//y = b / (1-x)^(1/a) a>= 1, b>=1 x>=b. a = 2,b = 1로 가정
	double result;
	double uncheckedChance = rand() / (double)RAND_MAX;
	while (uncheckedChance == 0 || uncheckedChance == 1) {
		uncheckedChance = rand() / (double)RAND_MAX;
	}
	double change = uncheckedChance;
	result = 1 / pow(1 - change, 1.0 / a);

	return result;

}

void print_output(double *a, int cond, int R, int state, int di, int G, int dp, int re) {

	double * arr1;
	arr1 = (double *)malloc(sizeof(double) *Dimension);

	for (int i = 0; i < Dimension; i++) {
		arr1[i] = *(a + i);
	}

	char filename[64];
	//R:프로그램 작동횟수, h/c: 배열의 상태 (1 - 최초 2 - 최종 3 - 차이) di: 분포 종류(1 - uniform, 2 - exp 3 - poewr), dp: 분포 파라미터 s: 노드 사이즈, n: 프로세싱 횟수, G: 성장 여부 (0 = 성장 안함, 1 = 성장), re: 투자비율
	if (cond == 0) {
		sprintf(filename, "R%dh%ddi%ddp%ds%dn%dG%dre%d.csv", R, state, di, dp, Dimension, processing_number, G, (re+4));
	}
	else if (cond == 1) {
		sprintf(filename, "R%dc%ddi%ddp%ds%dn%dG%dre%d.csv", R, state, di, dp, Dimension, processing_number, G, (re+4));
	}

	FILE *result = fopen(filename, "w");

	if (cond == 0) {
		fprintf(result, "Hash, Accumulated frequency\n");

	}
	else if (cond == 1) {
		fprintf(result, "Cryptocurrency, Accumulated frequency\n");
	}

	int ac = 0;

	for (int i = 0; i < Dimension - 1; i++) {

		ac++;

		if (arr1[i + 1] < arr1[i]) {
			fprintf(result, "%lf, %d\n", arr1[i], ac);
		}
		/*else {
			fprintf(result, "%lf\n", arr1[i]);
		}*/
	}

	ac++;
	fprintf(result, "%lf, %d\n", arr1[Dimension - 1], ac);

	fclose(result);
	free(arr1);
}

