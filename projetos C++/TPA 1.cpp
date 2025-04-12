#include <iostream>
using namespace std;

int carro(){
    double valor,distancia,km_por_litro, litros, valor_total;
    cout << "qual é o valor da gasolina? \n";
    cin >> valor;
    cout << "qual é a distancia até o seu destino? \n";
    cin >> distancia;
    cout << "quantos kilometros seu carro faz por litro? \n";
    cin >> km_por_litro;
    litros = distancia/km_por_litro;
    cout << "para você percorrer " << distancia << " km, você precisa de " << litros << " litros de gasolina \n";
    valor_total = litros * valor;
    cout << "você precisara pagar " << valor_total << " reais\n";
    return 0;
}
int buffet(){
    int adultos,crianças, adulto_total,criança_total, total;
    cout << "quantas crianças temos? \n";
    cin >> crianças;
    cout << "quantos adultos temos? \n";
    cin >> adultos;
    adulto_total = adultos * 55;
    criança_total = crianças * 25;
    total = adulto_total + criança_total;
    cout << "o preço em total para adultos é de " << adulto_total << " reais \n";
    cout << "o preço em total para crianças é de " << criança_total << " reais \n";
    cout << "o total a ser pago por todos é de " << total << " reais \n";
    return 0;
}
int radar(){
    const int tamanho = 10;
    int velocidades[tamanho] = {10,15,45,70,87,45,67,87,96,23};
    for (int i = 0; i <= (tamanho-1); i++){
        cout << "sua velocidade é de: " << velocidades[i] << ", você";
        if (velocidades[i] > 60)
        {
           cout << " passou do limite de velocidade, tu vai morrer seu corno,/corna \n";
        } else{
            cout << " ta dboa mn, rlxxxxx \n";
        }
        
    }
}

int main()
{
    for (int i = 0; i < 5; i++) {
        if (i == 0)
        {
            carro();
        } else if (i == 1)
        {
            buffet();
        } else if (i == 2)
        {
            radar();
        } else if (i == 3)
        {
            cout << "hiii \n";
        } else if (i == 4)
        {
            cout << "hiiii \n";
        } else if (i == 5)
        {
            cout << "hiiiii \n";
        }
    }
    
}



    
