#include <stdio.h>

float main(){
	float altura,peso,imc;
	printf("Digite sua altura: ");
    scanf("%f", & altura);
    
   	printf("Digite seu peso: ");
    scanf("%f", & peso);
    
    imc= peso / (altura * altura);
    printf("Para o peso de %.1f quilos e %.1f de altura, o seu IMC sera %.3f \n",peso,altura,imc );
    
    if (imc < 18.5) 
    {
     printf(" Seu IMC: %.2f, voce esta abaixo do peso.\n", imc); 
	}
   
    else if ((imc >= 18.5) && (imc < 24.9))

    {
    	printf ("Seu IMC: %.2f voce esta com o peso normal.\n", imc);
	}
     
    else if ((imc > 24.9 ) && (imc < 29.9))	
    {
     printf("Seu IMC: %.2f voce esta sobrepeso.\n", imc); 	
	}
    else if ((imc > 29.9) && (imc <34.9))
    {
    	 printf("Seu IMC: %.2f voce esta com OBESIDADE GRAU 1.\n", imc);
	}
	else{
		printf("erro");
	}
   
      
}

