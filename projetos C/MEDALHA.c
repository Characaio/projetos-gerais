#include<stdio.h>
float main() {
	float sem_medalha,bronze,prata,ouro,pontos;
	
	printf("Digite quantos pontos voce realizou na modalidade olimpica: ");
	scanf("%f", &pontos);
	
	if (pontos < 4)
	{
		printf("Voce nao ganhou nenhuma medalha. ");
	}
	else if ((pontos == 4) || (pontos == 5) || (pontos ==6))
	{
			printf("Voce ganhou medalha de bronze! parabens! ");
	}
	else if ((pontos > 7) && (pontos < 9))
	{
			printf("Voce ganhou a medalha de prata! parabens!. ");
	}
	else if (pontos == 10)
	{
			printf("VOCE GANHOU A MEDALHA DE OURO! PARABENS! ");
	}
	else
	{
			printf("Erro! Digite seus pontos novamente.");
	}
}
	
	
	
	
	
	
	
	

