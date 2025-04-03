#include <iostream>


using namespace std;


void main()
{
    int escolha;
    cout << "escolha um tipo \n" >> "1,2,3 ou 4 \n";
    cin >> escolha;
    if (escolha == 1){
        string nota;
        cout << "qual foi sua nota? \n ";
    
        cin >> nota;
        if ((nota >= 5) && (nota <= 10))
        {
            cout << "aprovado";
        } else if (nota > 10)
        {
            cout << "erro";
        } else{
            cout << "reprovado";
        }
        
        
    }
    
   

}

